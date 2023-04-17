"""Views for Eventbrite API v3."""
import requests

class EventbriteOAuth2Adapter():
    accountId = 'https://www.eventbriteapi.com/v3/users/me/'

    def complete_login(self, request, app, token, **kwargs):
        res = requests.get(self.accountId, token)
        return res
