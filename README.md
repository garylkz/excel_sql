## Requirements

Python 3.14 or above

## Build

Make sure that `pyinstaller` is installed with:

```bat
pip install pyinstaller
```

To compile a windows executable, run:

```sh
pyinstaller --onefile --windowed --icon=kokocat.ico -w 'gui.py' -n 'XL2Q'
```
