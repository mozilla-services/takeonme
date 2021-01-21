from json import dump as dump_json

import click


@click.group("example_service")
@click.pass_context
def list_(ctx: click.Context) -> None:
    """Enumerate resources for example service that can be hijacked"""
    pass


@list_.command("example_resource")
@click.option("--json", default=False, is_flag=True)
@click.pass_context
def example_resource(ctx: click.Context, json: bool) -> None:
    """Fetch and write example resource entries to the output file

    Buffers records in memory then pretty prints them to the output
    file as JSON with sorted keys

    """
    output = ctx.obj["output"]
    records = example_service_client.get_all_of_example_resource()
    if json:
        dump_json(records, output, sort_keys=True, indent=4)
    else:
        for record in records:
            output.write(f"{record}\n")
