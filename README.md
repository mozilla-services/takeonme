# takeonme

[![PyPI version](https://badge.fury.io/py/takeonme.svg)](https://badge.fury.io/py/takeonme)

`takeonme` enumerates resources that could be hijacked or taken over
(e.g. subdomains, hosted zones, IP, or other resources in a common
global namespace).


## Example usage

1. Run `pip install takeonme` to install the `takeonme` command from
   PyPI

1. Configure credentials for the service you want to enumerate
   (e.g. for
   [AWS](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials))

1. Run `takeonme <service name> <resource name>` to print API output a
   given resource from service name (e.g. `takeonme aws domains` for
   Route53 DNS records)

1. Run a tool to detect whether any of the resources can be hijacked
   (e.g. [subjack](https://github.com/haccer/subjack) for subdomains)

1. Reserve or take down the hijackable resources (they should be gone in a day or two)


## Non-goals

`takeonme` does **not** take on evaluating whether enumerated
resources can be hijacked instead use a red team tool.

`takeonme` does **not** run against multiple services or accounts or
use multiple credentials instead invoke it multiple times with
different default credentials.

`takeonme` does **not** enumerate resources that cannot be hijacked.


## Developing

Requirements:

* git
* [Python 3.8 or newer](https://www.python.org/downloads/)
* [poetry](https://python-poetry.org/)

1. `git clone` the repository then run `poetry install`

### Adding a new service or resource

Requirements:

* the resource can be hijacked i.e. it's on
  https://github.com/EdOverflow/can-i-take-over-xyz or similar

* the service provides an API to enumerate the resource (ideally a
  python client library too)

1. Run `cp -r example_service takeonme/` to recursively copy the
   example resource into the package namespace.

1. Run `mv takeonme/{example_service,service_name}`

1. Replace `example_*` with the service or resource name in
   `takeonme/service_name/commands.py`

1. Find a client library for the service and run `poetry add` to add
   the client libary to `takeonme` requirements

1. Add `cli.add_command(takeonme.<service_name>.commands.cli)` to
   `takeonme/cli.py`


## Implemented resources

* [AWS Route53 DNS records](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecord.html)
* [GCP DNS]()
