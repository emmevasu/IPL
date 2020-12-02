from django.contrib import admin
from django.urls import path
from .views import IplTopScorer

urlpatterns = [
    path('<num>',IplTopScorer),
    # path('home/',IplTopScorer),
    # path('img',getimage),
    # path('plot',ima),
]
