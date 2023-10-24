from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('login/', views.signin, name='login'),
    path('accounts/', include('allauth.urls')),
    path('report/', views.report, name='report'),
    path('get_respuesta/', views.get_respuesta, name='get_respuesta'),
]