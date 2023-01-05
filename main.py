import csv
import typer
from SampleServer import app as sample_app
from SampleServer.models import Game, Player, Word, Ref_Player_Words, Prompt

app = typer.Typer()

@app.command()
def seedwords(file: str):
    print(f"Loading {file} into words table")
    with open(file) as csvfile:
        spamreader = csv.reader(csvfile)
        list = [x[0] for x in spamreader]
        with sample_app.app_context():
            for word in list:
                print(f"creating {word}")
                Word.create(text=word)

@app.command()
def seedprompts(file: str):
    pass

if __name__ == "__main__":
    app()