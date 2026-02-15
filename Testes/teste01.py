import flet as ft

def main(page: ft.Page):
    page.title = "Teste 01"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 300

    linha01 = ft.Row(controls=[ft.Text("Lin1 Col01 | "), ft.Text("Lin1 Col02 | "), ft.Text("Lin1 Col03 | ")])
    linha02 = ft.Row(controls=[ft.Text("Lin2 Col01 | "), ft.Text("Lin2 Col02 | "), ft.Text("Lin2 Col03 | ")])
    linha03 = ft.Row(controls=[ft.Text("Lin3 Col01 | "), ft.Text("Lin3 Col02 | "), ft.Text("Lin3 Col03 | ")])

    coluna = ft.Column(
        controls=[
            linha01,
            linha02,
            linha03
        ]
    )

    page.add(coluna)

ft.app(target=main)
