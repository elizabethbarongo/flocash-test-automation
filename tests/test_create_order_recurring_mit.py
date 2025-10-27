import requests

def test_create_order_recurring_mit(config, auth, headers):
    url = f"{config.base_url}/orders"
    payload = {
        "order": {
            "amount": 50.00,
            "currency": "KES",
            "orderId": "MIT-AUTO-123456",
            "recurring": {"recurring": True, "original_txn": "T38935040627003"},
            "threeDS": False
        },
        "merchant": {"merchantAccount": "vietnga210484@yahoo.com"},
        "payer": {
            "country": "KE",
            "firstName": "Shabiha",
            "lastName": "Dennis",
            "mobile": "+251948185702",
            "email": "dennis@mobirr.com"
        },
        "payOption": {"id": 145},
        "cardInfo": {
            "algorithm": "TOKEN",
            "token": "50749898369453383429"
        },
        "billingTo": {
            "companyName": "Flocash",
            "firstName": "Dennis",
            "lastName": "Shabiha",
            "country": "VN",
            "postcode": "100000",
            "city": "Hanoi",
            "stateProvince": "Long Bien",
            "stateProvinceCode": "HN",
            "address1": "2B,alley 14, lane 219",
            "email": "dennis@mobirr.com",
            "phoneNumber": "+84986518056"
        }
    }

    resp = requests.post(url, json=payload, headers=headers, auth=auth, timeout=config.timeout)
    print("create_order_recurring_mit:", resp.status_code, resp.text)
    assert resp.status_code in (200, 201), f"create_order_recurring_mit failed: {resp.status_code} {resp.text}"
