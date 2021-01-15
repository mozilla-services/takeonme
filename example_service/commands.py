import json

import click


@click.group("example_service")
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Enumerate resources for example service that can be hijacked"""
    pass


@cli.command("example_resource")
@click.pass_context
def example_resource(ctx: click.Context) -> None:
    """Fetch and write example resource entries to the output file

    Buffers records in memory then pretty prints them to the output
    file as JSON with sorted keys

    """
    json.dump(
        example_service_client.get_all_of_example_resource(),
        ctx.obj["output"],
        sort_keys=True,
        indent=4,
    )
