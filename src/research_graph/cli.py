import logging

import typer

from research_graph import __version__
from research_graph.config import get_settings
from research_graph.logging_setup import setup_logging

app = typer.Typer(help="Research graph command line tool.")
logger = logging.getLogger(__name__)


def mask_token(token: str | None) -> str:
    if not token:
        return "not set"
    if len(token) <= 8:
        return "****"
    return f"{token[:4]}****{token[-4:]}"


@app.command(help="Show the package version.")
def version() -> None:
    typer.echo(__version__)


@app.command("check-config", help="Load settings and print a summary.")
def check_config() -> None:
    settings = get_settings()
    setup_logging(settings.log_level)
    logger.info("Settings loaded")
    typer.echo(f"github_token: {mask_token(settings.github_token)}")
    typer.echo(f"data_dir: {settings.data_dir}")
    typer.echo(f"log_level: {settings.log_level}")
    typer.echo(f"request_timeout: {settings.request_timeout}")
    typer.echo(f"max_concurrency: {settings.max_concurrency}")
