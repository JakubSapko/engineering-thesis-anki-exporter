import click
import platform
from etae.utils.message_utils import format_config_message

from etae.utils.utils import get_config_file


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.option(
    "--anon",
    help="Show your current config. Use --anon to anonymize your password",
    is_flag=True,
)
def get_config(anon: bool):
    current_system: str = platform.system()
    config = get_config_file(current_system)
    formatted_message: str = format_config_message(config, anon)
    click.echo("Current config:")
    click.echo(formatted_message)


@cli.command()
@click.argument("val")
def set_config(val):
    click.echo("Dropped the database")
