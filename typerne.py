import typer

app = typer.Typer()


@app.command()
def hello(name: str, age :int):
    name =''
    for i in range (10):
        name = name + '1'
        print(f"Hello {name} and {age}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()