import json
project_id = "cs-792-my-health"
location = "us-west1"
dataset_id = "cs-792-test-dataset"
fhir_store_id = "fhir-test-2"
resource_type = "Patient"
resource_id = "0e653090-559e-40db-ac77-bec7ace3f148"

import argparse
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="~/cs-792-my-health-083c7ccd10ab.json"

# [START healthcare_get_fhir_store]
# project_id, location, dataset_id, fhir_store_id
def get_fhir_store():
    """Gets the specified FHIR store.

    

    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
    before running the sample."""

    project_id = "cs-792-my-health"
    location = "us-west1"
    dataset_id = "cs-792-test-dataset"
    fhir_store_id = "fhir-test-2"

    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    # Imports Python's built-in "json" module
    import json

    api_version = "v1"
    service_name = "healthcare"
    # Instantiates an authorized API client by discovering the Healthcare API
    # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = discovery.build(service_name, api_version)

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'  # replace with your GCP project ID
    # location = 'us-central1'  # replace with the parent dataset's location
    # dataset_id = 'my-dataset'  # replace with the FHIR store's parent dataset
    # fhir_store_id = 'my-fhir-store'  # replace with the FHIR store's ID
    fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, location, dataset_id
    )
    fhir_store_name = "{}/fhirStores/{}".format(fhir_store_parent, fhir_store_id)

    fhir_stores = client.projects().locations().datasets().fhirStores()
    fhir_store = fhir_stores.get(name=fhir_store_name).execute()

    print(json.dumps(fhir_store, indent=2))
    return json.dumps(fhir_store)


# [END healthcare_get_fhir_store]


# [START healthcare_list_fhir_stores]
def list_fhir_stores(project_id, location, dataset_id):
    """Lists the FHIR stores in the given dataset.
    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
    before running the sample."""
    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    api_version = "v1"
    service_name = "healthcare"
    # Instantiates an authorized API client by discovering the Healthcare API
    # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = discovery.build(service_name, api_version)

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'  # replace with your GCP project ID
    # location = 'us-central1'  # replace with the dataset's location
    # dataset_id = 'my-dataset'  # replace with the parent dataset's ID
    fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, location, dataset_id
    )

    fhir_stores = (
        client.projects()
        .locations()
        .datasets()
        .fhirStores()
        .list(parent=fhir_store_parent)
        .execute()
        .get("fhirStores", [])
    )

    for fhir_store in fhir_stores:
        print(fhir_store)

    return fhir_stores


# [END healthcare_list_fhir_stores]


def testing():
    print("Testing 123")


def get_resource():
    """Gets a FHIR resource.

    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
    before running the sample."""
    # Imports Python's built-in "os" module
    import os

    # Imports the google.auth.transport.requests transport
    from google.auth.transport import requests

    # Imports a module to allow authentication using a service account
    from google.oauth2 import service_account


    project_id = "cs-792-my-health"
    location = "us-west1"
    dataset_id = "cs-792-test-dataset"
    fhir_store_id = "fhir-test-2"
    resource_type = "Patient"
    resource_id = "0e653090-559e-40db-ac77-bec7ace3f148"

    # Gets credentials from the environment.
    credentials = service_account.Credentials.from_service_account_file(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
    )
    scoped_credentials = credentials.with_scopes(
        ["https://www.googleapis.com/auth/cloud-platform"]
    )
    # Creates a requests Session object with the credentials.
    session = requests.AuthorizedSession(scoped_credentials)

    # URL to the Cloud Healthcare API endpoint and version
    base_url = "https://healthcare.googleapis.com/v1"

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'  # replace with your GCP project ID
    # location = 'us-central1'  # replace with the parent dataset's location
    # dataset_id = 'my-dataset'  # replace with the parent dataset's ID
    # fhir_store_id = 'my-fhir-store' # replace with the FHIR store ID
    # resource_type = 'Patient'  # replace with the FHIR resource type
    # resource_id = 'b682d-0e-4843-a4a9-78c9ac64'  # replace with the FHIR resource's ID
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, location)

    resource_path = "{}/datasets/{}/fhirStores/{}/fhir/{}/{}".format(
        url, dataset_id, fhir_store_id, resource_type, resource_id
    )

    # Sets required application/fhir+json header on the request
    headers = {"Content-Type": "application/fhir+json;charset=utf-8"}

    response = session.get(resource_path, headers=headers)
    response.raise_for_status()

    resource = response.json()

    print("Got {} resource:".format(resource["resourceType"]))
    print(json.dumps(resource, indent=2))

    return resource
