#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
import dotenv


def main():
    """Run administrative tasks."""
    if os.environ.get("STATE") == "LOCAL":
        DOT_ENV_PATH = Path() / '.env.local'
    else:
        DOT_ENV_PATH = Path() / '.env.production'
    if DOT_ENV_PATH.exists():
        dotenv.read_dotenv(str(DOT_ENV_PATH))
    else:
        print(
            "No .env.local or .env.production found, be sure to make it.\n"
            "set your environ variable in it."
        )
        return
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
