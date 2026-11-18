# PythonOSINT

A small Python tool that checks whether a user id appears on public profile pages.

## Setup

Python 3.10 or newer is required. Libraries live in a virtual environment and are listed in `requirements.txt`. Do not copy them into the repository.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate with `.venv\Scripts\activate`.

## Run

```bash
python OSINT.py
```

`.venv/` is listed in `.gitignore`, so the environment stays on your machine and is not pushed to GitHub.
