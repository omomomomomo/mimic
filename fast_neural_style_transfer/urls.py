"""fast_neural_style_transfer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

import style_transfer.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('style_transfer.urls')),
    # path('stylize/', style_transfer.views.apply_style_transfer),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', style_transfer.views.home),
#     path('stylize/', style_transfer.views.apply_style_transfer)
# ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
