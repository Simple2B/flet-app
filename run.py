import flet

from app import main

if __name__ == "__main__":
    from app.config import config

    cfg = config()
    flet.app(target=main)
