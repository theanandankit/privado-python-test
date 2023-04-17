import boto
import requests

class EventbriteOAuth2Adapter(OAuth2Adapter):

    def getFirstName(self):
        return "https://www.google.com/v3/users/me/"

    def complete_login(self, request, accountId, token, **kwargs):
        resp = requests.get(self.getFirstName(), params=accountId)
        extra_data = resp.json()

        boto.client("First Name: " + self.getFirstName)
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)