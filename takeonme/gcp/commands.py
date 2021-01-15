import json

import click

import takeonme.gcp.cloud_dns as cloud_dns


@click.group("gcp")
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Enumerate GCP resources that can be hijacked"""
    pass


@cli.command("dns")
@click.pass_context
def dns(ctx: click.Context) -> None:
    """Fetch and write GCP DNS records to the output file

    Buffers records in memory then pretty prints them to the output
    file as JSON with sorted keys

    """
    json.dump(
        cloud_dns.get_all_records(),
        ctx.obj["output"],
        sort_keys=True,
        indent=4,
    )
