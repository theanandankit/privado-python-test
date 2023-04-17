from commons.db_redis import RedisDB

class BaseHubspotAPI:
    def __init__(self, **kwargs) -> None:
        self.redis_db = kwargs.get("redis_db", RedisDB())

    def _set_hs_until(self, hs_until: int) -> None:
        key = f"hs_live_{self.api_type}_latest_hs_until"
        if self.api_type in (
            "email_event",
            "deal",
            "deal_with_history",
            "company",
            "company_with_history",
        ):
            hs_until = int(hs_until) + 1  # add 1 millisecond to avoid duplicates
        self.redis_db.set(key=key, val=str(hs_until))

