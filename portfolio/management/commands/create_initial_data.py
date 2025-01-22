from django.core.management.base import BaseCommand
from django.utils.text import slugify
from portfolio.models import Category, Tag, Project, Service

class Command(BaseCommand):
    help = 'Create initial data for the portfolio app'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating initial data...')

        # Create categories
        categories = [
            'Web Design',
            'Mobile Apps',
            'UI/UX Design',
            'Branding'
        ]
        
        for cat_name in categories:
            Category.objects.get_or_create(
                name=cat_name,
                slug=slugify(cat_name)
            )
            self.stdout.write(f'Created category: {cat_name}')

        # Create tags
        tags = [
            'HTML5',
            'CSS3',
            'JavaScript',
            'React',
            'Vue.js',
            'Python',
            'Django',
            'Node.js',
            'Tailwind CSS',
            'Bootstrap',
            'Responsive Design',
            'Mobile First'
        ]
        
        for tag_name in tags:
            Tag.objects.get_or_create(
                name=tag_name,
                slug=slugify(tag_name)
            )
            self.stdout.write(f'Created tag: {tag_name}')

        # Create services
        services = [
            {
                'title': 'Design UI/UX',
                'description': 'Interfaces intuitivas e atraentes que proporcionam a melhor experiência para seus usuários.',
                'icon': 'fas fa-pencil-ruler'
            },
            {
                'title': 'Desenvolvimento Web',
                'description': 'Websites e aplicações web modernas, responsivas e otimizadas para performance.',
                'icon': 'fas fa-code'
            },
            {
                'title': 'Marketing Digital',
                'description': 'Estratégias eficientes para aumentar sua visibilidade online e atrair mais clientes.',
                'icon': 'fas fa-bullhorn'
            },
            {
                'title': 'SEO',
                'description': 'Otimização para mecanismos de busca para melhorar seu ranking no Google.',
                'icon': 'fas fa-search'
            }
        ]
        
        for idx, service_data in enumerate(services):
            Service.objects.get_or_create(
                title=service_data['title'],
                defaults={
                    'description': service_data['description'],
                    'icon': service_data['icon'],
                    'order': idx
                }
            )
            self.stdout.write(f'Created service: {service_data["title"]}')

        # Create projects
        web_design = Category.objects.get(name='Web Design')
        html_tag = Tag.objects.get(name='HTML5')
        css_tag = Tag.objects.get(name='CSS3')
        js_tag = Tag.objects.get(name='JavaScript')
        react_tag = Tag.objects.get(name='React')
        tailwind_tag = Tag.objects.get(name='Tailwind CSS')

        projects = [
            {
                'title': 'E-commerce Moderno',
                'description': 'Uma plataforma de e-commerce moderna e responsiva com foco em UX.',
                'content': '''
                # E-commerce Moderno

                Uma plataforma de e-commerce moderna e responsiva desenvolvida com React e Tailwind CSS.
                O projeto inclui:

                - Design responsivo
                - Carrinho de compras
                - Sistema de pagamento
                - Painel administrativo
                - Otimização SEO
                ''',
                'category': web_design,
                'tags': [html_tag, css_tag, js_tag, react_tag, tailwind_tag],
                'client': 'Fashion Store',
                'url': 'https://fashionstore.com',
                'github_url': 'https://github.com/sanyahu/fashion-store',
                'technologies': 'React, Next.js, Tailwind CSS, Node.js',
                'featured': True,
                'order': 0
            }
        ]
        
        for project_data in projects:
            tags = project_data.pop('tags')
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                project.tags.add(*tags)
                self.stdout.write(f'Created project: {project.title}')

        self.stdout.write(self.style.SUCCESS('Successfully created initial data'))
