from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, Project, Service

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('portfolio:post_detail', kwargs={'slug': obj.slug})

class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('portfolio:project_detail', kwargs={'slug': obj.slug})

class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('portfolio:services') + f'#{obj.slug}'

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = "monthly"

    def items(self):
        return ['home', 'about', 'services', 'contact', 'projects', 'blog']

    def location(self, item):
        return reverse(f'portfolio:{item}')
