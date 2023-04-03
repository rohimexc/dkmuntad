from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
     path('', views.index, name='index'),
     path('tim/<str:id_dkm>/', views.tim, name='tim'),
     path('faq/', views.faq, name='faq'),
     path('profile/<str:id_dkm>/', views.profile, name='profile'),
     path('database/', views.database, name='database'),
     
     path('data-post/', views.data_post, name='data-post'),
     path('edit-post/<str:id>/', views.edit_post, name='edit-post'),
     path('hapus-post/<str:id>/', views.hapus_post, name='hapus-post'),
     
     path('data-testimoni/', views.data_testimoni, name='data-testimoni'),
     path('edit-testimoni/<str:id>/', views.edit_testimoni, name='edit-testimoni'),
     path('hapus-testimoni/<str:id>/', views.hapus_testimoni, name='hapus-testimoni'),
     
     path('data-pertanyaan/', views.data_pertanyaan, name='data-pertanyaan'),
     path('edit-pertanyaan/<str:id>/', views.edit_pertanyaan, name='edit-pertanyaan'),
     path('hapus-pertanyaan/<str:id>/', views.hapus_pertanyaan, name='hapus-pertanyaan'),
     
     path('edit/<str:id_dkm>/', views.edit, name='edit'),
     
     path('ulasan/<str:id_dkm>/', views.ulasan, name='ulasan'),
     path('refresh/', views.refresh, name='refresh'),
     path('logout', views.logoutpage, name='logout'),
]