from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('new_journal/', views.journal_view, name='new_journal'),
    path('view_journal/<int:pk>/', views.journal_detail, name='journal_detail'),
    path('edit_journal/<int:pk>/', views.journal_edit, name='journal_edit'),
    path('delete_journal/<int:pk>/', views.journal_delete, name='journal_delete'),
]
