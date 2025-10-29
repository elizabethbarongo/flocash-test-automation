import requests

def test_create_order_cit(config, auth, headers):
    url = f"{config.base_url}/orders"
    payload = {
        "order": {
            "amount": 50.00,
            "currency": "KES",
            "orderId": "CIT-AUTO-123456",
            "threeDS": True,
            "recurring": {"init_recurring": True}
        },
        "merchant": {"merchantAccount": "vietnga210484@yahoo.com"},
        "payer": {
            "country": "KE",
            "firstName": "Denis",
            "lastName": "Shabiha",
            "mobile": "251948185702",
            "email": "dennis@mobirr.com"
        },
        "payOption": {"id": 145},
        "cardInfo": {
            "cardHolder": "Dennis Shabiha",
            "cardNumber": "4508750015741019",
            "expireMonth": "01",
            "expireYear": "39",
            "cvv": "100"
        },
        "billingTo": {
            "companyName": "Flocash",
            "firstName": "Denis",
            "lastName": "Shabiha",
            "country": "ZW",
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
    print("create_order_cit:", resp.status_code, resp.text)
    assert resp.status_code in (200, 201), f"create_order_cit failed: {resp.status_code} {resp.text}"
