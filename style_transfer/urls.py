from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# import style_transfer.views

urlpatterns = [
    # path('', style_transfer.views.home),
    path('', views.home, name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('stylize/', views.apply_style_transfer),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
