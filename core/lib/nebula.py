import os
import requests
import sys

from rich import print

try:
    from core.lib import logs
except ModuleNotFoundError:
    sys.path.insert(1, "/opt/nsd")
  
    from core.lib import logs

class Nebula:
    def __init__(self, domain, wordlist, ssl, verbose) -> None:
        self.domain = domain
        self.wordlist = wordlist
        self.ssl = ssl
        self.verbose = verbose

    def get_words(self):
        # Check file exists
        if not os.path.exists(self.wordlist):
            logs.file_notFound(self.wordlist)
            quit()
        # Check if the file is a directory
        else:
            if not os.path.isfile(self.wordlist):
                logs.file_isDir(self.wordlist)
                quit()

        # verbose
        if self.verbose:
            print(f"[reset][magenta][$][/magenta] file opening: {self.wordlist.split('/')[-1]}")
        
        with open(self.wordlist, "rb") as f:
            # verbose
            if self.verbose:
                print(f"[reset][magenta][$][/magenta] reading {self.wordlist.split('/')[-1]}...")
            return f.read().splitlines()
    
    def sending(self, words: list):
        for word in words:
            word = word.decode()
            try:
                if self.ssl:
                    url = f"https://{word}.{self.domain}"
                else:
                    url = f"http://{word}.{self.domain}"

                r = requests.get(url)

                print(f"[reset][green][+][/green] {url} ({r.status_code})")

            except requests.exceptions.ConnectionError:
                # verbose
                if self.verbose:
                    print(f"[reset][red][-][/red] {url}")

    def run(self):
        words: list = self.get_words()
        
        # verbose
        if self.verbose:
            print(f"[reset][cyan][!][/cyan] starting the attack")

        self.sending(words)