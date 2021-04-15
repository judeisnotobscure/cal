"""fcf2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path, include
from instruments import views as vi
from register import views as vr
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^add/', vi.form_name_view,name='form_name'),
    re_path(r'^$', vi.search),#Search.as_view()),
    re_path(r'^search/$', vi.search),#Search.as_view()),
    path('update/<str:slug>/', vi.InstrumentDetailView.as_view(), name='update_detail'),#update for recieve shipment
    path('recieve/', vi.recieve_shipment), #recieve shipment,
    path('', include("django.contrib.auth.urls")), # Login, logout, change password
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


