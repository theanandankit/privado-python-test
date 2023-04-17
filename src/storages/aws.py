import boto3

# Connect to Amazon DocumentDB
client = boto3.client('docdb')

# Create a new database
db_name = "my_database"
response = client.create_db_instance(
    DBInstanceIdentifier=db_name,
    Engine='docdb',
    StorageEncrypted=True,
    DBInstanceClass='db.r5.large',
    VpcSecurityGroupIds=['sg-0123456789abcdef0'],
    AvailabilityZone='us-west-2a',
    PreferredMaintenanceWindow='sat:05:00-sat:05:30',
    AutoMinorVersionUpgrade=True,
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'Development'
        },
    ]
)

# Get a list of databases
response = client.describe_db_instances()
print("List of Databases:")
for db_instance in response['DBInstances']:
    print(db_instance['DBInstanceIdentifier'])
