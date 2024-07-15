from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.homepage, name='homepage'),  # URL for the homepage
    path('signup/', views.signup_view, name='signup'),  # URL for the signup page
    path('login/', views.login_view, name='login'),  # URL for the login page
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),  # URL for the patient dashboard
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),  # URL for the doctor dashboard
    path('create/', views.create_blog_post, name='create_post'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('public_posts/', views.public_posts, name='public_posts'),

]
