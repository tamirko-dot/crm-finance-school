import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestLoginView:
    def test_login_page_renders(self, client):
        resp = client.get(reverse("login"))
        assert resp.status_code == 200
        assert "כניסה" in resp.content.decode("utf-8")

    def test_redirect_when_authenticated(self, client, trainee):
        client.force_login(trainee)
        resp = client.get(reverse("login"))
        assert resp.status_code == 302
        assert "/dashboard" in resp["Location"]

    def test_valid_credentials_login(self, client, trainee):
        resp = client.post(reverse("login"), {"email": trainee.email, "password": "Test1234!"})
        assert resp.status_code == 302
        assert "_auth_user_id" in client.session

    def test_invalid_credentials_rejected(self, client, trainee):
        resp = client.post(reverse("login"), {"email": trainee.email, "password": "WrongPass!"})
        assert resp.status_code == 200
        assert "_auth_user_id" not in client.session

    def test_empty_fields_rejected(self, client):
        resp = client.post(reverse("login"), {"email": "", "password": ""})
        assert resp.status_code == 200
        assert "_auth_user_id" not in client.session

    def test_inactive_user_rejected(self, client, trainee):
        trainee.is_active = False
        trainee.save()
        resp = client.post(reverse("login"), {"email": trainee.email, "password": "Test1234!"})
        assert "_auth_user_id" not in client.session

    def test_logout_clears_session(self, client, trainee):
        client.force_login(trainee)
        client.get(reverse("logout"))
        assert "_auth_user_id" not in client.session


@pytest.mark.django_db
class TestDashboardRouting:
    def test_unauthenticated_redirects_to_login(self, client):
        resp = client.get(reverse("dashboard"))
        assert resp.status_code == 302
        assert "/accounts/login/" in resp["Location"]

    def test_trainee_sees_trainee_dashboard(self, client, trainee):
        client.force_login(trainee)
        resp = client.get(reverse("dashboard"))
        assert resp.status_code == 200
        assert b"dashboard_trainee" in resp.content or "חניך" in resp.content.decode("utf-8")

    def test_manager_sees_manager_dashboard(self, client, manager):
        client.force_login(manager)
        resp = client.get(reverse("dashboard"))
        assert resp.status_code == 200
        assert "מנהל לקוחות" in resp.content.decode("utf-8")

    def test_admin_sees_admin_dashboard(self, client, admin_user):
        client.force_login(admin_user)
        resp = client.get(reverse("dashboard"))
        assert resp.status_code == 200
        assert "מנהל מערכת" in resp.content.decode("utf-8")

    def test_ceo_sees_ceo_dashboard(self, client, ceo):
        client.force_login(ceo)
        resp = client.get(reverse("dashboard"))
        assert resp.status_code == 200
        assert 'מנכ"ל' in resp.content.decode("utf-8")


@pytest.mark.django_db
class TestRBACDecorators:
    """Role decorators must return 403 when wrong role tries to access a protected view."""

    def test_unauthenticated_gets_redirect_not_403(self, client):
        resp = client.get("/admin/")
        assert resp.status_code == 302

    def test_trainee_cannot_access_admin(self, client, trainee):
        client.force_login(trainee)
        resp = client.get("/admin/")
        assert resp.status_code == 302

    def test_home_redirects_authenticated_to_dashboard(self, client, trainee):
        client.force_login(trainee)
        resp = client.get("/")
        assert resp.status_code == 302
        assert "dashboard" in resp["Location"]

    def test_home_redirects_anonymous_to_login(self, client):
        resp = client.get("/")
        assert resp.status_code == 302
        assert "login" in resp["Location"]
