import click
#
# @click.group
# def mycommands():
#     pass
#
# @click.command()
# @click.option('--name', prompt='Enter your name', help='Name to greet')
# def grettings(name):
#     click.echo(f"Hello {name}")
#     print("Something")
#
# PRIORITIES = {
#     'o': "Optional",
#     'r': "Recommended",
#     'e': "Essential"
# }
class Pycritty:

    def __init__(self):
        pass

    @click.group()
    @click.pass_context
    def cli(self):
        pass

    @cli.group()
    @click.pass_context
    def font(self):
        pass

    @font.command() # options for local and global font
    @click.option('--local', '-l', is_flag=True, help='Install font locally')
    @click.option('--system', '-g', is_flag=True, help='Install font globally')
    @click.pass_context
    def list(self, local, system):

        click.echo(f"Font list of {local} and {system}")

    def run(self):
        print("Hello World")
        self.cli()

def main():
    pycritty = Pycritty()

    pycritty.run()

if __name__ == '__main__':
    main()