import requests

def test_place_details_fields():
    response = requests.get("https://rahulshettyacademy.com/maps/api/place/get/json", params={
        "key": "qaclick123",
        "place_id": "65543d20c0ccd1a519dd907d500b61d3"
    })
    assert response.status_code == 200

    data = response.json()


    assert data["location"] == {
        "latitude": "-38.383494",
        "longitude": "33.427362"
    }

    assert data["accuracy"] == "50"
    assert data["name"] == "Frontline house"
    assert data["phone_number"] == "(+91) 983 893 3937"
    assert data["address"] == "29, side layout, cohen 09"
    assert data["types"] == "shoe park,shop"
    assert data["website"] == "http://google.com"
    assert data ["language"] == "French-IN"

def test_name_field_negative_check():
        response = requests.get("https://rahulshettyacademy.com/maps/api/place/get/json", params={
            "key": "qaclick123",
            "place_id": "65543d20c0ccd1a519dd907d500b61d3"
        })
        assert response.status_code == 200
        data = response.json()

        assert isinstance(data["name"], str)
        assert data["name"]
