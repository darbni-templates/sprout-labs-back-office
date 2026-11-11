def test_pages_need_a_login(client):
    response = client.get("/orders")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


def test_a_wrong_password_is_refused(client):
    response = client.post("/login", data={"username": "khalid", "password": "nope"})
    assert response.status_code == 401
    assert "Wrong username or password" in response.text


def test_the_dashboard_shows_the_numbers(manager):
    text = manager.get("/").text
    assert "Signed in as Khalid Mansoor" in text
    assert "Total sales: 215.850 BHD" in text


def test_the_order_list_shows_orders(manager):
    assert "LP-1008" in manager.get("/orders").text


def test_an_order_page(manager):
    text = manager.get("/orders/3").text
    assert "Order LP-1003" in text and "Noor Hasan" in text and "18.150 BHD" in text


def test_an_unknown_order_is_404(manager):
    assert manager.get("/orders/999").status_code == 404


def test_archiving_hides_an_order(manager):
    manager.post("/orders/8/delete")
    assert "LP-1008" not in manager.get("/orders").text


def test_the_invoice_splits_out_the_vat(manager):
    text = manager.get("/orders/3/invoice").text
    assert "16.500 BHD" in text and "1.650 BHD" in text


def test_the_customers_page(manager):
    assert "41.650 BHD" in manager.get("/customers").text  # Mariam's three orders


def test_changing_the_stock(manager):
    manager.post("/stock/8", data={"stock": "20", "price_fils": "12900"})
    assert "20 in stock" in manager.get("/stock").text


def test_stock_must_be_a_number(manager):
    response = manager.post("/stock/8", data={"stock": "lots", "price_fils": "12900"})
    assert response.status_code == 400


def test_adding_a_supplier(manager):
    manager.post("/suppliers", data={"name": "Sitra Garden Centre", "email": "a@sitra.bh"})
    assert "Sitra Garden Centre" in manager.get("/suppliers").text


def test_a_supplier_needs_a_name(manager):
    assert manager.post("/suppliers", data={"name": " "}).status_code == 400


def test_the_complaints_page(manager):
    text = manager.get("/complaints").text
    assert "My Monstera arrived with two broken leaves." in text
