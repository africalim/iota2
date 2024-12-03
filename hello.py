#!/usr/bin/env python3 

#pip install click
import click

@click.command() # decorates the function to designate it as a Click command
@click.argument('name') # specifies name as a required command-line argument.
def hello(name):
   """Simple program that greets the NAME provided"""
   click.echo(f"Hello {name}, how are you?") #prints the output to the terminal.


if __name__ == '__main__':
    hello()
