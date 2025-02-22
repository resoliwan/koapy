import click

from koapy.cli.utils import verbose_option
from koapy.cli.utils.pywin32 import install_pywin32


@click.command(short_help="Install pywin32 and run post install script.")
@click.option("--version", metavar="VERSION", help="Version of pywin32 to install.")
@verbose_option(default=5)
def pywin32(version, verbose):
    install_pywin32(version)
