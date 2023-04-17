import logging
tmp = logging.getLogger(__name__)

class AccountDetailsFetcherUtility:
    def getAccountDetails(cls, accountId):
        try:
            tmp.debug(f"Try Block covered : {accountId}")
            return None
        except Exception as e:
            tmp.error(f"Exception block covered: {accountId}")
            return None