import json

import click

import takeonme.aws.route53 as r53


@click.group("aws")
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Enumerate AWS resources that can be hijacked for the current
    default AWS boto3 credentials

    """
    pass


@cli.command("dns")
@click.pass_context
def dns(ctx: click.Context) -> None:
    """Fetch and write AWS DNS records to the output file

    Buffers records in memory then pretty prints them to the output
    file as JSON with sorted keys

    """
    json.dump(r53.get_all_records(), ctx.obj["output"], sort_keys=True, indent=4)
