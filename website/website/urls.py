from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.index,name='home'),
    path('history', views.history,name='history'),
    path('enrollee', views.enrollee,name='enrollee'),
    path('contact', views.contact,name='contact'),
    path('employment', views.employment,name='employment'),
    path('articles', views.articles,name='articles'),
    path('admin/', admin.site.urls),
]
