import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import logging
import azure.functions as func
from util.cosmos_connection import create_data_helper

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('create_data is processing a request...')

    # The object we wish to create comes from the input json body
    object_to_create = req.get_json()
    
    create_data_helper(object_to_create)

    return func.HttpResponse(body = 'Success!', status_code = 200)