from django.core.management.base import BaseCommand
from accounts.models import User, UserRole

TEST_USERS = [
    {
        "email": "trainee@test.local",
        "username": "trainee_test",
        "full_name_he": "חניך לדוגמה",
        "full_name_en": "Test Trainee",
        "role": UserRole.TRAINEE,
        "password": "Test1234!",
    },
    {
        "email": "manager@test.local",
        "username": "manager_test",
        "full_name_he": "מנהל לקוחות לדוגמה",
        "full_name_en": "Test Manager",
        "role": UserRole.CUSTOMER_MANAGER,
        "password": "Test1234!",
    },
    {
        "email": "ceo@test.local",
        "username": "ceo_test",
        "full_name_he": "מנכ\"ל לדוגמה",
        "full_name_en": "Test CEO",
        "role": UserRole.CEO,
        "password": "Test1234!",
    },
    {
        "email": "sysadmin@test.local",
        "username": "admin_test",
        "full_name_he": "מנהל מערכת לדוגמה",
        "full_name_en": "Test Admin",
        "role": UserRole.ADMIN,
        "is_staff": True,
        "password": "Test1234!",
    },
]


class Command(BaseCommand):
    help = "Create one test user per role (dev only — never run in production)"

    def handle(self, *args, **options):
        for u in TEST_USERS:
            password = u.pop("password")
            is_staff = u.pop("is_staff", False)
            user, created = User.objects.get_or_create(
                email=u["email"],
                defaults={**u, "is_staff": is_staff},
            )
            if created:
                user.set_password(password)
                user.save()
                self.stdout.write(f"  [NEW] {u['email']} ({u['role']})")
            else:
                self.stdout.write(f"  [exists] {u['email']}")
        self.stdout.write(self.style.SUCCESS("Test users ready. Password for all: Test1234!"))
