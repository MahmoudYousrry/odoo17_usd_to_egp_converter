import requests

def get_usd_to_egp_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get("result") == "success":
            return data["rates"].get("EGP")
        return None
    except Exception:
        return None
