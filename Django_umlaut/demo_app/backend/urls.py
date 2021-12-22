from django.urls import path
from . import views

urlpatterns = [
    path('line_a', views.line_a, name='line-a'),
    path('line_b', views.line_b, name='line-b'),
]