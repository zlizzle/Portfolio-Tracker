from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_portfolio_value_endpoint():
    test_asset = {
        "symbol": "BTC",
        "quantity": 2.0,
        "average_price": 20000.0
    }
    client.post("/assets/", json=test_asset)

    response = client.get("/assets/portfolio/value")
    assert response.status_code == 200

    data = response.json()

    # Check the top-level keys
    assert "total_portfolio_value_usd" in data
    assert "total_portfolio_pnl_usd" in data
    assert "assets" in data
    assert isinstance(data["assets"], list)

    # Check at least one asset entry exists
    assert any(asset["symbol"] == "BTC" for asset in data["assets"])