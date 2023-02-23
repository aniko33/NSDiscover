# Nebula Subdomain Discover

# Index

- [Features](#features)

- [Installation](#Installation)

- [Compiling using Nuitka](#compiling-using-nuitka)

- [Usage](#usage)

- [Showcase](#showcase)

- [License](#license)

- [Contributors](#contributors)

# Features

- Fast (using Nuitka compiled version)

- CLI (command line interface)

# Installation

To install **NSDiscover** you need **Python** and **PIP** if you can ***run these commands to install*** it:

```bash
# Debian
sudo apt install python3 python3-pip
# optional 
sudo apt install python3 python-is-python3

# Fedora
sudo dnf install python3 python3-pip

# Arch linux
sudo pacman -S python3 python3-pip
```

###### Now install NSDiscover:

```bash
git clone https://github.com/aniko33/NSDiscover
cd NSDiscover
pip install -r requirements.txt 
sudo mkdir /opt/nsd
sudo cp -r * /opt/nsd
sudo cp main.py /bin/nsdiscover
echo "Usage: nsdiscover <args> --help"
```

# Compiling using Nuitka

if you want an **executable twice as fast** you can use ***nuitka*** a **compiler** that converts the code to C and then compiles it

```bash
sudo pip install nuitka
nuitka3 --follow-imports main.py
sudo cp main.bin /bin/nsdiscover 
```

or

```bash
pip install nuitka
nuitka --follow-imports main.py
sudo cp main.bin /bin/nsdiscover 
```

# Usage

```
Usage: main.py [OPTIONS] DOMAIN

Options:
  -w, --wordlist TEXT  [required]
  -s, --ssl BOOLEAN    Allows you to send HTTPS packets
  -v, --verbose
  --help               Show this message and exit.
```

**Basic usage**: `nsdiscover google.com -w /your/wordlist`

**Verbose**: `nsdiscover -v google.com -w /your/wordlist`

**Using HTTPS (SSL)**: `nsdiscover --ssl google.com -w /your/wordlist`

# Showcase
![image](https://user-images.githubusercontent.com/76649588/221003684-016860d9-ba5b-4448-b0fd-44ec7b4d42a9.png)
# License

This application is distributed under the ***[GPL](https://it.wikipedia.org/wiki/GNU_General_Public_License) license*** you can ***consult the file***: ***[LICENSE.txt](LICENSE.txt)***

# Contributors

<a href="https://github.com/aniko33/NSDiscover/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=aniko33/NSDiscover"/>
</a>
