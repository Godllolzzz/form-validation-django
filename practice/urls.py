from django.urls import path
from .  import views

urlpatterns = [
    # path("", views.practice_view, name = 'first_View')
    path("", views.PracticeView.as_view(), name = 'first_View')
]
