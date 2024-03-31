from django.contrib import admin
from django.urls import path
from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FirstPage, name='firstpage'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('registration/', views.registration_page, name='registration'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)