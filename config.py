import sys
from pathlib import Path
import dotenv

DOT_ENV_PATH = Path() / '.env.production'
if DOT_ENV_PATH.exists():
    dotenv.read_dotenv(str(DOT_ENV_PATH))
else:
    print(
        "No .env.local or .env.production found, be sure to make it.\n"
        "You can rename .env.example file to .env and "
        "set your environ variable in it."
    )
    sys.exit()

wsgi_app = "config.wsgi"
