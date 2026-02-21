import flet as ft


def main(page: ft.Page):
    page.title = "Teste 02"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 500
    page.window.resizable = True

    txt_titulo = ft.Text('Descrição do produto: ')
    produto = ft.TextField(label="Digite a descrição do produto...", text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do produto ')
    preco = ft.TextField(value="0", label="Digite o Preço...", text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Cadastrar')

    page.add(
        txt_titulo, 
        produto,
        txt_preco,
        preco,
        btn_produto
        
    )


ft.app(target=main)
