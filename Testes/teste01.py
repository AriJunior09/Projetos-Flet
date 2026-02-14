import flet as ft

def main(page: ft.Page):
    page.title = "Teste 01"
    page.window.width = 400
    page.window.height = 300
    page.padding = ft.padding.all(20)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def on_click(e):
        print("Botão clicado!")

    button = ft.ElevatedButton(text="Clique aqui", on_click=on_click)
    page.add(button)