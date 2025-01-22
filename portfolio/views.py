from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView, DetailView
from .models import Project, FeaturedService, Category, Tag, About, FAQ, WorkProcess, Post, Experience, Skill, Footer, Testimonial
from .forms import ContactForm
from django.contrib import messages
from django.core.cache import cache
from django import forms
from django.utils.translation import gettext as _

# Create your views here.

def get_base_context():
    """Retorna o contexto base que é usado em todas as views"""
    try:
        footer = Footer.objects.latest('created_at')
    except Footer.DoesNotExist:
        footer = None
    
    return {
        'footer': footer,
    }

def home(request):
    context = get_base_context()
    featured_projects = Project.objects.filter(featured=True)[:6]
    services = FeaturedService.objects.all().order_by('order')[:3]
    testimonials = Testimonial.objects.all().order_by('?')[:3]
    
    context.update({
        'featured_projects': featured_projects,
        'services': services,
        'testimonials': testimonials
    })
    return render(request, 'portfolio/home.html', context)

def about(request):
    context = get_base_context()
    about = About.objects.first()
    skills = Skill.objects.all().order_by('order')
    experiences = Experience.objects.all().order_by('order')
    
    context.update({
        'about': about,
        'skills': skills,
        'experiences': experiences,
        'design_experiences': experiences.filter(experience_type='design'),
        'development_experiences': experiences.filter(experience_type='development'),
        'page': 'about'
    })
    return render(request, 'portfolio/about.html', context)

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'project_list'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_base_context())
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        queryset = Project.objects.all().order_by('-created_at')
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_base_context())
        project = self.get_object()
        
        # Get previous and next projects
        try:
            context['previous_project'] = Project.objects.filter(
                created_at__lt=project.created_at
            ).order_by('-created_at').first()
        except Project.DoesNotExist:
            context['previous_project'] = None

        try:
            context['next_project'] = Project.objects.filter(
                created_at__gt=project.created_at
            ).order_by('created_at').first()
        except Project.DoesNotExist:
            context['next_project'] = None
            
        # Get related projects from same category
        context['related_projects'] = Project.objects.filter(
            category=project.category
        ).exclude(id=project.id)[:3]
        
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'portfolio/post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_base_context())
        return context

    def get_queryset(self):
        return Post.objects.filter(published=True)

def services(request):
    context = get_base_context()
    services = FeaturedService.objects.all().order_by('order')
    processes = WorkProcess.objects.all().order_by('order')
    context.update({
        'services': services,
        'processes': processes
    })
    return render(request, 'portfolio/services.html', context)

def blog(request):
    context = get_base_context()
    posts = Post.objects.filter(published=True).order_by('-created_at')
    context.update({
        'posts': posts
    })
    return render(request, 'portfolio/blog.html', context)

def contact(request):
    context = get_base_context()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # Salva o contato com informações adicionais
                contact = form.save(commit=False)
                
                # Salva o IP do usuário
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    contact.ip_address = x_forwarded_for.split(',')[0]
                else:
                    contact.ip_address = request.META.get('REMOTE_ADDR')
                
                # Salva o User Agent
                contact.user_agent = request.META.get('HTTP_USER_AGENT', '')
                
                # Salva a origem do contato
                contact.referrer = request.META.get('HTTP_REFERER', '')
                
                contact.save()

                # Envia e-mail de notificação
                subject = f'Novo contato de {contact.name}'
                message = f'''
                Nome: {contact.name}
                E-mail: {contact.email}
                Assunto: {contact.subject}
                Mensagem: {contact.message}
                
                Informações adicionais:
                IP: {contact.ip_address}
                User Agent: {contact.user_agent}
                Origem: {contact.referrer}
                Data: {contact.created_at}
                '''
                
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )

                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'status': 'success',
                        'message': _('Sua mensagem foi enviada com sucesso! Em breve entraremos em contato.')
                    })
                else:
                    messages.success(request, _('Sua mensagem foi enviada com sucesso! Em breve entraremos em contato.'))
                    form = ContactForm()  # Limpa o formulário
            except Exception as e:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'status': 'error',
                        'message': _('Ocorreu um erro ao enviar sua mensagem. Por favor, tente novamente mais tarde.')
                    })
                else:
                    messages.error(request, _('Ocorreu um erro ao enviar sua mensagem. Por favor, tente novamente mais tarde.'))
        else:
            error_message = ''
            if form.has_error('timestamp'):
                error_message = _('Por favor, aguarde alguns segundos antes de enviar outra mensagem.')
            elif form.has_error('website'):
                error_message = _('Erro de validação. Por favor, tente novamente.')
            else:
                error_message = _('Por favor, corrija os erros no formulário.')
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'error',
                    'message': error_message
                })
            else:
                messages.error(request, error_message)
    else:
        form = ContactForm()

    # Busca as FAQs ordenadas
    faqs = FAQ.objects.all().order_by('order')
    context.update({
        'form': form,
        'faqs': faqs,
        'page': 'contact'
    })
    return render(request, 'portfolio/contact.html', context)
