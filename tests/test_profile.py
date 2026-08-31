def test_profile_redirects_when_logged_out(client):
    resp = client.get("/profile")
    assert resp.status_code == 302
    assert "/login" in resp.headers["Location"]


def test_profile_ok_when_logged_in(client):
    with client.session_transaction() as sess:
        sess["user_id"] = 1
        sess["user_name"] = "Demo User"

    resp = client.get("/profile")
    assert resp.status_code == 200
    assert b"Demo User" in resp.data
    assert b"demo@spendly.com" in resp.data


def test_navbar_shows_logged_in_state(client):
    with client.session_transaction() as sess:
        sess["user_id"] = 1
        sess["user_name"] = "Demo User"

    resp = client.get("/profile")
    assert b"Log out" in resp.data
    assert b"Demo User" in resp.data
