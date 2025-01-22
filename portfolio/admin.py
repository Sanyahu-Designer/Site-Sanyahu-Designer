from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from .models import Project, Service, Category, Tag, Contact, Testimonial, About, FeaturedService, FAQ, WorkProcess, Post, Experience, Skill, Footer

# Formulários personalizados com CKEditor
class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'description': CKEditor5Widget(config_name='default'),
            'content': CKEditor5Widget(config_name='default')
        }

class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'description': CKEditor5Widget(config_name='default')
        }

class TestimonialAdminForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
        widgets = {
            'testimonial': CKEditor5Widget(config_name='default')
        }

class AboutAdminForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(config_name='default')
        }

class FeaturedServiceAdminForm(forms.ModelForm):
    class Meta:
        model = FeaturedService
        fields = '__all__'
        widgets = {
            'description': CKEditor5Widget(config_name='default')
        }

class FAQAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer': CKEditor5Widget(config_name='default')
        }

class WorkProcessAdminForm(forms.ModelForm):
    class Meta:
        model = WorkProcess
        fields = '__all__'
        widgets = {
            'description': CKEditor5Widget(config_name='default')
        }

# Definição das classes Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('title', 'featured', 'category', 'created_at')
    list_filter = ('featured', 'category', 'tags')
    search_fields = ('title', 'description', 'client')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    filter_horizontal = ('tags',)

class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ('title', 'category', 'order')
    list_filter = ('category',)
    list_editable = ('order',)
    search_fields = ('title', 'description')
    fieldsets = (
        ('Informações', {
            'fields': ('title', 'description', 'icon', 'category', 'order')
        }),
    )

class TestimonialAdmin(admin.ModelAdmin):
    form = TestimonialAdminForm
    list_display = ('name', 'company', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'company', 'testimonial')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)

class AboutAdmin(admin.ModelAdmin):
    form = AboutAdminForm
    list_display = ('title', 'created_at', 'updated_at')

class FeaturedServiceAdmin(admin.ModelAdmin):
    form = FeaturedServiceAdminForm
    list_display = ('title', 'order', 'updated_at')
    list_editable = ('order',)
    fieldsets = (
        ('Conteúdo', {
            'fields': ('title', 'description', 'icon_svg', 'order')
        }),
    )

class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ('question', 'order', 'updated_at')
    list_editable = ('order',)
    fieldsets = (
        ('Conteúdo', {
            'fields': ('question', 'answer', 'order')
        }),
    )

class WorkProcessAdmin(admin.ModelAdmin):
    form = WorkProcessAdminForm
    list_display = ('title', 'order', 'updated_at')
    list_editable = ('order',)
    fieldsets = (
        ('Conteúdo', {
            'fields': ('title', 'description', 'icon', 'order')
        }),
    )

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'published', 'order')
    list_filter = ('published', 'category', 'tags')
    search_fields = ('title', 'description', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience_type', 'version', 'proficiency_level', 'order')
    list_filter = ('experience_type',)
    search_fields = ('title', 'description')
    ordering = ('order',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill_type', 'order')
    list_filter = ('skill_type',)
    search_fields = ('title', 'description')
    ordering = ('order',)

class FooterAdmin(admin.ModelAdmin):
    list_display = ('tagline', 'created_at', 'updated_at')
    search_fields = ('tagline',)
    readonly_fields = ('created_at', 'updated_at')

# Registrar os modelos
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(FeaturedService, FeaturedServiceAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(WorkProcess, WorkProcessAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Footer, FooterAdmin)
