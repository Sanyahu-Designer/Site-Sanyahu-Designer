from django.core.management.base import BaseCommand
from django.utils import timezone
from portfolio.models import (
    Category, Tag, Project, Service, Testimonial, About, Skill,
    Experience, Hero, FeaturedService, FAQ, WorkProcess, Post,
    Technology, Footer
)
from django.core.files.base import ContentFile
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker('pt_BR')

class Command(BaseCommand):
    help = 'Gera dados fictícios para o portfolio'

    def handle(self, *args, **kwargs):
        self.stdout.write('Gerando dados fictícios...')

        # Criar categorias
        categories = [
            'Web Design',
            'Desenvolvimento Web',
            'UI/UX Design',
            'Design Gráfico',
            'Marketing Digital'
        ]
        for cat in categories:
            Category.objects.create(name=cat)

        # Criar tags
        tags = [
            'Python', 'Django', 'JavaScript', 'React', 'Vue.js',
            'HTML5', 'CSS3', 'Bootstrap', 'MySQL', 'PostgreSQL',
            'AWS', 'Docker', 'Git', 'Node.js', 'PHP'
        ]
        for tag in tags:
            Tag.objects.create(name=tag)

        # Criar projetos
        for i in range(6):
            project = Project.objects.create(
                title=f'Projeto {fake.company()}',
                description=fake.paragraph(),
                content='\n'.join(fake.paragraphs(3)),
                category=Category.objects.order_by('?').first(),
                client=fake.company(),
                url=fake.url(),
                github_url=f'https://github.com/user/project-{i}',
                technologies=', '.join(random.sample(tags, 4)),
                launch_date=fake.date_between(start_date='-2y'),
                featured=random.choice([True, False]),
                order=i
            )
            project.tags.set(Tag.objects.order_by('?')[:4])

        # Criar serviços
        services = [
            ('Design UI/UX', 'ui_ux', 'fas fa-pencil-ruler'),
            ('Desenvolvimento Web', 'dev', 'fas fa-code'),
            ('Marketing Digital', 'tools', 'fas fa-bullhorn')
        ]
        for i, (title, category, icon) in enumerate(services):
            Service.objects.create(
                title=title,
                description=fake.paragraph(),
                icon=icon,
                order=i,
                category=category
            )

        # Criar depoimentos
        for i in range(4):
            Testimonial.objects.create(
                name=fake.name(),
                position=fake.job(),
                company=fake.company(),
                testimonial=fake.paragraph(),
                order=i
            )

        # Criar sobre
        About.objects.create(
            title='Sobre Mim',
            description='\n'.join(fake.paragraphs(3))
        )

        # Criar habilidades
        skills = [
            ('UI Design', 'design', 'fas fa-pencil-alt'),
            ('Frontend', 'development', 'fas fa-code'),
            ('Backend', 'development', 'fas fa-server'),
            ('DevOps', 'tools', 'fas fa-tools')
        ]
        for i, (title, skill_type, icon) in enumerate(skills):
            Skill.objects.create(
                title=title,
                description=fake.paragraph(),
                icon=icon,
                skill_type=skill_type,
                order=i
            )

        # Criar experiências
        experiences = [
            ('Adobe XD', 'design'),
            ('VS Code', 'development'),
            ('Git', 'tools')
        ]
        for i, (title, exp_type) in enumerate(experiences):
            Experience.objects.create(
                title=title,
                description=fake.paragraph(),
                experience_type=exp_type,
                version='2023',
                proficiency_level='Avançado',
                order=i
            )

        # Criar hero
        Hero.objects.create(
            title_1='Olá, eu sou',
            title_2='Designer & Desenvolvedor',
            description=fake.paragraph(),
            cta_primary_text='Ver Projetos',
            cta_primary_url='/projetos',
            cta_secondary_text='Contato',
            cta_secondary_url='/contato'
        )

        # Criar serviços em destaque
        featured_services = [
            'Design de Interface',
            'Desenvolvimento Web',
            'Marketing Digital'
        ]
        for i, service in enumerate(featured_services):
            FeaturedService.objects.create(
                title=service,
                description=fake.paragraph(),
                icon_svg='<svg>...</svg>',
                order=i
            )

        # Criar FAQs
        faqs = [
            'Como funciona o processo de desenvolvimento?',
            'Qual o prazo médio de entrega?',
            'Quais tecnologias você utiliza?'
        ]
        for i, question in enumerate(faqs):
            FAQ.objects.create(
                question=question,
                answer=fake.paragraph(),
                order=i
            )

        # Criar processo de trabalho
        processes = [
            ('Planejamento', 'fas fa-clipboard'),
            ('Design', 'fas fa-paint-brush'),
            ('Desenvolvimento', 'fas fa-code'),
            ('Entrega', 'fas fa-rocket')
        ]
        for i, (title, icon) in enumerate(processes):
            WorkProcess.objects.create(
                title=title,
                description=fake.paragraph(),
                icon=icon,
                order=i
            )

        # Criar posts
        for i in range(5):
            post = Post.objects.create(
                title=fake.sentence(),
                description=fake.paragraph(),
                content='\n'.join(fake.paragraphs(5)),
                published=True,
                category=random.choice(categories),
                order=i
            )
            post.tags.set(Tag.objects.order_by('?')[:3])

        # Criar tecnologias
        technologies = [
            ('Python', 'fab fa-python'),
            ('React', 'fab fa-react'),
            ('Node.js', 'fab fa-node-js')
        ]
        for i, (name, icon) in enumerate(technologies):
            Technology.objects.create(
                name=name,
                description=fake.paragraph(),
                icon=icon,
                order=i
            )

        # Criar footer
        Footer.objects.create(
            tagline='Transformando ideias em realidade digital'
        )

        self.stdout.write(self.style.SUCCESS('Dados fictícios gerados com sucesso!'))
