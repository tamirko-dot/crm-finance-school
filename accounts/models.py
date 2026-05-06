from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserRole(models.TextChoices):
    TRAINEE = "trainee", "חניך"
    CUSTOMER_MANAGER = "customer_manager", "מנהל לקוחות"
    ADMIN = "admin", "מנהל מערכת"
    CEO = "ceo", "מנכ\"ל"


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str | None = None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", UserRole.ADMIN)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    full_name_he = models.CharField(max_length=200, blank=True)
    full_name_en = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.TRAINEE)
    supabase_user_id = models.CharField(max_length=255, blank=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "משתמש"
        verbose_name_plural = "משתמשים"

    def __str__(self) -> str:
        return self.full_name_he or self.email

    @property
    def display_name(self) -> str:
        return self.full_name_he or self.username
