import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name', required=True)
def run(name):
    """Start project"""

    click.echo(f"Starting project: {name}")

if __name__ == '__main__':
    cli()