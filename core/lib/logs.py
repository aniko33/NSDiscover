from rich import print

def file_error(filename: str):
    print(f"[red]ERROR[/red]: {filename} is empty i is not valid as wordlist")

def file_notFound(filename: str):
    print(f"[red]ERROR[/red]: {filename} not found")

def file_isDir(filename: str):
    print(f"[red]ERROR[/red]: {filename} it's not a file")