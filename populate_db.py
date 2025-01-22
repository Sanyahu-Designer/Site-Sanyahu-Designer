import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_config.settings')
django.setup()

from django.contrib.auth.models import User
from portfolio.models import Project, Service, Testimonial
from blog.models import Category, Post

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print('Superuser created successfully!')

def create_projects():
    projects = [
        {
            'title': 'E-commerce Platform',
            'description': '''
            <h3>Project Overview</h3>
            <p>A full-featured e-commerce platform built with Django and React. This project showcases my ability to create complex, scalable web applications.</p>
            
            <h4>Key Features:</h4>
            <ul>
                <li>User authentication and authorization</li>
                <li>Product catalog with categories and filters</li>
                <li>Shopping cart and checkout system</li>
                <li>Payment integration with Stripe</li>
                <li>Order management and tracking</li>
                <li>Admin dashboard for inventory management</li>
            </ul>
            
            <h4>Technical Details:</h4>
            <p>The backend is built with Django REST Framework, featuring comprehensive API documentation and test coverage. The frontend utilizes React with Redux for state management and Material-UI for the interface.</p>
            ''',
            'technologies': 'Django, React, PostgreSQL, Redis, Docker',
            'is_featured': True,
            'github_url': 'https://github.com/example/ecommerce',
            'url': 'https://ecommerce-demo.example.com'
        },
        {
            'title': 'AI Image Generator',
            'description': '''
            <h3>Project Description</h3>
            <p>An innovative AI-powered image generation tool that creates unique artwork based on text descriptions.</p>
            
            <h4>Features:</h4>
            <ul>
                <li>Text-to-image generation using Stable Diffusion</li>
                <li>Style transfer capabilities</li>
                <li>Image manipulation tools</li>
                <li>Gallery for generated images</li>
                <li>Social sharing integration</li>
            </ul>
            
            <h4>Technical Stack:</h4>
            <p>Built with Python and PyTorch for the AI components, FastAPI for the backend, and Vue.js for the frontend. Deployed on AWS using containerization for scalability.</p>
            ''',
            'technologies': 'Python, PyTorch, FastAPI, Vue.js, AWS',
            'is_featured': True,
            'github_url': 'https://github.com/example/ai-image-gen',
            'url': 'https://ai-image-gen.example.com'
        },
        {
            'title': 'Task Management System',
            'description': '''
            <h3>Overview</h3>
            <p>A comprehensive task management system designed for remote teams, featuring real-time updates and collaboration tools.</p>
            
            <h4>Key Features:</h4>
            <ul>
                <li>Real-time task updates and notifications</li>
                <li>Team collaboration tools</li>
                <li>Time tracking and reporting</li>
                <li>Project analytics dashboard</li>
                <li>Integration with popular tools (Slack, GitHub)</li>
            </ul>
            
            <h4>Implementation Details:</h4>
            <p>Built using Django Channels for real-time functionality, React for the frontend, and PostgreSQL for data storage. Implements WebSocket connections for live updates.</p>
            ''',
            'technologies': 'Django, React, WebSocket, PostgreSQL',
            'is_featured': True,
            'github_url': 'https://github.com/example/task-manager',
            'url': 'https://task-manager-demo.example.com'
        }
    ]
    
    for project in projects:
        Project.objects.get_or_create(
            title=project['title'],
            defaults={
                'description': project['description'],
                'technologies': project['technologies'],
                'is_featured': project['is_featured'],
                'github_url': project['github_url'],
                'url': project['url']
            }
        )
    print('Projects created successfully!')

def create_services():
    services = [
        {
            'title': 'Full Stack Development',
            'description': '''
            <h3>End-to-End Web Development Solutions</h3>
            <p>Comprehensive web development services covering both frontend and backend development. From concept to deployment, I deliver scalable and maintainable solutions.</p>
            
            <h4>Services Include:</h4>
            <ul>
                <li>Custom web application development</li>
                <li>API development and integration</li>
                <li>Database design and optimization</li>
                <li>Frontend development with modern frameworks</li>
                <li>Performance optimization and scaling</li>
            </ul>
            ''',
            'icon': 'fas fa-code',
            'order': 1
        },
        {
            'title': 'Cloud Architecture',
            'description': '''
            <h3>Cloud Solutions Architecture</h3>
            <p>Expert cloud architecture services to help businesses leverage the power of cloud computing. Specialized in AWS and Google Cloud Platform.</p>
            
            <h4>Expertise Areas:</h4>
            <ul>
                <li>Cloud migration strategies</li>
                <li>Serverless architecture design</li>
                <li>Microservices implementation</li>
                <li>DevOps automation</li>
                <li>Cloud security best practices</li>
            </ul>
            ''',
            'icon': 'fas fa-cloud',
            'order': 2
        },
        {
            'title': 'AI/ML Solutions',
            'description': '''
            <h3>Artificial Intelligence & Machine Learning</h3>
            <p>Cutting-edge AI and ML solutions to help businesses automate processes and gain valuable insights from their data.</p>
            
            <h4>Services Offered:</h4>
            <ul>
                <li>Custom ML model development</li>
                <li>Natural Language Processing</li>
                <li>Computer Vision solutions</li>
                <li>Predictive analytics</li>
                <li>AI integration with existing systems</li>
            </ul>
            ''',
            'icon': 'fas fa-brain',
            'order': 3
        }
    ]
    
    for service in services:
        Service.objects.get_or_create(
            title=service['title'],
            defaults={
                'description': service['description'],
                'icon': service['icon'],
                'order': service['order']
            }
        )
    print('Services created successfully!')

