from typing import List

import click
import platform

from etae.utils.anki_utils import get_decks_data, invoke
from etae.utils.api_utils import send_data_to_etae
from etae.utils.message_utils import format_config_message
from etae.utils.utils import get_config_file, set_config_file


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    current_system: str = platform.system()
    ctx.ensure_object(dict)
    ctx.obj["system"] = current_system
    click.echo("Welcome to etae!")


@cli.command(
    help="Show your current config. Use --anon to anonymize your password",
)
@click.option(
    "--anon",
    is_flag=True,
)
@click.pass_context
def get_config(ctx, anon: bool):
    current_system: str = ctx.obj["system"]
    config = get_config_file(current_system)
    formatted_message: str = format_config_message(config, anon)
    click.echo("Current config:")
    click.echo(formatted_message)


@cli.command(help="Set your config.")
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


@cli.command(help="Send your Anki data to ETAE.")
@click.pass_context
def send_anki_data(ctx):
    current_system: str = ctx.obj["system"]
    config = get_config_file(current_system)
    if config is None:
        click.echo("Config file not found, please set it up first")
        return
    deck_result: dict[str, List[str] | None] = invoke("deckNames")
    deck_names: List[str] | None = deck_result.get("result")
    if deck_names is None:
        click.echo("No decks found")
        return
    is_selected = False
    selected_decks = set()
    while not is_selected:
        click.echo("Please select a deck:")
        for index, deck_name in enumerate(deck_names):
            click.echo(f"{index + 1}. {deck_name}")
        click.echo("Enter X to finish selection")
        selected_option = click.prompt("")
        if selected_option in ["X", "x"]:
            is_selected = True
            continue
        selected_option = int(selected_option)
        if selected_option > len(deck_names) or selected_option < 1:
            click.echo("Invalid deck number")
            continue
        deck_name: str = deck_names[selected_option - 1]
        click.echo(f"Selected deck: {deck_name}")
        is_correct = click.confirm("Is this correct?")
        if is_correct:
            selected_decks.add(deck_name)
    cards_info = get_decks_data(selected_decks)
    _ = send_data_to_etae(config, cards_info)
