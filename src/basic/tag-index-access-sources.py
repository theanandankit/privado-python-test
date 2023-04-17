import datetime as dt

from pyspark.sql import functions as F
from databricks import table

METRICS = {
    'ad_spend': F.sum('ad_spend'),
    'device_id': F.sum('device_id'),
    'idfa': F.sum('idfa'),
}

class FactAdSpend():
    def fact_ad_spend(self):
        return table(METRICS)
    
    def ad_spend_perc(self):
        return table(METRICS, 100)

# var sources = cpg.call("<operator>.indexAccess").argument.isIdentifier.l
# var sinks = cpg.call.methodFullName("databricks.*").l
# sinks.reachableByFlows(sources).l