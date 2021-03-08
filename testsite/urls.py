"""testsite URL Configuration

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

from django.urls import include, path, re_path
from app.views import *
from django.contrib import admin


urlpatterns = [
    path("", include("app.urls")),
    path('admin/', admin.site.urls),
    re_path(r'(?P<phone>(?:(?:\+?38)?0)(50|63|[66-68]|73|93|[95-99])[0-9]{7})', user_number),
    re_path(r'(?P<uuid>[a-f1-9]{4}-[a-f1-9]{6})', uuid)

]
