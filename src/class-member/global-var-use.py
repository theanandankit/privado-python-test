import logging
import requests
from toolbox.utils import chunks

log = logging.getLogger(name=__name__)

url = "https://app.commissionly.io/api/public/opportunity"


class CommissionlyClient:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def post_data(self, data):
        data_chunks = list(chunks(data, 2500))
        log.info("Records that have not been updated: %s" % (self.password))
        
        for chunk in data_chunks:
            r = requests.post(
                url,
                json={"isloop": True, "data": chunk},
                auth=data.password,
            )

            json_response = r.json()

            for key, value in json_response.items():
                if value.get("id") is False:
                    log.info("Records that have not been updated: %s" % (value))