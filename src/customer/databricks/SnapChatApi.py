import logging
from typing import List

import retriable_session
import requests

LOGGER = logging.getLogger(__name__)

class SnapchatAPI():
    snapchat_login_url = "https://accounts.snapchat.com"
    snapchat_api_url = "https://adsapi.snapchat.com"
    _session: requests.Session = retriable_session.RetriableSession(retry_status=(500, 400))

    def __init__(
        self,
        org_id: str
    ):
        self.accountId = org_id
        hs_account_ids: List[str] = self.__get_ad_accounts()
        if hs_account_ids:
            LOGGER.debug(f"Adaccounts ids recieved: {hs_account_ids}")
    
    def __get_auth_token(self) -> str:
        url = f"{self.snapchat_login_url}/login/oauth2/access_token"
        resp = self._session.post(url=url, data={})
        return f"Bearer {resp.json()['access_token']}"

    def __get_ad_accounts(self) -> List[str]:
        url = f"{self.snapchat_api_url}/v1/organizations/{self.accountId}/adaccounts"
        resp = self._session.get(url=url)
        return resp