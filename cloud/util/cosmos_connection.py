from azure.cosmos import exceptions, CosmosClient, PartitionKey

# Initialize the Cosmos client
# You can find the ENDPOINT and KEY values by going to your Azure portal online and clicking on the
# "keys" section of your CosmosDB service!
ENDPOINT = '<INSERT COSMOSDB ENDPOINT>'
KEY = '<INSERT PRIVATE KEY>'

# Initialize your CosmosDB Client
cosmos_client = CosmosClient(ENDPOINT, KEY)

# Initialize your database if it doesn't exist
database_name = 'demo_database'
cosmos_database = cosmos_client.create_database_if_not_exists(id = database_name)

# Initialize your container inside of the database if it doesn't exist
container_name = 'demo_container'
cosmos_container = cosmos_database.create_container_if_not_exists(id = container_name, 
    partition_key = PartitionKey(path = '/id'),
    offer_throughput = 400)

def create_data_helper(obj: dict) -> None:
    response = cosmos_container.create_item(body = obj)

def read_data_helper(id_number: str) -> dict:
    return cosmos_container.read_item(item = id_number, partition_key = id_number)

def update_data_helper(id_number: str, obj: dict) -> None:
    read_item = cosmos_container.read_item(item = id_number, partition_key = id_number)
    
    print(read_item)
    for key in obj:
        read_item[key] = obj[key]
    print(read_item)

    response = cosmos_container.upsert_item(body = read_item)

def delete_data_helper(id_number: str) -> None:
    response = cosmos_container.delete_item(item = id_number, partition_key = id_number)
