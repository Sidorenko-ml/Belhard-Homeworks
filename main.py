# Написать программу, которая упорядочивает файлы в директории 
# Символ - должен стать символом / в пути к файлу (pathlib)

from pathlib import Path
from random import randint
import click


@click.command()
@click.argument('restructure_directory')
def restructure_directory(restructure_directory):
    Path('directory').mkdir(exist_ok=True)
    for i in range(10):
        Path(f'directory/'
        f'{randint(2020, 2022)}-'
        f'{randint(1,12)}-'
        f'{randint(1, 31)}.txt').touch()
    dir = Path('directory')
    for path in dir.iterdir():
        if "2020" in path.stem and path.suffix == '.txt':
            if path.name[6] == "-": 
                Path(f'directory/{path.stem[:4]}').mkdir(exist_ok=True)
                Path(f'directory/{path.stem[:4]}/{path.name[5]}').mkdir(exist_ok=True)
                if path.name[-6] == "-":
                    Path(f'directory/{path.stem[:4]}/{path.name[5]}/'f'{path.name[-5:]}').touch()
                else:
                    Path(f'directory/{path.stem[:4]}/{path.name[5]}/'f'{path.name[-6:]}').touch()
            else:
                Path(f'directory/{path.stem[:4]}').mkdir(exist_ok=True)
                Path(f'directory/{path.stem[:4]}/{path.name[5:7]}').mkdir(exist_ok=True)
                if path.name[-6] == "-":
                    Path(f'directory/{path.stem[:4]}/{path.name[5:7]}/'f'{path.name[-5:]}').touch()
                else:
                    Path(f'directory/{path.stem[:4]}/{path.name[5:7]}/'f'{path.name[-6:]}').touch()
            Path(f'directory/'f'{path.name}').unlink() # Удаляет файлы

        if "2021" in path.stem and path.suffix == '.txt':
            if path.name[6] == "-": 
                Path(f'directory/{path.stem[:4]}').mkdir(exist_ok=True)
                Path(f'directory/{path.stem[:4]}/{path.name[5]}').mkdir(exist_ok=True)
                if path.name[-6] == "-":
                    Path(f'directory/{path.stem[:4]}/{path.name[5]}/'f'{path.name[-5:]}').touch()
                else:
                    Path(f'directory/{path.stem[:4]}/{path.name[5]}/'f'{path.name[-6:]}').touch()
            else:
                Path(f'directory/{path.stem[:4]}').mkdir(exist_ok=True)
                Path(f'directory/{path.stem[:4]}/{path.name[5:7]}').mkdir(exist_ok=True)
                if path.name[-6] == "-":
                    Path(f'directory/{path.stem[:4]}/{path.name[5:7]}/'f'{path.name[-5:]}').touch()
                else:
                    Path(f'directory/{path.stem[:4]}/{path.name[5:7]}/'f'{path.name[-6:]}').touch()
            Path(f'directory/'f'{path.name}').unlink() # Удаляет файлы
            
        if "2022" in path.stem and path.suffix == '.txt':
            if path.name[6] == "-": 
                Path(f'directory/{path.stem[:4]}').mkdir(exist_ok=True)
                Path(f'directory/{path.stem[:4]}/{path.name[5]}').mkdir(exist_ok=True)
                if path.name[-6] == "-":
                    Path(f'directory/{path.stem[:4]}/{path.name[5]}/'f'{path.name[-5:]}').touch()
                else:
                    Path(f'directory/{path.stem[:4]}/{path.name[5]}/'f'{path.name[-6:]}').touch()
            else:
                Path(f'directory/{path.stem[:4]}').mkdir(exist_ok=True)
                Path(f'directory/{path.stem[:4]}/{path.name[5:7]}').mkdir(exist_ok=True)
                if path.name[-6] == "-":
                    Path(f'directory/{path.stem[:4]}/{path.name[5:7]}/'f'{path.name[-5:]}').touch()
                else:
                    Path(f'directory/{path.stem[:4]}/{path.name[5:7]}/'f'{path.name[-6:]}').touch()
            Path(f'directory/'f'{path.name}').unlink() # Удаляет файлы


if __name__ == "__main__":
    restructure_directory()