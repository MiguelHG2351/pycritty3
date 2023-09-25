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

    # add grettings method
    # @staticmethod
    @click.command()
    @click.option('--name', prompt='Enter your name', help='Name to greet')
    def grettings(name):
        click.echo(f"Hello {name}")

    @click.command()
    @click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="r")
    @click.argument("todofile", type=click.Path(exists=False), required=0)
    @click.option("-n", "--name", prompt="Enter the todo name", help="Name of the todo")
    @click.option("-d", "--description", prompt="Describe the todo", help="The description of the todo")
    def add_todos(name, description, priority, todofile):
        filename = todofile if todofile is not None else "mytodo.txt"
        with open(filename, "a+") as f:
            f.write(f"{name}: {description} [Priority {PRIORITIES[priority]} ]\n")



    def run(self):
        print("Hello World")
        mycommands.add_command(self.add_todos)
        mycommands()
