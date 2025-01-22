from django.core.management.base import BaseCommand
from portfolio.models import About, Service
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Migra os dados estáticos do template para o banco de dados'

    def handle(self, *args, **kwargs):
        # Migrar dados da página Sobre
        if not About.objects.exists():
            about = About.objects.create(
                title="Sobre Mim",
                content="""
                <h2>Olá, eu sou o Sanyahu</h2>
                <p>Com mais de 20 anos de experiência em design e desenvolvimento web, dedico minha carreira a criar soluções digitais que não apenas impressionam visualmente, mas também geram resultados concretos para os meus clientes.</p>
                
                <p>Combinando princípios sólidos de design com as mais recentes tecnologias da web, crio experiências digitais que se destacam. Acredito que cada projeto é uma oportunidade única para inovar e superar expectativas. Atualmente, estou focado no aprimoramento do meu conhecimento em Python.</p>
                
                <p>Quando não estou codificando ou projetando interfaces gráficas e web, geralmente estou compartilhando conhecimento em meu blog ou explorando novas tecnologias e tendências de design.</p>
                """,
                meta_description="Conheça mais sobre minha trajetória como designer e desenvolvedor web. Descubra minha paixão por criar experiências digitais únicas e impactantes."
            )
            self.stdout.write(self.style.SUCCESS('Dados da página Sobre migrados com sucesso'))

        # Migrar dados dos serviços
        services_data = [
            {
                'title': 'Design UI/UX',
                'description': """
                <ul class="space-y-2 text-text-light">
                    <li>Design de Interfaces</li>
                    <li>Prototipagem</li>
                    <li>Design System</li>
                    <li>Figma / Adobe XD</li>
                    <li>Design Responsivo</li>
                </ul>
                """,
                'icon': 'fas fa-pencil-ruler',
                'order': 1
            },
            {
                'title': 'Desenvolvimento',
                'description': """
                <ul class="space-y-2 text-text-light">
                    <li>HTML / CSS / JavaScript</li>
                    <li>PHP / MySQL</li>
                    <li>React / Vue.js</li>
                    <li>Python / Django</li>
                    <li>Node.js</li>
                    <li>Git / GitHub</li>
                </ul>
                """,
                'icon': 'fas fa-code',
                'order': 2
            },
            {
                'title': 'Ferramentas',
                'description': """
                <ul class="space-y-2 text-text-light">
                    <li>VS Code</li>
                    <li>Coreldraw</li>
                    <li>Inkscape</li>
                    <li>Jira / Trello</li>
                    <li>Google Search Console</li>
                    <li>Google Analytics</li>
                    <li>Inteligência Artificial</li>
                </ul>
                """,
                'icon': 'fas fa-tools',
                'order': 3
            }
        ]

        for service_data in services_data:
            service_slug = slugify(service_data['title'])
            service, created = Service.objects.update_or_create(
                slug=service_slug,
                defaults={
                    'title': service_data['title'],
                    'description': service_data['description'],
                    'icon': service_data['icon'],
                    'order': service_data['order']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Serviço {service.title} criado com sucesso'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Serviço {service.title} atualizado com sucesso'))
