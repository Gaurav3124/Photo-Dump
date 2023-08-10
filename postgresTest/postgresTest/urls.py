"""GameZoneApp URL Configuration

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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name="HomePage"),
    path('Insert',views.insertphoto,name="insertphoto"),
    path('showphoto',views.showphoto,name="showphoto"),
    path('Edit/<int:id>',views.editphoto,name="editphoto"),
    path('Update/<int:id>',views.updatephoto,name="updatephoto"),
    path('Delete/<int:id>',views.deletephoto,name="deletephoto"),
    path('sortasc',views.sortasc,name="sortasc"),
    path('sortdesc',views.sortdesc,name="sortdesc"),
    path('runquery',views.runquery,name="runquery"),
]