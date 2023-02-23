#!/usr/bin/python3
import os
import click
import sys

from rich import print
from rich.align import Align

try:
    from core.lib import banner
    from core.lib import nebula
except ModuleNotFoundError:
    sys.path.insert(1, "/opt/nsd")
    
    from core.lib import banner
    from core.lib import nebula

@click.command()
@click.option("-w", "--wordlist", required=True, type=str)
@click.option("-s", "--ssl", default=False, type=bool, help="Allows you to send HTTPS packets")
@click.option("-v", "--verbose", is_flag=True, default=False, type=bool)
@click.argument("domain", type=str)

def main(domain, wordlist, ssl, verbose):
    # Getting the size of terminal
    columns, lines = os.get_terminal_size()

    if columns <= 39:
        print(Align(banner.banner_small()))
    else: print(Align(banner.banner_large()))

    nebula.Nebula(domain, wordlist, ssl, verbose).run()

if __name__ == "__main__":
    main()