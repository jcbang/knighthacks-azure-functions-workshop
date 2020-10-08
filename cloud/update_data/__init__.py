import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import logging
import azure.functions as func
from util.cosmos_connection import update_data_helper

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('update_data is processing a request...')

    # The object we wish to update comes from the input json body
    json_body = req.get_json()
    id_to_update = json_body['id']
    object_to_update = json_body['object_to_update']

    try:
        update_data_helper(id_to_update, object_to_update)

        return func.HttpResponse(body = 'Successfully updated object', status_code = 200)
    except:
        return func.HttpResponse(body = 'Resource not found', status_code = 400)
