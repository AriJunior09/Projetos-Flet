import flet as ft


def main(page: ft.Page):
    page.title = "Teste 02"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 500
    page.window.resizable = True
    
    
    
    
    
    
ft.app(target=main)