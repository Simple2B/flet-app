import flet as ft

from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider
from app.config import config

conf = config()


def login_by_github(page: ft.Page):
    provider = GitHubOAuthProvider(
        client_id=conf.GITHUB_CLIENT_ID,
        client_secret=conf.GITHUB_CLIENT_SECRET,
        redirect_url=conf.GITHUB_REDIRECT_URL,
    )
    page.login(provider)

    def login_click(e):
        page.login(provider)

    def on_login(e):
        print("Access token:", page.auth.token.access_token)
        print("User ID:", page.auth.user.id)

    page.on_login = on_login
    page.add(ft.ElevatedButton("Login with GitHub", on_click=login_click))
    page.update()
