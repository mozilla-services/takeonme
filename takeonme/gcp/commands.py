from json import dump as dump_json

import click

import takeonme.gcp.cloud_dns as cloud_dns


@click.group("gcp")
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Enumerate GCP resources that can be hijacked"""
    pass


@cli.command("domains")
@click.option("--json", default=False, is_flag=True)
@click.pass_context
def domains(ctx: click.Context, json: bool) -> None:
    """Fetch, buffer, and write GCP DNS records to the output file

    Sort, de-dupe, and print one unique domain name per line
    or when --json is provided pretty print JSON with sorted keys

    """
    output = ctx.obj["output"]
    records = cloud_dns.get_all_records()
    if json:
        dump_json(
            records,
            output,
            sort_keys=True,
            indent=4,
        )
    else:
        record_names = [
            record.get("name", None)
            for record in records
            if record and record.get("name", None)
        ]
        for unique_domain in sorted(set(record_names)):
            output.write(f"{unique_domain}\n")
