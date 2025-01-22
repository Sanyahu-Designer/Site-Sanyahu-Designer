import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_config.settings')
django.setup()

from django.contrib.auth.models import User
from portfolio.models import Project, Service, Testimonial, Category, Tag

def create_superuser():
    if not User.objects.filter(username='sanyahu').exists():
        User.objects.create_superuser('sanyahu', 'arte@sanyahudesigner.com.br', 'sua_senha_aqui')
        print('Superuser created successfully!')

def create_categories():
    categories = [
        'Desenvolvimento Web',
        'Design Gráfico',
        'Full Stack'
    ]
    
    created_categories = {}
    for category_name in categories:
        category, created = Category.objects.get_or_create(name=category_name)
        created_categories[category_name] = category
    print('Categories created successfully!')
    return created_categories

def create_tags():
    tags = [
        'Python',
        'Django',
        'React',
        'JavaScript',
        'TypeScript',
        'TailwindCSS',
        'MariaDB',
        'Docker',
        'Git',
        'AWS',
        'Adobe Illustrator',
        'Adobe Photoshop',
        'Figma'
    ]
    
    created_tags = {}
    for tag_name in tags:
        tag, created = Tag.objects.get_or_create(name=tag_name)
        created_tags[tag_name] = tag
    print('Tags created successfully!')
    return created_tags

def create_projects(categories, tags):
    projects = [
        {
            'title': 'Sistema de Gestão de Eventos',
            'description': '''
            <h3>Plataforma Completa para Gestão de Eventos</h3>
            <p>Desenvolvimento de uma plataforma web robusta para gerenciamento de eventos, 
            incluindo venda de ingressos, gestão de participantes e análise de dados.</p>
            
            <h4>Funcionalidades Principais:</h4>
            <ul>
                <li>Sistema de autenticação e autorização</li>
                <li>Painel administrativo personalizado</li>
                <li>Integração com gateway de pagamento</li>
                <li>Geração de relatórios e análises</li>
                <li>Sistema de notificações em tempo real</li>
                <li>API RESTful para integração com aplicativos móveis</li>
            </ul>
            
            <h4>Tecnologias Utilizadas:</h4>
            <p>Backend desenvolvido em Django com DRF, frontend em React com TypeScript, 
            e estilização usando TailwindCSS. Toda a infraestrutura foi configurada na AWS 
            usando containers Docker.</p>
            ''',
            'technologies': 'Python, Django, React, TypeScript, TailwindCSS, MariaDB, Docker, AWS',
            'featured': True,
            'url': 'https://github.com/sanyahu',
            'category': 'Full Stack',
            'project_tags': ['Python', 'Django', 'React', 'TypeScript', 'TailwindCSS', 'MariaDB', 'Docker', 'AWS']
        },
        {
            'title': 'E-commerce com Django e React',
            'description': '''
            <h3>Plataforma de E-commerce Moderna</h3>
            <p>Desenvolvimento de uma plataforma de e-commerce completa com funcionalidades 
            avançadas e design responsivo.</p>
            
            <h4>Características:</h4>
            <ul>
                <li>Catálogo de produtos dinâmico</li>
                <li>Sistema de carrinho de compras</li>
                <li>Gestão de estoque em tempo real</li>
                <li>Dashboard administrativo personalizado</li>
                <li>Sistema de busca avançado</li>
                <li>Integração com múltiplos meios de pagamento</li>
            </ul>
            
            <h4>Stack Tecnológico:</h4>
            <p>Aplicação construída com Django no backend e React no frontend, utilizando 
            MariaDB como banco de dados e Docker para containerização.</p>
            ''',
            'technologies': 'Python, Django, React, MariaDB, Docker',
            'featured': True,
            'url': 'https://github.com/sanyahu',
            'category': 'Full Stack',
            'project_tags': ['Python', 'Django', 'React', 'MariaDB', 'Docker']
        },
        {
            'title': 'Sistema de Blog com Django',
            'description': '''
            <h3>Blog Profissional com Django</h3>
            <p>Desenvolvimento de um sistema de blog moderno e otimizado para SEO, 
            com funcionalidades avançadas de gestão de conteúdo.</p>
            
            <h4>Recursos:</h4>
            <ul>
                <li>Editor de texto rico</li>
                <li>Sistema de tags e categorias</li>
                <li>Comentários com moderação</li>
                <li>Otimização para SEO</li>
                <li>Sistema de newsletters</li>
                <li>Analytics integrado</li>
            </ul>
            
            <h4>Implementação:</h4>
            <p>Desenvolvido com Django e MariaDB, utilizando TailwindCSS para 
            estilização e Docker para deploy.</p>
            ''',
            'technologies': 'Python, Django, MariaDB, TailwindCSS, Docker',
            'featured': True,
            'url': 'https://github.com/sanyahu',
            'category': 'Desenvolvimento Web',
            'project_tags': ['Python', 'Django', 'MariaDB', 'TailwindCSS', 'Docker']
        }
    ]
    
    for project in projects:
        category = categories[project['category']]
        project_obj, created = Project.objects.get_or_create(
            title=project['title'],
            defaults={
                'description': project['description'],
                'technologies': project['technologies'],
                'featured': project['featured'],
                'url': project['url'],
                'category': category
            }
        )
        
        if created:
            # Adicionar tags ao projeto
            for tag_name in project['project_tags']:
                project_obj.tags.add(tags[tag_name])
                
    print('Projects created successfully!')

