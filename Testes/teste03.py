import flet as ft

def main(page):
    page.title = "Seja bem vindo!"
    page.window.width = 400
    page.window.height = 500

    def login(e):

        if not entrada_nome.value:
            entrada_nome.error_text = "Favor digite o seu nome!"
            entrada_nome.error_text = "Favor digite o seu nome!"
            page.update()

        if not entrada_senha.value:
            entrada_senha.error_text = "Senha obrigatória!"
            page.update()

        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f"Nome: {nome}\nSenha: {senha}")

            page.clean()
            page.add(ft.Text(f"Olá, {nome}\nSeja bem vindo ao nosso sistema!"))
            pass

    entrada_nome = ft.TextField(label="Digite seu nome...")
    entrada_senha = ft.TextField(label="Digite a sua senha...")
    botao_login = ft.ElevatedButton("Login", on_click=login)


    page.add(
        entrada_nome,
        entrada_senha,
        botao_login
    )


ft.app(target=main)
