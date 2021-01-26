# takeonme

[![PyPI version](https://badge.fury.io/py/takeonme.svg)](https://badge.fury.io/py/takeonme)

`takeonme` enumerates resources that could be hijacked or taken over
(e.g. subdomains, hosted zones, IP, or other resources in a common
global namespace).


## Example usage

1. Run `pip install takeonme` to install the `takeonme` command from
   PyPI

1. [Configure
   credentials](https://github.com/mozilla-services/takeonme/#implemented-resources)
   for the service you want to enumerate

1. Run `takeonme list <service name> <resource name>` to list
   resources from a service (e.g. `takeonme list aws domains`)

1. Run a tool to detect whether any of the resources can be hijacked
   (e.g. [subjack](https://github.com/haccer/subjack) for subdomains)

1. Reserve or take down the hijackable resources (they should be gone in a day or two)


## Non-goals

`takeonme` does **not** run against multiple services or accounts or
use multiple credentials instead invoke it multiple times with
different default credentials.

`takeonme` does **not** enumerate resources that cannot be hijacked.


## Developing

Requirements:

* git
* [Python 3.8 or newer](https://www.python.org/downloads/)
* [poetry](https://python-poetry.org/)

1. `git clone` the repository

1. run `poetry install`


To add a new service or resource, follow [this template](https://github.com/mozilla-services/takeonme/issues/new?template=custom.md).


## Implemented resources

* [AWS Route53 DNS records](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecord.html)
* [AWS EC2 Elastic IPs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Address.html)
  * [configuring credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials)

* [GCP Cloud DNS records](https://cloud.google.com/dns/docs/reference/v1/resourceRecordSets#resource)
  * [configuring credentials](https://cloud.google.com/docs/authentication/production)
