from typing import List

import logging

from time import sleep
from tqdm import tqdm

from google.cloud import aiplatform
from google.api_core.exceptions import ResourceExhausted

SLEEP_TIME = 30

logger = logging.getLogger('google.cloud.aiplatform.base')
logger.setLevel(logging.WARNING)

def delete(items: List):
    for item in tqdm(items):
        try:
            item.delete()
        except ResourceExhausted:
            print(f"Cooling down API limiter, sleeping {SLEEP_TIME} s")
            sleep(SLEEP_TIME)
            item.delete()

if __name__ == "__main__":

    # Delete all custom jobs

    print("Deleteing custom jobs")
    jobs = aiplatform.CustomJob.list()
    delete(jobs)

    # Delete training pipelines
    print("Deleteing custom training pipelines")
    jobs = aiplatform.CustomTrainingJob.list()
    delete(jobs)

    # Delete models
    print("Deleteing models")
    models = aiplatform.Model.list()
    delete(models)

    # Delete all pipelines
    print("Deleteing custom jobs")
    pipelines = aiplatform.PipelineJob.list()
    delete(pipelines)

    # Delete metadatastore
    print('Delete metadatastore')

    PROJECT_ID = 'boris001'
    LOCATION = 'us-central1'
    API_ENDPOINT = "{}-aiplatform.googleapis.com".format(LOCATION)
    METADATA_STORE = 'default'

    # Vertex AI location root path for your dataset, model and endpoint resources
    PARENT = "projects/" + PROJECT_ID + "/locations/" + LOCATION + "/metadataStores/" + METADATA_STORE

    from google.cloud import aiplatform_v1beta1 as aip

    client_options = {"api_endpoint": API_ENDPOINT}
    store_client = aip.MetadataServiceClient(
       client_options = {"api_endpoint": API_ENDPOINT}
    )

    from google.cloud.aiplatform_v1beta1.types.metadata_service import DeleteMetadataStoreRequest

    request = DeleteMetadataStoreRequest(name = PARENT)
    result = store_client.delete_metadata_store(request=request)
    