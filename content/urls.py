from django.urls import path
from content import views
from exams import views as exam_views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("<slug:course_slug>/", views.course_detail, name="course_detail"),
    path("<slug:course_slug>/request-access/", views.request_course_access, name="request_course_access"),
    path("<slug:course_slug>/modules/<slug:module_slug>/", views.module_view, name="module_view"),
    path("<slug:course_slug>/exam/", exam_views.exam_start, name="exam_start"),
    path("<slug:course_slug>/exam/<int:attempt_pk>/", exam_views.exam_question, name="exam_question"),
    path("<slug:course_slug>/exam/<int:attempt_pk>/submit/", exam_views.exam_submit, name="exam_submit"),
    path("<slug:course_slug>/exam/<int:attempt_pk>/result/", exam_views.exam_result, name="exam_result"),
]
