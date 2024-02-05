from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Test data

data_test_conversion_1 = {
    "number": 1000,
    "unit": "g"
}

data_test_conversion_2 = {
    "number": 1,
    "unit": "kg"
}

data_test_together = {
    "entry_data_1": data_test_conversion_1,
    "entry_data_2": data_test_conversion_2,
}


def test_read_item():
    response = client.get("/convert")
    assert response.status_code == 200
    assert response.json() == "Welcome to the home page of the API"


# Test the conversion of a number from g to kg
def test_convert_units():
    response = client.post("/convert/weight", json=data_test_conversion_1, params={
        "unit_target": "kg"
    })

    assert response.status_code == 200
    assert response.json() == {
        "number": "1.00000",
        "unit": "kg"
    }


# Test the addition of two numbers with different units of measurement
def test_add_units():
    response = client.post(
        "/convert/weight/add",
        json=data_test_together,)

    assert response.status_code == 200
    assert response.json() == [
        {
            "number": "2000.00000",
            "unit": "g"
        },
        {
            "number": "2.00000",
            "unit": "kg"
        }]


def test_subtract_units():
    response = client.post(
        "/convert/weight/subtract",
        json=data_test_together,)

    print(data_test_together)

    assert response.status_code == 200
    assert response.json() == [
        {
            "number": "0",
            "unit": "g"
        },
        {
            "number": "0",
            "unit": "kg"
        }]
