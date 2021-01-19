from json import dump as dump_json

import click

import takeonme.aws.route53 as r53


@click.group("aws")
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Enumerate AWS resources that can be hijacked for the current
    default AWS boto3 credentials

    """
    pass


@cli.command("domains")
@click.option("--json", default=False, is_flag=True)
@click.pass_context
def domains(ctx: click.Context, json: bool) -> None:
    """Fetch, buffer, and write AWS DNS records to the output file

    Sort, de-dupe, and print one unique domain name per line
    or when --json is provided pretty print JSON with sorted keys

    """
    output = ctx.obj["output"]
    records = r53.get_all_records()
    if json:
        dump_json(records, output, sort_keys=True, indent=4)
    else:
        record_names = [
            record.get("Name", None)
            for record in records
            if record and record.get("Name", None)
        ]
        for unique_domain in sorted(set(record_names)):
            output.write(f"{unique_domain}\n")
