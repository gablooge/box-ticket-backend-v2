from django.urls import reverse


def test_logout_user_valid(client, django_db_setup, get_superuser_token):
    user, staff_user, superuser = django_db_setup
    uri = reverse("auth_logout")
    client.defaults["HTTP_AUTHORIZATION"] = "Bearer {}".format(
        get_superuser_token["access"]
    )

    resp = client.post(
        uri,
        data={"refresh_token": get_superuser_token["refresh"]},
        content_type="application/json",
    )
    assert resp.json()["message"] == "Logout successfully."
    assert resp.json()["success"] is True
    assert resp.status_code == 200


def test_logout_user_invalid(client, django_db_setup, get_superuser_token):
    user, staff_user, superuser = django_db_setup
    uri = reverse("auth_logout")
    client.defaults["HTTP_AUTHORIZATION"] = "Bearer {}".format(
        get_superuser_token["access"]
    )

    resp = client.post(
        uri,
        data={"refresh_token": "wrong"},
        content_type="application/json",
    )
    assert resp.json()["message"] == "Refresh Token not valid"
    assert resp.json()["success"] is False
    assert resp.status_code == 400


def test_logout_superuser_empty_payload(client, django_db_setup):
    user, staff_user, superuser = django_db_setup
    uri = reverse("auth_logout")
    resp = client.post(uri, data={}, content_type="application/json")

    assert resp.json()["detail"] == "Authentication credentials were not provided."
    assert resp.status_code == 401
