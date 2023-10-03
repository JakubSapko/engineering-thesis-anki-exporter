import click
import platform
from etae.utils.message_utils import format_config_message

from etae.utils.utils import get_config_file, set_config_file


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    current_system: str = platform.system()
    ctx.ensure_object(dict)
    ctx.obj["system"] = current_system
    click.echo("Welcome to etae!")


@cli.command()
@click.option(
    "--anon",
    help="Show your current config. Use --anon to anonymize your password",
    is_flag=True,
)
@click.pass_context
def get_config(ctx, anon: bool):
    current_system: str = ctx.obj["system"]
    config = get_config_file(current_system)
    formatted_message: str = format_config_message(config, anon)
    click.echo("Current config:")
    click.echo(formatted_message)


@cli.command()
@click.pass_context
def set_config(ctx):
    click.echo("Welcome to config setup!")
    is_finished = False
    while not is_finished:
        login = click.prompt("Please enter your login")
        password = click.prompt("Please enter your password")
        click.echo(f"Your login: {login}\nYour password: {password}")
        is_correct = click.confirm("Is this correct?")
        if is_correct:
            is_finished = True
            set_config_file(ctx.obj["system"], login, password)
    click.echo("Config setup finished!")
