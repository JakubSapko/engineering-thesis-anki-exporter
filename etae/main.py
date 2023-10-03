import click
import platform
from etae.utils.message_utils import format_config_message

from etae.utils.utils import get_config_file


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--anon",
    help="Show your current config. Use --anon to anonymize your password",
    is_flag=True,
)
def config(anon: bool):
    current_system: str = platform.system()
    config = get_config_file(current_system)
    formatted_message: str = format_config_message(config, anon)
    click.echo("Current config:")
    click.echo(formatted_message)


@cli.command()
@click.argument("val")
def set_bar(val):
    click.echo("Dropped the database")
