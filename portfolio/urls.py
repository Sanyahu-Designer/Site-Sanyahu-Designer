from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
    path('projetos/', views.ProjectListView.as_view(), name='projects'),
    path('projetos/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('servicos/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('contato/', views.contact, name='contact'),
]
