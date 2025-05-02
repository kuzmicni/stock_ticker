import click
from .main import show_ytd

@click.command()
@click.argument("ticker")
def main(ticker):
    """Get the Year-to-Date (YTD) performance for a stock ticker."""
    try:
        result = show_ytd(ticker.upper())
        click.echo(click.style(f"{ticker.upper()} is {result:+.2f}% YTD.", fg="green" if result > 0 else "red"))
    except Exception as e:
        click.echo(click.style(f"Error: {e}", fg="yellow"))
