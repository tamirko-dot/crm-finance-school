"""
Dev helper: open Course 1 for the test trainee so Phase 4 flow can be verified.
Safe to run multiple times.
"""
from django.core.management.base import BaseCommand
from accounts.models import User
from content.models import Course
from enrollment.models import CourseEnrollment, EnrollmentStatus


class Command(BaseCommand):
    help = "Open Course 1 for trainee@test.local (dev verification only)"

    def handle(self, *args, **options):
        try:
            trainee = User.objects.get(email="trainee@test.local")
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("trainee@test.local not found — run create_test_users first"))
            return

        try:
            manager = User.objects.get(email="manager@test.local")
        except User.DoesNotExist:
            manager = trainee

        course = Course.objects.get(slug="c01-re-finance-basics")

        enrollment, created = CourseEnrollment.objects.get_or_create(
            user=trainee, course=course,
            defaults={"status": EnrollmentStatus.LOCKED}
        )

        if enrollment.status == EnrollmentStatus.LOCKED:
            enrollment.request_unlock()
            enrollment.save()
            enrollment.approve_unlock(approved_by=manager)
            enrollment.save()
            self.stdout.write(self.style.SUCCESS(f"Opened {course.slug} for {trainee.email}"))
        else:
            self.stdout.write(f"Enrollment already at status={enrollment.status} — no change")
