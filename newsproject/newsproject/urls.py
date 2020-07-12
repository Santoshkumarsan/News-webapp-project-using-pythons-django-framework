"""newspro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from newsapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.news_home),
    url(r'^home/', views.news_2ndhome),
    url(r'^signuppage/', views.signupsystem),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/', views.handlelogout),
    url(r'^firstnews/', views.firstnews),
    url(r'^secondnews/', views.secondnews),
    url(r'^thirdnews/', views.thirdnews),
    url(r'^fourthnews/', views.fourthnews),
    url(r'^fivthnews/', views.fifthnews),
    url(r'^sixthnews/', views.sixthnews),
    url(r'^seventhnews/', views.seventhnews),
    url(r'^eightthnews/', views.eightthnews),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
