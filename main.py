import click


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
    if anon:
        click.echo("Your config is: ...")
    click.echo("Initialized the database")


@cli.command()
@click.argument("val")
def set_bar(val):
    click.echo("Dropped the database")
