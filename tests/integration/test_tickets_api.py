def test_health_does_not_require_api_key(client) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_tickets_endpoint_rejects_missing_api_key(client) -> None:
    response = client.get("/tickets")

    assert response.status_code == 401


def test_create_and_list_ticket(client, auth_headers) -> None:
    create_response = client.post(
        "/tickets",
        json={"title": "Printer on fire", "description": "Literally smoking", "priority": "high"},
        headers=auth_headers,
    )
    assert create_response.status_code == 201
    created = create_response.json()
    assert created["status"] == "open"

    list_response = client.get("/tickets", headers=auth_headers)
    titles = [ticket["title"] for ticket in list_response.json()]

    assert "Printer on fire" in titles


def test_list_tickets_filters_by_priority(client, auth_headers) -> None:
    client.post("/tickets", json={"title": "Low one", "priority": "low"}, headers=auth_headers)
    client.post("/tickets", json={"title": "High one", "priority": "high"}, headers=auth_headers)

    response = client.get("/tickets?priority=high", headers=auth_headers)
    tickets = response.json()

    assert len(tickets) == 1
    assert tickets[0]["title"] == "High one"


def test_close_ticket_marks_it_closed(client, auth_headers) -> None:
    created = client.post(
        "/tickets", json={"title": "Needs closing"}, headers=auth_headers
    ).json()

    response = client.post(f"/tickets/{created['id']}/close", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["status"] == "closed"


def test_close_unknown_ticket_returns_404(client, auth_headers) -> None:
    response = client.post("/tickets/999/close", headers=auth_headers)

    assert response.status_code == 404


def test_stats_reports_total(client, auth_headers) -> None:
    client.post("/tickets", json={"title": "One"}, headers=auth_headers)
    client.post("/tickets", json={"title": "Two"}, headers=auth_headers)

    response = client.get("/stats", headers=auth_headers)
    stats = response.json()

    assert stats["total"] == 2


def test_create_ticket_without_assignee_defaults_to_null(client, auth_headers) -> None:
    response = client.post("/tickets", json={"title": "No owner yet"}, headers=auth_headers)

    assert response.json()["assignee"] is None


def test_create_ticket_with_assignee(client, auth_headers) -> None:
    response = client.post(
        "/tickets", json={"title": "Has owner", "assignee": "Ana"}, headers=auth_headers
    )

    assert response.json()["assignee"] == "Ana"


def test_assign_ticket_updates_assignee(client, auth_headers) -> None:
    created = client.post("/tickets", json={"title": "Needs owner"}, headers=auth_headers).json()

    response = client.post(
        f"/tickets/{created['id']}/assign", json={"assignee": "Bruno"}, headers=auth_headers
    )

    assert response.status_code == 200
    assert response.json()["assignee"] == "Bruno"


def test_assign_unknown_ticket_returns_404(client, auth_headers) -> None:
    response = client.post(
        "/tickets/999/assign", json={"assignee": "Ana"}, headers=auth_headers
    )

    assert response.status_code == 404
