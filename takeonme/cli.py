import click

import takeonme.aws.commands
import takeonme.gcp.commands


@click.group()
@click.option("-o", "--output", type=click.File("wb"), default="-")
@click.pass_context
def cli(ctx: click.Context, output: click.File) -> None:
    ctx.ensure_object(dict)
    ctx.obj["output"] = output


cli.add_command(takeonme.aws.commands.cli)
cli.add_command(takeonme.gcp.commands.cli)


if __name__ == "__main__":
    cli()
