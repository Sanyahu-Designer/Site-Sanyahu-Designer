from django.core.management.base import BaseCommand
from portfolio.models import Hero, FeaturedService
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Migra os dados estáticos da página inicial para o banco de dados'

    def handle(self, *args, **kwargs):
        # Migrar dados do Hero
        if not Hero.objects.exists():
            hero = Hero.objects.create(
                title_1="We Create.",
                title_2="We Expand.",
                description="Transform your digital presence with exclusive and innovative solutions.",
                cta_primary_text="View Projects",
                cta_primary_url="#projetos",
                cta_secondary_text="Contact Me",
                cta_secondary_url="#contato",
                image="hero/hero-image.svg"
            )
            self.stdout.write(self.style.SUCCESS('Dados do Hero migrados com sucesso'))

        # Migrar dados dos serviços em destaque
        featured_services_data = [
            {
                'title': 'UI/UX Design',
                'description': 'Intuitive and attractive interfaces that provide the best experience for your users.',
                'icon_svg': '''<svg class="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"/>
                </svg>''',
                'order': 1
            },
            {
                'title': 'Web Development',
                'description': 'Responsive and performance-optimized websites and web applications.',
                'icon_svg': '''<svg class="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
                </svg>''',
                'order': 2
            },
            {
                'title': 'Digital Marketing',
                'description': 'Strategic solutions to increase your online visibility and reach your target audience.',
                'icon_svg': '''<svg class="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z"/>
                </svg>''',
                'order': 3
            }
        ]

        for service_data in featured_services_data:
            service, created = FeaturedService.objects.update_or_create(
                title=service_data['title'],
                defaults={
                    'description': service_data['description'],
                    'icon_svg': service_data['icon_svg'],
                    'order': service_data['order']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Serviço em destaque {service.title} criado com sucesso'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Serviço em destaque {service.title} atualizado com sucesso'))
