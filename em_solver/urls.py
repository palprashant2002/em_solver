"""em_solver URL Configuration

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
from django.urls import path
from . import views
<<<<<<< HEAD
from engg_maths import views as view_math

=======
from engg_maths import views as view_mh
>>>>>>> 688c50e2603e8b02c023b25185b8db9222434a10
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('math/', views.math, name='math'),
    path('dstl/', views.dstl, name='dstl'),
    path('test/', views.test),
<<<<<<< HEAD
    
=======
    path('inp',view_mh.fetchfunc),
>>>>>>> 688c50e2603e8b02c023b25185b8db9222434a10

]
