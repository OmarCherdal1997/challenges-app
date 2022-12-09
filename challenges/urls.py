from . import views
from django.urls import path



urlpatterns = [
    path("",views.index), #challenges
    path('<int:month>',views.monthly_challenges_numbers),
    path('<str:month>',views.monthly_challenges, name="monthly_challenges_path")
]