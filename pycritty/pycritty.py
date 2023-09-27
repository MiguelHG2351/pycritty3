import click

@click.group
def mycommands():
    pass

@click.command()
@click.option('--name', prompt='Enter your name', help='Name to greet')
def grettings(name):
    click.echo(f"Hello {name}")
    print("Something")

PRIORITIES = {
    'o': "Optional",
    'r': "Recommended",
    'e': "Essential"
}
class Pycritty:

    def __init__(self):
        pass

    @click.group()
    def font():
        pass

    @font.command() # options for local and global font
    @click.option('--local', '-l', is_flag=True, help='Install font locally')
    @click.option('--global', '-g', is_flag=True, help='Install font globally')
    def list():

        click.echo("Font list")

    def run(self):
        print("Hello World")
        mycommands.add_command(self.font)
        mycommands()
