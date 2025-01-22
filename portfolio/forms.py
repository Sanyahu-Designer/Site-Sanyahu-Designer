from django import forms
from .models import Contact
import time
from django.core.cache import cache

class ContactForm(forms.ModelForm):
    # Campo honeypot - bots tendem a preencher campos ocultos
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'style': 'display:none !important; position:absolute !important; left:-9999px !important;',
            'tabindex': '-1',
            'autocomplete': 'off'
        })
    )
    
    # Campo para armazenar o timestamp inicial
    timestamp = forms.FloatField(
        widget=forms.HiddenInput,
        required=False
    )
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-gold-primary focus:border-transparent',
                'placeholder': 'Seu nome'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-gold-primary focus:border-transparent',
                'placeholder': 'seu@email.com'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-gold-primary focus:border-transparent',
                'placeholder': 'Assunto da mensagem'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-gold-primary focus:border-transparent',
                'placeholder': 'Sua mensagem',
                'rows': 5
            })
        }
        labels = {
            'name': 'Nome',
            'email': 'E-mail',
            'subject': 'Assunto',
            'message': 'Mensagem'
        }
        error_messages = {
            'name': {
                'required': 'Por favor, informe seu nome.'
            },
            'email': {
                'required': 'Por favor, informe seu e-mail.',
                'invalid': 'Por favor, informe um e-mail válido.'
            },
            'subject': {
                'required': 'Por favor, informe o assunto.'
            },
            'message': {
                'required': 'Por favor, escreva sua mensagem.'
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona o timestamp inicial quando o formulário é criado
        if not self.is_bound:  # Apenas quando o formulário é novo
            self.initial['timestamp'] = time.time()

    def clean(self):
        cleaned_data = super().clean()

        # 1. Verifica o campo honeypot
        if cleaned_data.get('website'):
            raise forms.ValidationError(
                'Spam detectado.'
            )

        # 2. Verifica o tempo de preenchimento
        timestamp = cleaned_data.get('timestamp')
        if timestamp:
            submission_time = time.time() - float(timestamp)
            if submission_time < 3:  # Muito rápido para ser humano
                raise forms.ValidationError(
                    'Por favor, leia o formulário com atenção antes de enviar.'
                )
            # Salva o tempo de preenchimento para usar no save
            cleaned_data['submission_time'] = submission_time

        return cleaned_data

    def save(self, commit=True, request=None):
        instance = super().save(commit=False)
        # Salva o tempo de preenchimento
        if 'submission_time' in self.cleaned_data:
            instance.submission_time = self.cleaned_data['submission_time']

        if request:
            # Salva o IP do usuário
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                instance.ip_address = x_forwarded_for.split(',')[0]
            else:
                instance.ip_address = request.META.get('REMOTE_ADDR')

            # Salva o User Agent
            instance.user_agent = request.META.get('HTTP_USER_AGENT', '')

            # Verifica rate limiting
            cache_key = f'contact_form_{instance.ip_address}'
            submission_count = cache.get(cache_key, 0)

            if submission_count >= 5:  # Máximo de 5 submissões por hora
                raise forms.ValidationError(
                    'Muitas tentativas. Por favor, aguarde um momento antes de tentar novamente.'
                )

            # Incrementa o contador
            cache.set(cache_key, submission_count + 1, 3600)  # Expira em 1 hora

        if commit:
            instance.save()

        return instance
