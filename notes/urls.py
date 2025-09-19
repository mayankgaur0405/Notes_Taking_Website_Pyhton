from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/create/', views.note_create, name='note_create'),
    path('note/<int:pk>/update/', views.note_update, name='note_update'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
]
