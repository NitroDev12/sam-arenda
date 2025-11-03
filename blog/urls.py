from django.urls import path
from .views import home,skuter_qosh

urlpatterns = [
    path("",home,name="saxifa"),
    path('skuterqosh/', skuter_qosh, name='skuter_qosh'),
]