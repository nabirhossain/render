<<<<<<< HEAD
=======
<<<<<<< HEAD
"""render_upload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
>>>>>>> 3c31ee2 (first commit)
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.render_upload, name='render_upload'),


=======
    path('admin/', admin.site.urls),
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_upload, name='render_upload'),


>>>>>>> 282f5eb (render upload)
>>>>>>> 3c31ee2 (first commit)
]