def create_testimonials():
    testimonials = [
        {
            'name': 'John Smith',
            'position': 'CTO',
            'company': 'Tech Innovations Inc.',
            'testimonial': '''
            <p>Working with this developer was an absolute pleasure. Their technical expertise and attention to detail helped us launch our platform ahead of schedule. The code quality and documentation were exceptional.</p>
            ''',
            'order': 1
        },
        {
            'name': 'Sarah Johnson',
            'position': 'Product Manager',
            'company': 'Digital Solutions Ltd.',
            'testimonial': '''
            <p>Exceptional problem-solving skills and great communication throughout the project. They not only delivered what we asked for but also suggested improvements that made our product even better.</p>
            ''',
            'order': 2
        },
        {
            'name': 'Michael Chen',
            'position': 'Founder',
            'company': 'StartupX',
            'testimonial': '''
            <p>Their expertise in both frontend and backend development was crucial for our startup. They helped us build a scalable MVP that attracted significant investor interest.</p>
            ''',
            'order': 3
        }
    ]
    
    for testimonial in testimonials:
        Testimonial.objects.get_or_create(
            name=testimonial['name'],
            defaults={
                'position': testimonial['position'],
                'company': testimonial['company'],
                'testimonial': testimonial['testimonial'],
                'order': testimonial['order']
            }
        )
    print('Testimonials created successfully!')

def create_blog_categories():
    categories = [
        {
            'name': 'Web Development',
            'description': 'Articles about web development technologies and best practices'
        },
        {
            'name': 'Cloud Computing',
            'description': 'Posts about cloud architecture and services'
        },
        {
            'name': 'Artificial Intelligence',
            'description': 'Insights into AI and machine learning'
        }
    ]
    
    for category in categories:
        Category.objects.get_or_create(
            name=category['name'],
            defaults={
                'description': category['description']
            }
        )
    print('Blog categories created successfully!')

def create_blog_posts():
    posts = [
        {
            'title': 'Building Scalable Web Applications with Django',
            'content': '''
            <h2>Introduction</h2>
            <p>Django is a powerful framework for building web applications, but scaling them requires careful consideration and proper architecture.</p>
            
            <h3>Key Considerations for Scalability</h3>
            <ul>
                <li>Database optimization</li>
                <li>Caching strategies</li>
                <li>Asynchronous processing</li>
                <li>Load balancing</li>
            </ul>
            
            <h3>Best Practices</h3>
            <p>In this article, we'll explore the best practices for building scalable Django applications, including code examples and real-world scenarios.</p>
            
            <h4>1. Database Optimization</h4>
            <pre><code>
            # Example of database optimization
            from django.db.models import prefetch_related
            
            def get_articles():
                return Article.objects.prefetch_related('author', 'categories').all()
            </code></pre>
            
            <h4>2. Caching Implementation</h4>
            <p>Proper caching can significantly improve your application's performance...</p>
            ''',
            'excerpt': 'Learn how to build scalable web applications using Django, including best practices for database optimization, caching, and more.',
            'category': 'Web Development',
            'is_featured': True
        },
        {
            'title': 'Understanding Cloud Native Architecture',
            'content': '''
            <h2>Cloud Native Architecture</h2>
            <p>Cloud native architecture is revolutionizing how we build and deploy applications. Let's explore the key concepts and benefits.</p>
            
            <h3>Core Principles</h3>
            <ul>
                <li>Microservices</li>
                <li>Containers</li>
                <li>DevOps automation</li>
                <li>Continuous delivery</li>
            </ul>
            
            <h3>Implementation Strategies</h3>
            <p>We'll discuss various strategies for implementing cloud native architecture in your organization...</p>
            
            <h4>1. Microservices Architecture</h4>
            <pre><code>
            # Example Docker configuration
            version: '3'
            services:
              web:
                build: .
                ports:
                  - "8000:8000"
              redis:
                image: "redis:alpine"
            </code></pre>
            ''',
            'excerpt': 'Dive deep into cloud native architecture, exploring microservices, containers, and DevOps practices.',
            'category': 'Cloud Computing',
            'is_featured': True
        },
        {
            'title': 'Getting Started with Machine Learning in Python',
            'content': '''
            <h2>Machine Learning Basics</h2>
            <p>Python has become the go-to language for machine learning. Let's explore how to get started with ML using Python.</p>
            
            <h3>Essential Libraries</h3>
            <ul>
                <li>NumPy</li>
                <li>Pandas</li>
                <li>Scikit-learn</li>
                <li>TensorFlow</li>
            </ul>
            
            <h3>Your First ML Model</h3>
            <pre><code>
            import numpy as np
            from sklearn.model_selection import train_test_split
            from sklearn.linear_model import LinearRegression
            
            # Example of training a simple linear regression model
            X = np.random.rand(100, 1)
            y = 2 * X + 1 + np.random.randn(100, 1) * 0.1
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            model = LinearRegression()
            model.fit(X_train, y_train)
            </code></pre>
            ''',
            'excerpt': 'Learn the basics of machine learning using Python, including essential libraries and your first ML model.',
            'category': 'Artificial Intelligence',
            'is_featured': True
        }
    ]
    
    for post in posts:
        category = Category.objects.get(name=post['category'])
        Post.objects.get_or_create(
            title=post['title'],
            defaults={
                'content': post['content'],
                'excerpt': post['excerpt'],
                'category': category,
                'is_featured': post['is_featured']
            }
        )
    print('Blog posts created successfully!')

if __name__ == '__main__':
    print('Starting database population...')
    create_superuser()
    create_projects()
    create_services()
    create_testimonials()
    create_blog_categories()
    create_blog_posts()
    print('Database population completed!')
