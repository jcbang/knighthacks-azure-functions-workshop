import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import logging
import json
import azure.functions as func
from util.cosmos_connection import read_data_helper

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('read_data is processing a request...')

    # Get the 'id' field from the input request json body
    json_body = req.get_json()
    id_to_read = json_body['id']

    try:
        found_object = read_data_helper(id_to_read)

        return func.HttpResponse(body = json.dumps(found_object), status_code = 200)
    except:
        return func.HttpResponse(body = 'Resource not found', status_code = 400)
