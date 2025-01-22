from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import logging
from django.core.validators import MinValueValidator, MaxValueValidator
from django_ckeditor_5.fields import CKEditor5Field

logger = logging.getLogger(__name__)

# Create your models here.

class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Slug', unique=True, blank=True)
    description = models.TextField('Descrição', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Tag(models.Model):
    name = models.CharField('Nome', max_length=50)
    slug = models.SlugField('Slug', unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class Project(models.Model):
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', unique=True, blank=True)
    description = models.TextField('Descrição', blank=True)
    content = models.TextField('Conteúdo', blank=True)
    image = models.ImageField('Imagem', upload_to='projects/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    tags = models.ManyToManyField(Tag, verbose_name='Tags')
    client = models.CharField('Cliente', max_length=200, blank=True)
    url = models.URLField('URL do Projeto', blank=True)
    github_url = models.URLField('URL do GitHub', blank=True)
    technologies = models.CharField('Tecnologias', max_length=200)
    launch_date = models.DateField('Data de Lançamento', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    featured = models.BooleanField('Destaque', default=False)
    order = models.IntegerField('Ordem', default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('portfolio:project_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['order', '-created_at']

class Service(models.Model):
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', unique=True, blank=True)
    description = models.TextField('Descrição')
    icon = models.CharField('Ícone', max_length=50, help_text='Nome do ícone do Font Awesome (ex: fas fa-code)')
    order = models.IntegerField('Ordem', default=0)
    category = models.CharField('Categoria', max_length=50, choices=[
        ('ui_ux', 'Design UI/UX'),
        ('dev', 'Desenvolvimento'),
        ('tools', 'Ferramentas')
    ], default='dev')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_features(self):
        features = [
            'Design de Interfaces',
            'Design System',
            'Figma',
            'Design Responsivo'
        ] if self.category == 'ui_ux' else [
            'HTML / CSS / JavaScript',
            'PHP / MySQL',
            'React / Vue.js',
            'Python / Django',
            'Node.js',
            'Git / GitHub'
        ] if self.category == 'dev' else [
            'VS Code',
            'CorelDraw / Inkscape',
            'Jira / Trello',
            'Google Search Console',
            'Google Analytics',
            'Inteligência Artificial'
        ]
        return features

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['order']

class Testimonial(models.Model):
    name = models.CharField('Nome', max_length=200)
    position = models.CharField('Cargo', max_length=200)
    company = models.CharField('Empresa', max_length=200)
    image = models.ImageField('Foto', upload_to='testimonials/', null=True, blank=True)
    testimonial = CKEditor5Field('Depoimento', blank=True, config_name='default')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    order = models.IntegerField('Ordem', default=0)

    def __str__(self):
        return f"{self.name} - {self.company}"

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'
        ordering = ['order', '-created_at']

class Newsletter(models.Model):
    email = models.EmailField('E-mail', unique=True)
    created_at = models.DateTimeField('Data de Inscrição', auto_now_add=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Inscrição Newsletter'
        verbose_name_plural = 'Inscrições Newsletter'
        ordering = ['-created_at']

    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail')
    message = models.TextField('Mensagem')
    created_at = models.DateTimeField('Data de Envio', auto_now_add=True)
    read = models.BooleanField('Lida', default=False)
    replied = models.BooleanField('Respondida', default=False)

    class Meta:
        verbose_name = 'Mensagem de Contato'
        verbose_name_plural = 'Mensagens de Contato'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d/%m/%Y %H:%M')}"

class Contact(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email')
    subject = models.CharField('Assunto', max_length=200)
    message = models.TextField('Mensagem')
    created_at = models.DateTimeField('Data de Envio', auto_now_add=True)
    ip_address = models.GenericIPAddressField('Endereço IP', null=True, blank=True)
    user_agent = models.TextField('User Agent', blank=True)
    submission_time = models.FloatField('Tempo de Preenchimento', default=0)
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.subject}'

class About(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    profile_image = models.ImageField('Foto de Perfil', upload_to='about/')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Sobre'
        verbose_name_plural = 'Sobre'

    def __str__(self):
        return self.title

class Skill(models.Model):
    SKILL_TYPES = (
        ('design', 'Design'),
        ('development', 'Desenvolvimento'),
        ('tools', 'Ferramentas'),
    )
    
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descrição', blank=True)
    icon = models.CharField('Ícone FontAwesome', max_length=50, blank=True)
    skill_type = models.CharField('Tipo', max_length=20, choices=SKILL_TYPES, blank=True)
    order = models.IntegerField('Ordem', default=0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'
        ordering = ['order']

    def __str__(self):
        return self.title

class Experience(models.Model):
    EXPERIENCE_TYPES = (
        ('design', 'Design'),
        ('development', 'Desenvolvimento'),
        ('tools', 'Ferramentas'),
    )
    
    title = models.CharField('Nome do Software/Recurso', max_length=100)
    description = models.TextField('Descrição', blank=True)
    experience_type = models.CharField('Tipo', max_length=20, choices=EXPERIENCE_TYPES, blank=True)
    version = models.CharField('Versão', max_length=50, blank=True)
    proficiency_level = models.CharField('Nível de Proficiência', max_length=50, blank=True)
    order = models.IntegerField('Ordem', default=0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Software/Recurso'
        verbose_name_plural = 'Softwares/Recursos'
        ordering = ['order']

    def __str__(self):
        return self.title

class FeaturedService(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    icon_svg = models.TextField('Ícone SVG')
    order = models.IntegerField('Ordem', default=0)
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Serviço em Destaque'
        verbose_name_plural = 'Serviços em Destaque'
        ordering = ['order']

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField('Pergunta', max_length=200)
    answer = models.TextField('Resposta')
    order = models.IntegerField('Ordem', default=0)
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['order']

    def __str__(self):
        return self.question

class WorkProcess(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    icon = models.CharField('Ícone', max_length=50)
    order = models.IntegerField('Ordem', default=0)
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Processo de Trabalho'
        verbose_name_plural = 'Processos de Trabalho'
        ordering = ['order']

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', max_length=200, unique=True)
    description = models.TextField('Descrição', blank=True)
    content = models.TextField('Conteúdo')
    image = models.ImageField('Imagem', upload_to='blog', blank=True, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    published = models.BooleanField('Publicado', default=False)
    category = models.CharField('Categoria', max_length=100, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tags', blank=True)
    order = models.IntegerField('Ordem', default=0)

    meta_title = models.CharField('Meta Title', max_length=60, blank=True, help_text='Título otimizado para SEO (máx. 60 caracteres)')
    meta_description = models.TextField('Meta Description', max_length=160, blank=True, help_text='Descrição otimizada para SEO (máx. 160 caracteres)')
    meta_keywords = models.CharField('Meta Keywords', max_length=200, blank=True, help_text='Palavras-chave separadas por vírgula')
    focus_keyword = models.CharField('Palavra-chave Principal', max_length=100, blank=True, help_text='Palavra-chave principal para otimização')
    canonical_url = models.URLField('URL Canônica', blank=True, help_text='URL canônica se diferente da URL padrão')
    og_title = models.CharField('OG Title', max_length=60, blank=True, help_text='Título para compartilhamento em redes sociais')
    og_description = models.TextField('OG Description', max_length=200, blank=True, help_text='Descrição para compartilhamento em redes sociais')
    og_image = models.ImageField('OG Image', upload_to='blog/og', blank=True, null=True, help_text='Imagem para compartilhamento (1200x630px)')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.meta_title:
            self.meta_title = self.title[:60]
        if not self.meta_description:
            self.meta_description = self.description[:160] if self.description else ''
        if not self.og_title:
            self.og_title = self.meta_title
        if not self.og_description:
            self.og_description = self.meta_description
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

class Technology(models.Model):
    name = models.CharField('Nome da Tecnologia', max_length=200)
    description = models.TextField('Descrição', blank=True)
    icon = models.CharField('Ícone', max_length=50, help_text='Nome do ícone do Font Awesome (ex: fab fa-wordpress)', blank=True)
    order = models.IntegerField('Ordem', default=0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'
        ordering = ['order']

class Footer(models.Model):
    tagline = models.CharField(
        'Tagline', 
        max_length=500, 
        help_text='Frase principal do footer que aparece em todas as páginas'
    )
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.tagline

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'
        ordering = ['-created_at']
