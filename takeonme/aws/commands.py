from json import (
    dump as dump_json,
    load as load_json,
)

import click

from takeonme.dns_util import records_to_sorted_unique_domains
import takeonme.aws.route53 as r53


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
        for unique_domain in records_to_sorted_unique_domains(
            records, name_field="Name"
        ):
            output.write(f"{unique_domain}\n")
