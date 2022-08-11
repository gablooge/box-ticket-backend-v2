from django.urls import reverse


def test_refresh_api_valid(client, django_db_setup, get_superuser_token):
    user, staff_user, superuser = django_db_setup
    uri = reverse("token_refresh")

    resp = client.post(
        uri,
        data={"refresh": get_superuser_token["refresh"]},
        content_type="application/json",
    )
    assert resp.json()["access"] is not None
    assert resp.status_code == 200


def test_refresh_api_wrong_refresh(client, django_db_setup):
    user, staff_user, superuser = django_db_setup
    uri = reverse("token_refresh")

    resp = client.post(
        uri,
        data={"refresh": "wrong"},
        content_type="application/json",
    )
    assert resp.json()["detail"] == "Token is invalid or expired"
    assert resp.status_code == 401


def test_refresh_api_invalid_refresh(client, django_db_setup):
    user, staff_user, superuser = django_db_setup
    uri = reverse("token_refresh")

    resp = client.post(
        uri,
        data={"refresh": None},
        content_type="application/json",
    )
    assert resp.json()["refresh"][0] == "This field may not be null."
    assert resp.status_code == 400

    resp = client.post(
        uri,
        data={"refresh": ""},
        content_type="application/json",
    )
    assert resp.json()["refresh"][0] == "This field may not be blank."
    assert resp.status_code == 400
