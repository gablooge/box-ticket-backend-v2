import pytest
from django.urls import reverse
from django.conf import settings
from jwt import decode


def test_login_superuser_valid_with_email(client, django_db_setup):
    user, staff_user, superuser = django_db_setup
    uri = reverse("token_login")
    resp = client.post(
        uri,
        data={"email": superuser.email, "password": settings.TEST_PASSWORD},
        content_type="application/json",
    )

    assert (
        decode(resp.json()["access"], settings.JWT_SECRET_KEY, algorithms=["HS256"])[
            "user_id"
        ]
        == superuser.id
    )
    assert resp.status_code == 200


def test_login_user_valid(client, django_db_setup):
    user, staff_user, superuser = django_db_setup
    uri = reverse("token_login")
    resp = client.post(
        uri,
        data={"email": user.email, "password": settings.TEST_PASSWORD},
        content_type="application/json",
    )

    assert (
        decode(resp.json()["access"], settings.JWT_SECRET_KEY, algorithms=["HS256"])[
            "user_id"
        ]
        == user.id
    )
    assert resp.status_code == 200


def test_login_superuser_empty_payload(client, django_db_setup):
    user, staff_user, superuser = django_db_setup
    uri = reverse("token_login")
    resp = client.post(uri, data={}, content_type="application/json")

    assert resp.json()["email"][0] == "This field is required."
    assert resp.status_code == 400


@pytest.mark.parametrize(
    "client, email, password, field, error, django_db_setup",
    [
        # blank password
        ("", "test_superuser", "", "password", "This field may not be blank.", ""),
        # blank email
        (
            "",
            "",
            settings.TEST_PASSWORD,
            "email",
            "This field may not be blank.",
            "",
        ),
        # null password
        ("", "test_superuser", None, "password", "This field may not be null.", ""),
        # null email
        (
            "",
            None,
            settings.TEST_PASSWORD,
            "email",
            "This field may not be null.",
            "",
        ),
    ],
    indirect=["client", "django_db_setup"],
)
def test_login_superuser_invalid_payload(
    client, email, password, field, error, django_db_setup
):
    user, staff_user, superuser = django_db_setup
    uri = reverse("token_login")
    resp = client.post(
        uri,
        data={"email": email, "password": password},
        content_type="application/json",
    )

    assert resp.json()[field][0] == error
    assert resp.status_code == 400


@pytest.mark.parametrize(
    "client, email, password, django_db_setup",
    [
        ("", "wrong", "wrong", ""),  # wrong email and password
        ("", "wrong", settings.TEST_PASSWORD, ""),  # wrong password
    ],
    indirect=["client", "django_db_setup"],
)
def test_login_superuser_invalid(client, email, password, django_db_setup):
    user, staff_user, superuser = django_db_setup
    uri = reverse("token_login")
    resp = client.post(
        uri,
        data={"email": email, "password": password},
        content_type="application/json",
    )

    assert resp.json()["detail"] == "No active account found with the given credentials"
    assert resp.status_code == 401


def test_login_get_not_allowed(client, django_db_setup):
    user, staff_user, superuser = django_db_setup
    uri = reverse("token_login")
    resp = client.get(uri, content_type="application/json")

    assert resp.json()["detail"] == 'Method "GET" not allowed.'
    assert resp.status_code == 405
