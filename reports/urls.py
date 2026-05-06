from django.urls import path
from . import views

urlpatterns = [
    path("", views.group_report, name="group_report"),
    path("trainees/", views.trainees_list, name="trainees_list"),
    path("trainees/<int:pk>/", views.trainee_detail, name="trainee_detail"),
    path("unlock-requests/", views.unlock_requests, name="unlock_requests"),
    path("unlock-requests/<int:pk>/approve/", views.approve_request, name="approve_request"),
    path("unlock-requests/<int:pk>/deny/", views.deny_request, name="deny_request"),
    path("capstone/", views.capstone_inbox, name="capstone_inbox"),
    path("confidence/", views.confidence_map, name="confidence_map"),
]
