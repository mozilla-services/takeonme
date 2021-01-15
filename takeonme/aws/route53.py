from typing import Any, Dict, Generator, List

import boto3


def get_client() -> boto3.session.Session.client:
    """
    Returns a botocore.client.Route53 with the default AWS creds
    """
    return boto3.client("route53")


def fetch_hosted_zones(
    client: boto3.session.Session.client,
) -> Generator[Dict[str, Any], None, None]:
    for zone in client.get_paginator("list_hosted_zones").paginate():
        assert "HostedZones" in zone
        yield zone["HostedZones"]


def fetch_records_for_hosted_zone(
    client: boto3.session.Session.client, hosted_zone: Dict[str, Any]
) -> Generator[Dict[str, Any], None, None]:
    assert "Id" in hosted_zone
    for record_set in client.get_paginator("list_resource_record_sets").paginate(
        HostedZoneId=hosted_zone["Id"]
    ):
        assert "ResourceRecordSets" in record_set
        yield record_set["ResourceRecordSets"]


def get_all_records() -> List[Dict[str, Any]]:
    client = get_client()
    return [
        record
        for zone in fetch_hosted_zones(client)
        for record in fetch_records_for_hosted_zone(client, zone)
    ]
