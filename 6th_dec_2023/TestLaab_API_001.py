# Python testing freamework -> Unit test, Nose, Pytest(TestNG)
# Every Test will start from test_name.py
# pytest -h

# how to do create booking by using the pyTest -> allure

# Create a booking - POST -
# URL
# Headers
# BODY (Payload) - Json
# Token ? / Auth
# verify the booking id

import pytest
import requests


@pytest.mark.positive
def test_create_booking_positive():
    print("create Booking testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=json_payload)

    # Assertions

    assert response.status_code == 200

    # get the response body and verify the json Booking ID is not None
    data = response.json()
    booking_id = data["booking_id"]
    print(booking_id)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Amit", "Failed Message - incorrect FirstName"


@pytest.mark.negative
def test_create_booking_positive():
    print("create Booking testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=json_payload)

    # Assertions

    assert response.status_code == 500
