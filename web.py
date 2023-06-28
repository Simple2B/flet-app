import flet as ft

from app import main

if __name__ == "__main__":
    from app.config import config

    config = config()
    ft.app(
        name=config.FLET_NAME,
        target=main,
        view=None,
        port=config.FLET_PORT,
        host=config.FLET_HOST,
    )
