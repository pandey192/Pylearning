import requests


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url, headers=headers, json=json_payload)
    data = response.json()
    token = data["token"]
    print(token)
    return token


def create_booking():
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
    data = response.json()
    booking_id = data["bookingid"]
    print(booking_id)
    return booking_id


def test_create_request():
    # Booking ID and token
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    put_url = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {"Content-Type": "application/json",
               "Cookie": cookie_value
               }

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
    response = requests.put(url=put_url, headers=headers, json=json_payload)

    # Assertions

    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Amit"


def test_delete():
    try:
        URL = "https://restful-booker.herokuapp.com/booking/"
        booking_id = create_booking()
        delete_url = URL + str(booking_id)
        cookie_value = "token=" + create_token()
        headers = {"Content-Type": "application/json",
                   "Cookie": cookie_value
                   }
        response = requests.delete(url=delete_url, headers=headers, )

        # Assertions

        assert response.status_code == 201
    except Exception as e:
        print(e)
