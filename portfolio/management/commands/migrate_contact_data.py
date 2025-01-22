from django.core.management.base import BaseCommand
from portfolio.models import FAQ

class Command(BaseCommand):
    help = 'Migra os dados estáticos da página de contato para o banco de dados'

    def handle(self, *args, **kwargs):
        # Migrar FAQs
        faqs_data = [
            {
                'question': 'Qual é o prazo médio de um projeto?',
                'answer': '''O prazo de desenvolvimento varia de acordo com a complexidade e escopo do projeto. 
                Em média, um site institucional leva de 30 a 45 dias para ser concluído. Durante nossa conversa inicial, 
                poderei fornecer uma estimativa mais precisa com base nas suas necessidades específicas.''',
                'order': 1
            },
            {
                'question': 'Como funciona o processo de desenvolvimento?',
                'answer': '''O processo começa com uma reunião de briefing onde entendemos suas necessidades. 
                Em seguida, desenvolvemos o layout e, após sua aprovação, iniciamos a programação. 
                Você acompanha todo o processo e recebe atualizações regulares sobre o andamento do projeto.''',
                'order': 2
            },
            {
                'question': 'Quais formas de pagamento são aceitas?',
                'answer': '''Aceito diversas formas de pagamento, incluindo transferência bancária, PIX e cartão de crédito. 
                O pagamento geralmente é dividido em etapas: uma entrada no início do projeto e o restante 
                distribuído de acordo com as entregas.''',
                'order': 3
            },
            {
                'question': 'Oferecem suporte após a entrega do projeto?',
                'answer': '''Sim! Após a entrega do projeto, oferecemos um período de suporte gratuito para ajustes 
                e correções. Também disponibilizamos pacotes de manutenção mensal para atualizações contínuas 
                e melhorias no seu site.''',
                'order': 4
            }
        ]

        for faq_data in faqs_data:
            faq, created = FAQ.objects.update_or_create(
                question=faq_data['question'],
                defaults={
                    'answer': faq_data['answer'],
                    'order': faq_data['order']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'FAQ "{faq.question}" criada com sucesso'))
            else:
                self.stdout.write(self.style.SUCCESS(f'FAQ "{faq.question}" atualizada com sucesso'))
