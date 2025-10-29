import requests

def test_get_card_token(config, auth, headers):
    trace_number = "T38935040627003"  
    url = f"{config.base_url}/orders/{trace_number}"
    resp = requests.get(url, headers=headers, auth=auth, timeout=config.timeout)
    print("get_card_token:", resp.status_code, resp.text)
    assert resp.status_code == 200, f"get_card_token failed: {resp.status_code} {resp.text}"
