import flet as ft


def main(page: ft.Page):
    page.title = "Seja bem vindo!"
    page.window.width = 400
    page.window.height = 500

    entrada_nome = ft.TextField(label="Digite seu nome...")
    entrada_senha = ft.TextField(label="Digite a sua senha...")

    def login(e):
        # Limpar mensagens de erro anteriores
        entrada_nome.error_text = None
        entrada_senha.error_text = None

        tem_erro = False

        if not entrada_nome.value or entrada_nome.value.strip() == "":
            entrada_nome.error_text = "Favor digite o seu nome!"
            tem_erro = True

        if not entrada_senha.value or entrada_senha.value.strip() == "":
            entrada_senha.error_text = "Senha obrigatória!"
            tem_erro = True

        if tem_erro:
            # Atualiza os campos para mostrar os erros
            entrada_nome.update()
            entrada_senha.update()
            return

        # Se não há erro, prossegue
        nome = entrada_nome.value
        senha = entrada_senha.value
        print(f"Nome: {nome}\nSenha: {senha}")

        page.clean()
        page.add(ft.Text(f"Olá, {nome}\nSeja bem vindo ao nosso sistema!"))
        page.update()

    botao_login = ft.ElevatedButton("Login", on_click=login)

    page.add(
        entrada_nome,
        entrada_senha,
        botao_login
    )


ft.app(target=main)