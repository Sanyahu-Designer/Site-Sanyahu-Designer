from django.core.management.base import BaseCommand
from django.utils import timezone
from portfolio.models import (
    Category, Tag, Project, Service, Testimonial, About, Skill,
    Experience, Hero, FeaturedService, FAQ, WorkProcess, Post,
    Technology, Footer
)
from django.core.files.base import ContentFile
import requests
from io import BytesIO
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Cria dados de exemplo para o portfolio'

    def handle(self, *args, **kwargs):
        self.stdout.write('Criando dados de exemplo...')

        # Criando Categorias
        categories = [
            {'name': 'Web Design', 'description': 'Projetos de design para web'},
            {'name': 'Desenvolvimento Web', 'description': 'Projetos de desenvolvimento web'},
            {'name': 'UI/UX Design', 'description': 'Projetos de interface e experiência do usuário'},
            {'name': 'Design Gráfico', 'description': 'Projetos de design gráfico e identidade visual'}
        ]
        
        for cat_data in categories:
            Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )

        # Criando Tags
        tags = ['HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'React', 'Vue.js', 'UI/UX', 'Responsive', 'Mobile First']
        for tag_name in tags:
            Tag.objects.get_or_create(name=tag_name)

        # Criando Serviços
        services = [
            {
                'title': 'Design UI/UX',
                'description': '''
                - Wireframes e Protótipos
                - Design System
                - Design Responsivo
                - Testes de Usabilidade
                ''',
                'icon': 'fas fa-pencil-ruler',
                'category': 'ui_ux'
            },
            {
                'title': 'Desenvolvimento Web',
                'description': '''
                - Sites Institucionais
                - E-commerce
                - Sistemas Web
                - APIs RESTful
                ''',
                'icon': 'fas fa-code',
                'category': 'dev'
            },
            {
                'title': 'Design Gráfico',
                'description': '''
                - Identidade Visual
                - Social Media
                - Material Impresso
                - Apresentações
                ''',
                'icon': 'fas fa-palette',
                'category': 'tools'
            }
        ]

        for idx, service_data in enumerate(services):
            Service.objects.get_or_create(
                title=service_data['title'],
                defaults={
                    'description': service_data['description'],
                    'icon': service_data['icon'],
                    'category': service_data['category'],
                    'order': idx
                }
            )

        # Criando Depoimentos
        testimonials = [
            {
                'name': 'João Silva',
                'position': 'CEO',
                'company': 'TechCorp',
                'testimonial': 'Excelente trabalho! O projeto foi entregue no prazo e superou nossas expectativas.'
            },
            {
                'name': 'Maria Santos',
                'position': 'Diretora de Marketing',
                'company': 'Digital Solutions',
                'testimonial': 'Profissional extremamente competente e dedicado. Recomendo fortemente!'
            },
            {
                'name': 'Pedro Oliveira',
                'position': 'Gerente de Projetos',
                'company': 'Inovação Tech',
                'testimonial': 'Ótima experiência! Comunicação clara e resultados impressionantes.'
            }
        ]

        for idx, testimonial_data in enumerate(testimonials):
            Testimonial.objects.get_or_create(
                name=testimonial_data['name'],
                defaults={
                    'position': testimonial_data['position'],
                    'company': testimonial_data['company'],
                    'testimonial': testimonial_data['testimonial'],
                    'order': idx
                }
            )

        # Criando Sobre
        about_text = '''
        Designer e desenvolvedor web com mais de 5 anos de experiência em criar soluções digitais inovadoras. 
        Especializado em UI/UX Design e desenvolvimento full-stack com foco em tecnologias modernas como React, 
        Vue.js e Django.
        '''
        
        About.objects.get_or_create(
            title='Sobre Mim',
            defaults={
                'description': about_text,
            }
        )

        # Criando Habilidades
        skills = [
            {
                'title': 'UI/UX Design',
                'description': 'Design de interfaces e experiência do usuário',
                'icon': 'fas fa-pencil-ruler',
                'skill_type': 'design'
            },
            {
                'title': 'Desenvolvimento Frontend',
                'description': 'HTML, CSS, JavaScript, React, Vue.js',
                'icon': 'fas fa-code',
                'skill_type': 'development'
            },
            {
                'title': 'Desenvolvimento Backend',
                'description': 'Python, Django, Node.js, APIs',
                'icon': 'fas fa-server',
                'skill_type': 'development'
            }
        ]

        for idx, skill_data in enumerate(skills):
            Skill.objects.get_or_create(
                title=skill_data['title'],
                defaults={
                    'description': skill_data['description'],
                    'icon': skill_data['icon'],
                    'skill_type': skill_data['skill_type'],
                    'order': idx
                }
            )

        # Criando Experiências
        experiences = [
            {
                'title': 'Adobe XD',
                'description': 'Design de interfaces e prototipagem',
                'experience_type': 'design',
                'version': '2023',
                'proficiency_level': 'Avançado'
            },
            {
                'title': 'Visual Studio Code',
                'description': 'Editor de código principal',
                'experience_type': 'development',
                'version': 'Latest',
                'proficiency_level': 'Avançado'
            },
            {
                'title': 'Git/GitHub',
                'description': 'Controle de versão e colaboração',
                'experience_type': 'tools',
                'version': 'Latest',
                'proficiency_level': 'Avançado'
            }
        ]

        for idx, exp_data in enumerate(experiences):
            Experience.objects.get_or_create(
                title=exp_data['title'],
                defaults={
                    'description': exp_data['description'],
                    'experience_type': exp_data['experience_type'],
                    'version': exp_data['version'],
                    'proficiency_level': exp_data['proficiency_level'],
                    'order': idx
                }
            )

        # Criando Hero
        hero_data = {
            'title_1': 'Design & Desenvolvimento',
            'title_2': 'Transformando ideias em realidade digital',
            'description': 'Criamos experiências digitais únicas e memoráveis para seu negócio',
            'cta_primary_text': 'Ver Projetos',
            'cta_primary_url': '/projetos/',
            'cta_secondary_text': 'Contato',
            'cta_secondary_url': '/contato/'
        }

        Hero.objects.get_or_create(
            title_1=hero_data['title_1'],
            defaults={
                'title_2': hero_data['title_2'],
                'description': hero_data['description'],
                'cta_primary_text': hero_data['cta_primary_text'],
                'cta_primary_url': hero_data['cta_primary_url'],
                'cta_secondary_text': hero_data['cta_secondary_text'],
                'cta_secondary_url': hero_data['cta_secondary_url']
            }
        )

        # Criando FAQs
        faqs = [
            {
                'question': 'Qual é o prazo médio de entrega de um projeto?',
                'answer': 'O prazo varia de acordo com a complexidade do projeto, mas geralmente entre 4 a 8 semanas.'
            },
            {
                'question': 'Quais tecnologias você utiliza?',
                'answer': 'Trabalho com as tecnologias mais modernas do mercado, incluindo React, Vue.js, Django e Node.js.'
            },
            {
                'question': 'Como funciona o processo de desenvolvimento?',
                'answer': 'O processo inclui análise de requisitos, prototipagem, desenvolvimento, testes e deploy.'
            }
        ]

        for idx, faq_data in enumerate(faqs):
            FAQ.objects.get_or_create(
                question=faq_data['question'],
                defaults={
                    'answer': faq_data['answer'],
                    'order': idx
                }
            )

        # Criando Processo de Trabalho
        processes = [
            {
                'title': 'Descoberta',
                'description': 'Entendemos suas necessidades e objetivos',
                'icon': 'fas fa-search'
            },
            {
                'title': 'Planejamento',
                'description': 'Definimos a melhor estratégia e tecnologias',
                'icon': 'fas fa-tasks'
            },
            {
                'title': 'Design',
                'description': 'Criamos interfaces intuitivas e atraentes',
                'icon': 'fas fa-pencil-ruler'
            },
            {
                'title': 'Desenvolvimento',
                'description': 'Transformamos o design em código funcional',
                'icon': 'fas fa-code'
            }
        ]

        for idx, process_data in enumerate(processes):
            WorkProcess.objects.get_or_create(
                title=process_data['title'],
                defaults={
                    'description': process_data['description'],
                    'icon': process_data['icon'],
                    'order': idx
                }
            )

        # Criando Posts do Blog
        posts = [
            {
                'title': 'Tendências de Design para 2024',
                'description': 'Descubra as principais tendências de design que dominarão 2024',
                'content': '''
                As tendências de design para 2024 estão focadas em:
                
                1. Design Minimalista
                2. Cores Vibrantes
                3. Tipografia Expressiva
                4. Animações Suaves
                5. Dark Mode
                
                Continue lendo para saber mais sobre cada tendência...
                ''',
                'category': 'Design'
            },
            {
                'title': 'Como Melhorar a Performance do seu Site',
                'description': 'Dicas práticas para otimizar a velocidade do seu site',
                'content': '''
                Para melhorar a performance do seu site:
                
                1. Otimize as imagens
                2. Use cache do navegador
                3. Minifique CSS e JavaScript
                4. Utilize CDN
                5. Escolha uma boa hospedagem
                
                Veja mais detalhes sobre cada técnica...
                ''',
                'category': 'Desenvolvimento'
            }
        ]

        for post_data in posts:
            post, created = Post.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'description': post_data['description'],
                    'content': post_data['content'],
                    'category': post_data['category'],
                    'published': True
                }
            )
            if created:
                # Adiciona algumas tags ao post
                post.tags.add(*Tag.objects.all()[:3])

        # Criando Tecnologias
        technologies = [
            {
                'name': 'React',
                'description': 'Biblioteca JavaScript para construção de interfaces',
                'icon': 'fab fa-react'
            },
            {
                'name': 'Django',
                'description': 'Framework web Python de alto nível',
                'icon': 'fab fa-python'
            },
            {
                'name': 'Vue.js',
                'description': 'Framework JavaScript progressivo',
                'icon': 'fab fa-vuejs'
            }
        ]

        for idx, tech_data in enumerate(technologies):
            Technology.objects.get_or_create(
                name=tech_data['name'],
                defaults={
                    'description': tech_data['description'],
                    'icon': tech_data['icon'],
                    'order': idx
                }
            )

        # Criando Footer
        Footer.objects.get_or_create(
            tagline='Transformando ideias em experiências digitais memoráveis'
        )

        # Criando Projetos
        web_design = Category.objects.get(name='Web Design')
        projects = [
            {
                'title': 'E-commerce Moderno',
                'description': 'Desenvolvimento de uma plataforma de e-commerce completa',
                'content': '''
                Projeto de e-commerce desenvolvido com:
                - Frontend em React
                - Backend em Django
                - Pagamentos integrados
                - Painel administrativo personalizado
                ''',
                'technologies': 'React Django PostgreSQL AWS',
                'featured': True
            },
            {
                'title': 'App de Gestão',
                'description': 'Sistema de gestão empresarial responsivo',
                'content': '''
                Sistema completo de gestão com:
                - Dashboard interativo
                - Relatórios em tempo real
                - Gestão de usuários
                - API RESTful
                ''',
                'technologies': 'Vue.js Node.js MongoDB Docker',
                'featured': True
            },
            {
                'title': 'Portal de Notícias',
                'description': 'Portal de notícias com sistema de gestão de conteúdo',
                'content': '''
                Portal completo com:
                - Sistema de categorias
                - Busca avançada
                - Editor de conteúdo rico
                - Cache inteligente
                ''',
                'technologies': 'Django React PostgreSQL Redis',
                'featured': True
            }
        ]

        for idx, project_data in enumerate(projects):
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults={
                    'description': project_data['description'],
                    'content': project_data['content'],
                    'category': web_design,
                    'technologies': project_data['technologies'],
                    'featured': project_data['featured'],
                    'order': idx
                }
            )
            if created:
                # Adiciona algumas tags ao projeto
                project.tags.add(*Tag.objects.all()[:3])

        self.stdout.write(self.style.SUCCESS('Dados de exemplo criados com sucesso!'))
