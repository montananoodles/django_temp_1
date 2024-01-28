"""
appppppppppp
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('getNotes/', views.getNotes)
]

