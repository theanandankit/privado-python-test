import requests

class TestClient:
    def get_event_data(self, accountId):
        payload = { "test": accountId }
        r = requests.get(
            "https://www.apple.com/v3/users/me/",
            params=payload
        )

        if r.status_code == 200:
            return r.status_code, "Extract complete"
        else:
            return r.status_code, r.text