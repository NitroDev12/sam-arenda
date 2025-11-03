from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),           # ← bu endi asosiy sahifa
    path('skuterqosh/', views.skuter_qosh, name='skuter_qosh'),
]
