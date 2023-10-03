import click
import platform

from etae.utils.utils import find_config_file


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
    print(current_system)
    config = find_config_file(current_system)
    if anon:
        click.echo("Your config is: ...")


@cli.command()
@click.argument("val")
def set_bar(val):
    click.echo("Dropped the database")
