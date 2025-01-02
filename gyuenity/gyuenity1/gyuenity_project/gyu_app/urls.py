from django.urls import path, include
from gyu_app import views
from .views import  set_payment_session , check_session

app_name = "gyu_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('course/', views.course, name='course'),
     path('faqs/', views.faqs_view, name='faqs'),
    path('login', views.login, name='login'),  
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profil/', views.profil, name='profil'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('courses', views.courses, name='courses'),
    path('class1', views.class1_view, name='class1'), 
    path('pembayaran', views.pembayaran, name='pembayaran'),
    path('check_payment_status/', views.check_payment_status, name='check_payment_status'),
    path('set-session/', set_payment_session, name='set_payment_session'),
    path('check-session/', check_session, name='check_session'),
    path('materi1class1', views.materi1class1, name='materi1class1'),
    path('quizm1class1', views.quizm1class1, name='quizm1class1'),
    path('quizresultm1c1/', views.quizresultm1c1, name='quizresultm1c1'),
    path('progressbelajar', views.progressbelajar, name='progressbelajar'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('hasilquiz', views.hasilquiz, name='hasilquiz'),
]
