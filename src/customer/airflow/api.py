import requests
from abcd import union_df, in_currentDay_df

class Client:
    access_token: str = None

    def post(self, uuid: str, account_id: str, endpoint: str = "results"):
        if not self.access_token:
            self.authenticate()

        settlement_in_currentDay_df = union_df.select(
            "settlementID",
            "settlement-start-date",
            "settlement-end-date",
            "deposit-date",
            "total-amount",
            "currency",
            "customer_name",
            "marketplace"
        ).filter(col("total-amount").isNotNull())

        market_place_df = in_currentDay_df.select(
            "settlementID",
            "marketplace_name"
        ).distinct()
        n_currentDay_df = in_currentDay_df.select(
            "settlementID",
            "settlement-start-date",
            "settlement-end-date",
            "deposit-date",
            "total-amount",
            "currency",
            "bank_account_id",
            "order-id",
            "customer-order-id",
            "adjustment-id",
            "shipment_id",
            "shipment-fee-type",
            "shipment-fee-amount",
            "order-fee-type",
            "order-fee-amount",
            "email-id",
            "order-item-code",
            "customer-order-item-id",
            "customer-adjustment-item-id",
            "sku",
            "quantity-purchased",
            "price-type",
            "discount-amount",
            "price-amount",
            "item-related-fee-type",
            "item-related-fee-amount",
            "misc-fee-amount",
            "other-fee-amount",
            "other-fee-reason-description",
            "promotion-id",
            "promotion-type",
            "promotion-amount",
            "direct-payment-type",
            "direct-payment-amount",
            "other-amount"
        )

        response = requests.post(
            url=f"https://{account_id}.rest.marketingcloudapis.com/data/v1/async/{uuid}/{endpoint}",
            headers={
                "Authorization": self.auth_header(),
                "Content-Type": "application/json",
            },
            body=[settlement_in_currentDay_df, n_currentDay_df]
        )
        return response
    

    # def __init__(
    #     self,
    #     submit_url: str,
    #     account_id: str,
    # ):
    #     self.account_id = account_id
    #     self.submit_url = submit_url
    #     self.auth_time = None