import sqlalchemy
from datadog import statsd

def generate_vehicle_row(row, vehicle_type):
    row_vehicle = dict()
    row_vehicle['VEHICLE_REGISTRATION_NUMBER'] = vehicle_type["VEHICLE_REGISTRATION_NUMBER"]

    statsd.increment(row_vehicle)



    # if row.get('POLICY_TYPE') == 'B2C':
        # if row['VRG'] or row['VEHICLE_MAKE'] or row['VEHICLE_MODEL'] or row['VEHICLE_COLOUR']:
        # row_vehicle = dict((k, row[k]) for k in ('POLICY_NUMBER', 'VRG', 'VEHICLE_MAKE',
        #                                             'VEHICLE_MODEL', 'VEHICLE_COLOUR'))

# class ProductionConfig(Config):
#     SENTRY_DSN = (
#         "https://8b9a3fb13bae477ca078d11d29ae43e9@o115453.ingest.sentry.io/5714434"
#     )
#     PUBSUB_HOST = "pubsub:8080"
#     AWS_S3_ENDPOINT_URL: Optional[str] = None
#     BULK_LOAD_BUCKET: str = os.getenv("BULK_LOAD_BUCKET")
#     NEPTUNE_BASE_URL: str = os.getenv("NEPTUNE_BASE_URL")

# def connect_db(args):
#     dbName = "postgresql"
#     db = sqlalchemy.create_engine(
#         f"postgresql+psycopg2://",
#         f"{dbName}+psycopg2://",
#         pool_pre_ping=True,
#         client_encoding="utf8",
#         connect_args=args
#     )
#     conn = db.connect()


# lemonade_python_common/utils/secret.py:<module>.SecretProvider.<init>.get_secret.<returnValue>

# (?i)(request|retry|retriable|aiohttp|treq|grequests|urllib|http|uplink|httoop|flask_restful|tornado.httpclient|pycurl|bs4|.*(HttpClient)).*


# from requests import ConnectTimeout, ReadTimeout
# try:
#     r = self._get(headers, path)
# except (ConnectionError, ConnectTimeout, ReadTimeout) as ex:
#     log.exception(
#         f"failed to get {path} from car service | error={str(ex)[:500]}"
#     )
#     return ApiResponse(response={}, success=False, status_code=-1)

# Call(
#     id = 30L,
#     argumentIndex = 1,
#     argumentName = None,
#     code = "f\"{dbName}+psycopg2://\"",
#     columnNumber = Some(value = 8),
#     dispatchType = "STATIC_DISPATCH",
#     dynamicTypeHintFullName = ArraySeq(),
#     lineNumber = Some(value = 6),
#     methodFullName = "<operator>.formatString",
#     name = "<operator>.formatString",
#     order = 2,
#     signature = "",
#     typeFullName = "ANY"
# ),