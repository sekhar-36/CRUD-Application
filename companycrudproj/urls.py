"""
URL configuration for companycrudproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,re_path as url
from companycrudapp import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.CompanyListView.as_view(),name='home'),
    url(r'^(?P<pk>\d+)/$',views.CompanyDetailView.as_view(),name='detail'),
    url(r'^create/',views.CompanyCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.CompanyUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.CompanyDeleteView.as_view(),name='delete'),
]

#username =company
#password=Company@123