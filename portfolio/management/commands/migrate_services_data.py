from django.core.management.base import BaseCommand
from portfolio.models import WorkProcess

class Command(BaseCommand):
    help = 'Migra os dados estáticos da página de serviços para o banco de dados'

    def handle(self, *args, **kwargs):
        # Migrar dados do processo de trabalho
        work_process_data = [
            {
                'title': 'Discovery',
                'description': 'Entendemos suas necessidades e objetivos através de uma análise detalhada.',
                'icon': 'fas fa-search',
                'order': 1
            },
            {
                'title': 'Planejamento',
                'description': 'Desenvolvemos uma estratégia clara e definimos as melhores soluções.',
                'icon': 'fas fa-pencil-ruler',
                'order': 2
            },
            {
                'title': 'Desenvolvimento',
                'description': 'Implementamos as soluções com foco em qualidade e performance.',
                'icon': 'fas fa-code',
                'order': 3
            },
            {
                'title': 'Entrega',
                'description': 'Realizamos testes rigorosos e entregamos um produto pronto para uso.',
                'icon': 'fas fa-rocket',
                'order': 4
            }
        ]

        for process_data in work_process_data:
            process, created = WorkProcess.objects.update_or_create(
                title=process_data['title'],
                defaults={
                    'description': process_data['description'],
                    'icon': process_data['icon'],
                    'order': process_data['order']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Processo "{process.title}" criado com sucesso'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Processo "{process.title}" atualizado com sucesso'))
