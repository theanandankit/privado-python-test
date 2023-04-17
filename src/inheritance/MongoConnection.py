from pymongo import MongoClient
from django.conf import settings


class MongoConnection(object):
    def __init__(self):
        DATABASES = settings.DATABASES
        self.client = MongoClient(
            host=[DATABASES['MONGO']['HOST']],
            username=DATABASES['MONGO']['USERNAME'],
            password=DATABASES['MONGO']['PASSWORD'],
            authSource=DATABASES['MONGO']['AUTH_DATABASE']
        )
        # self.client = MongoClient(host=[DATABASES['MONGO']['HOST']])
        self.db = self.client[DATABASES['MONGO']['DATABASE']]
        # self.collection = None

    def get_collection(self, name):
        self.collection = self.db[name]