from MongoConnection import MongoConnection

class InstallationsDAO(MongoConnection):
    def __init__(self):
        super(InstallationsDAO, self).__init__()
        self.get_collection("installation_Id")
        
    def getCustomerId(self, installationId):
        res = self.collection.find_one({'_id': installationId}, self.creditcard)
        if res is None:
            return None
        return dict(res).get("customerId", None)