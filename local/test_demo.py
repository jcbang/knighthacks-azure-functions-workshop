import requests
import json

# Input your endpoint URLs here
CREATE_DATA_URL = '<URL>'
READ_DATA_URL = '<URL>'
UPDATE_DATA_URL = '<URL>'
DELETE_DATA_URL = '<URL>'

def send_web_request(url: str, obj: dict) -> None:
    # Send a post request to the specified URL with a data input
    res = requests.post(url, data = json.dumps(obj))

    # Status code 200 is the universal "success" response
    if res.status_code == 200:
        print('\tSuccess!')
    else:
        print('\tSomething went wrong :(')

    print(f'\tResponse: {res.text}\n')

# An object we want to create in our database
create_data_object = {
    'id': '123', # Our object ID (and our partition key)
    'name': 'fruit smoothie', # Data types can be simple strings...
    'ingredients': ['blueberry', 'strawberry'], # or arrays...
    'properties': { # or even a whole nested object!
        'texture': 'smooth',
        'flavor': 'berry',
        'color': 'purple'
    }
}

# An object containing only the key of the object we want to create in our database
# This is used for "READING" and "DELETING" data (since read and deletions require only the key)
read_data_object = {
    'id': '123'
}

# An object containing the key of the object we want to update in our database
# and any fields we wish to update for that specific object;
# Since we want to update the 'name' field, we include that in our body
update_data_object = {
    'id': '123',
    'object_to_update': {
        'name': 'berry fruit smoothie'
    }
}

# --- TEST OBJECT CREATION --------------------------------

# 1. Create the object in the database using the create_data_object
print('Sending data to the CREATE endpoint; response is:')
send_web_request(CREATE_DATA_URL, create_data_object)

# 2. See if the object exists in the database using the read_data_object
print('Sending data to the READ endpoint; response is:')
send_web_request(READ_DATA_URL, read_data_object)

# --- TEST OBJECT UPDATE ----------------------------------

# 3. Update the object in the database using the update_data_object
print('Sending data to the UPDATE endpoint; response is:')
send_web_request(UPDATE_DATA_URL, update_data_object)

# 4. See if the object correctly updated in the database using the read_data_object
print('Sending data to the READ endpoint; response is:')
send_web_request(READ_DATA_URL, read_data_object)

# --- TEST OBJECT DELETE ----------------------------------

# 5. Delete the object in the database using the read_data_object
print('Sending data to the DELETE endpoint; response is:')
send_web_request(DELETE_DATA_URL, read_data_object)

# 6. See if the object correctly deleted in the database using the read_data_object
print('Sending data to the READ endpoint; response is:')
send_web_request(READ_DATA_URL, read_data_object)

# --- END -------------------------------------------------
