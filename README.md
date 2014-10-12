# AoikWinWhich
[AoikWinWhich](https://github.com/AoiKuiyuyou/AoikWinWhich) written in Python.

Tested working with:
- Python: 2.5+ and 3.0+
- Windows 8.1
- Windows earlier versions should work but not tested

## Table of Contents
- [Setup](#setup)
  - [Setup via git](#setup-via-git)
  - [Setup via pip](#setup-via-pip)
- [Usage](#usage)

## Setup
- [Setup via git](#setup-via-git)
- [Setup via pip](#setup-via-pip)

### Setup via git
Clone this git repository to local:
```
git clone https://github.com/AoiKuiyuyou/AoiWinWhich-Python
```

In the local repository directory, the
[entry program](/src/aoikwinwhich/aoikwinwhich.py) can be run directly without further
installation:
```
python src/aoikwinwhich/aoikwinwhich.py
```

If you prefer an installation, run the **setup.py** file in the local repository
directory:
```
python setup.py install
```

The installation will install program files into Python's "package directory".
As a result, the entry program is also accessible via module name:
```
python -m aoikwinwhich.aoikwinwhich
```

And the installation will create an executable file in Python's
"script directory". If Python's "script directory" has been added to your
command console's **PATH** environment variable, the entry program should be
accessible in short name:
```
aoikwinwhich
```

### Setup via pip
Run:
```
pip install git+https://github.com/AoiKuiyuyou/AoikWinWhich-Python
```

Installing via pip is equivalent to cloning this git repository to local and
running the **setup.py** file in the local repository directory.

## Usage
See [usage](https://github.com/AoiKuiyuyou/AoikWinWhich#how-to-use) in the
general project [AoikWinWhich](https://github.com/AoiKuiyuyou/AoikWinWhich).
