from typing import Any, Dict, Generator, List

import google.auth
import googleapiclient.discovery


def get_default_credentials() -> Any:
    credentials, _ = google.auth.default()
    return credentials


def get_service_client(service_name: str, service_version: str) -> Any:
    return googleapiclient.discovery.build(
        service_name, service_version, credentials=get_default_credentials()
    )


def fetch_projects() -> Generator[Dict[Any, Any], None, None]:
    """
    Fetch and yield GCP projects

    https://cloud.google.com/resource-manager/reference/rest/v1/projects#Project
    """
    client = get_service_client("cloudresourcemanager", "v1")
    while True:
        request = client.projects().list()
        response = request.execute()

        for project in response.get("projects", []):
            yield project

        request = client.projects().list_next(
            previous_request=request, previous_response=response
        )


def fetch_managed_zones_for_project(
    project: str,
) -> Generator[Dict[Any, Any], None, None]:
    """
    Fetch and yield the GCP project's managed zones

    https://cloud.google.com/dns/docs/reference/v1/managedZones#resource
    """
    client = get_service_client("dns", "v1")
    request = client.managedZones().list(project=project)
    while request is not None:
        response = request.execute()

        for managed_zone in response["managedZones"]:
            yield managed_zone

        request = client.managedZones().list_next(
            previous_request=request, previous_response=response
        )


def fetch_records_for_project_and_managed_zone(
    project: str, managed_zone: str
) -> Generator[Dict[Any, Any], None, None]:
    """
    Fetch and yield GCP Cloud DNS records for the project's managed zone

    https://cloud.google.com/dns/docs/reference/v1/resourceRecordSets#resource

    managed_zone is the zone name or id.
    """
    client = get_service_client("dns", "v1")

    request = client.resourceRecordSets().list(
        project=project, managedZone=managed_zone
    )
    while request is not None:
        response = request.execute()

        for resource_record_set in response["rrsets"]:
            yield resource_record_set

        request = client.resourceRecordSets().list_next(
            previous_request=request, previous_response=response
        )


def get_all_records() -> List[Dict[str, Any]]:
    return [
        record
        for project in fetch_projects()
        for zone in fetch_managed_zones_for_project(project["name"])
        for record in fetch_records_for_project_and_managed_zone(
            project["name"], zone["name"]
        )
    ]
