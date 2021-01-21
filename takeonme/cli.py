from typing import Union, IO

import click

import takeonme.aws.commands
import takeonme.gcp.commands


@click.group()
@click.pass_context
def cli(ctx: click.Context) -> None:
    ctx.ensure_object(dict)


@cli.group("list")
@click.option("-i", "--input", type=click.File("r"), default=None)
@click.option("-o", "--output", type=click.File("w"), default="-")
@click.pass_context
def list_(
    ctx: click.Context, output: click.File, input: Union[IO[str], str, None]
) -> None:
    if input is not None and input == "-":
        input = click.get_text_stream("stdin", encoding="utf8", errors="strict")

    ctx.obj["input"] = input
    ctx.obj["output"] = output


list_.add_command(takeonme.aws.commands.list_)
list_.add_command(takeonme.gcp.commands.list_)


if __name__ == "__main__":
    cli()
