from json import (
    dump as dump_json,
    load as load_json,
)

import click

from takeonme.util import sorted_unique_by_key
import takeonme.aws.route53 as r53
import takeonme.aws.ec2 as ec2


@click.group("aws")
@click.pass_context
def list_(ctx: click.Context) -> None:
    """Enumerate AWS resources that can be hijacked for the current
    default AWS boto3 credentials

    """
    pass


@list_.command("domains")
@click.option("--json", default=False, is_flag=True)
@click.pass_context
def domains(ctx: click.Context, json: bool) -> None:
    """Fetch, buffer, and write AWS DNS records to the output file

    Sort, de-dupe, and print one unique domain name per line
    or when --json is provided pretty print JSON with sorted keys

    """
    input = ctx.obj["input"]
    output = ctx.obj["output"]

    records = load_json(input) if input is not None else r53.get_all_records()
    if json:
        dump_json(records, output, sort_keys=True, indent=4)
    else:
        for unique_domain in sorted_unique_by_key(records, "Name"):
            output.write(f"{unique_domain}\n")


@list_.command("ips")
@click.option("--json", default=False, is_flag=True)
@click.pass_context
def ips(ctx: click.Context, json: bool) -> None:
    """Fetch, buffer, and write AWS Elastic IP addresses to the output file

    Sort, de-dupe, and print one unique IPs name per line
    or when --json is provided pretty print JSON with sorted keys

    """
    input = ctx.obj["input"]
    output = ctx.obj["output"]

    records = load_json(input) if input is not None else ec2.get_all_elastic_ips()
    if json:
        dump_json(records, output, sort_keys=True, indent=4)
    else:
        for public_ip in sorted_unique_by_key(records, "PublicIp"):
            output.write(f"{public_ip}\n")
