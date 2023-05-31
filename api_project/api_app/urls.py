from django.urls import path
from . import views

urlpatterns = [
        # path('api', app_view.as_view(), name='app_view'),
        path('', views.getData),
        path('api/', views.getData),
        path('add/', views.addItem),
]