def create_services():
    services = [
        {
            'title': 'Desenvolvimento Web Full Stack',
            'description': '''Desenvolvimento completo de aplicações web, desde o backend até o frontend. 
            Utilizando as melhores práticas e tecnologias modernas como Python, Django, React e mais. 
            Foco em código limpo, escalável e de fácil manutenção.''',
            'icon': 'fas fa-code',
            'category': 'dev'
        },
        {
            'title': 'Design de Identidade Visual',
            'description': '''Desenvolvimento completo de identidade visual para sua marca, incluindo logotipo, 
            paleta de cores, tipografia e manual de marca. Criação pensada estrategicamente para comunicar 
            os valores e a essência do seu negócio.''',
            'icon': 'fas fa-paint-brush',
            'category': 'ui_ux'
        },
        {
            'title': 'Desenvolvimento Backend',
            'description': '''Criação de APIs robustas e escaláveis utilizando Python e Django. 
            Implementação de sistemas seguros, otimizados e bem documentados. Experiência com 
            bancos de dados SQL e NoSQL, cache, mensageria e mais.''',
            'icon': 'fas fa-database',
            'category': 'dev'
        },
        {
            'title': 'Desenvolvimento Frontend',
            'description': '''Desenvolvimento de interfaces modernas e responsivas utilizando React, 
            TypeScript e TailwindCSS. Foco em performance, acessibilidade e experiência do usuário.''',
            'icon': 'fas fa-laptop-code',
            'category': 'dev'
        },
        {
            'title': 'Design Editorial',
            'description': '''Criação e diagramação de materiais editoriais como revistas, catálogos, 
            e-books e apresentações. Layout clean e profissional com foco na experiência do leitor 
            e na comunicação efetiva do conteúdo.''',
            'icon': 'fas fa-book',
            'category': 'ui_ux'
        },
        {
            'title': 'DevOps e Deploy',
            'description': '''Configuração e manutenção de infraestrutura usando Docker, AWS e outras 
            tecnologias cloud. Implementação de CI/CD, monitoramento e escalabilidade.''',
            'icon': 'fas fa-server',
            'category': 'dev'
        }
    ]
    
    for service in services:
        Service.objects.get_or_create(
            title=service['title'],
            defaults={
                'description': service['description'],
                'icon': service['icon'],
                'category': service['category']
            }
        )
    print('Services created successfully!')

def create_testimonials():
    testimonials = [
        {
            'name': 'Ricardo Oliveira',
            'position': 'CTO',
            'company': 'TechStart Solutions',
            'testimonial': '''O sistema de gestão de eventos desenvolvido superou todas as nossas expectativas. 
            A qualidade do código e a atenção aos detalhes foram impressionantes.'''
        },
        {
            'name': 'Amanda Santos',
            'position': 'Gerente de Projetos',
            'company': 'E-commerce Brasil',
            'testimonial': '''A plataforma de e-commerce desenvolvida revolucionou nossa operação online. 
            O sistema é robusto, rápido e muito fácil de usar.'''
        },
        {
            'name': 'Carolina Mendes',
            'position': 'Diretora de Marketing',
            'company': 'Revista Digital',
            'testimonial': '''Além do excelente trabalho de desenvolvimento web, o design editorial 
            do nosso site ficou excepcional. Um profissional completo que entende tanto de código 
            quanto de design.'''
        }
    ]
    
    for testimonial in testimonials:
        Testimonial.objects.get_or_create(
            name=testimonial['name'],
            defaults={
                'position': testimonial['position'],
                'company': testimonial['company'],
                'testimonial': testimonial['testimonial']
            }
        )
    print('Testimonials created successfully!')

if __name__ == '__main__':
    print('Starting database population with real data...')
    create_superuser()
    categories = create_categories()
    tags = create_tags()
    create_projects(categories, tags)
    create_services()
    create_testimonials()
    print('Database population completed successfully!')
