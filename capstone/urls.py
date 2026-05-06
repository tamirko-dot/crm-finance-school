from django.urls import path
from . import views

urlpatterns = [
    path("<slug:course_slug>/submit/", views.submit_capstone, name="capstone_submit"),
    path("<int:pk>/review/", views.review_capstone, name="capstone_review"),
]
