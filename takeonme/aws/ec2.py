from typing import Any, Dict, Generator, List

import boto3


def get_client() -> boto3.session.Session.client:
    """
    Returns a botocore.client.Route53 with the default AWS creds
    """
    return boto3.client("ec2")


def fetch_elastic_ips(
    client: boto3.session.Session.client,
) -> Generator[Dict[str, Any], None, None]:
    response = client.describe_addresses()
    assert "Addresses" in response
    yield from response["Addresses"]


def get_all_elastic_ips() -> List[Dict[str, Any]]:
    """
    Return Route53 DNS resource record sets

    https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecordSet.html
    """
    client = get_client()
    return list(fetch_elastic_ips(client))
