import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import logging
import azure.functions as func
from util.cosmos_connection import delete_data_helper

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('delete_data is processing a request...')

    # Get the 'id' field from the input request json body
    json_body = req.get_json()
    id_to_delete = json_body['id']

    try:
        delete_data_helper(id_to_delete)

        return func.HttpResponse(body = f'Successfully deleted object with id {id_to_delete}', status_code = 200)
    except:
        return func.HttpResponse(body = 'Resource not found', status_code = 400)
