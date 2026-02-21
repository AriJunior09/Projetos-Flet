import flet as ft

def main(page):
    page.window.width = 400
    page.window.height = 500

    def login(e):

        # Limpa erros anteriores
        entrada_nome.error_text = None
        entrada_senha.error_text = None

        erro = False

        if not entrada_nome.value:
            entrada_nome.error_text = "Por favor preencha o seu nome!"
            erro = True

        if not entrada_senha.value:
            entrada_senha.error_text = "Senha obrigatoria!"
            erro = True

        entrada_nome.update()
        entrada_senha.update()

        if erro:
            return

        nome = entrada_nome.value
        senha = entrada_senha.value
        print(f"Nome: {nome}\nSenha: {senha}")

        page.clean()
        page.add(ft.Text(f"Olá, {nome}\nSeja bem vindo!"))

    entrada_nome = ft.TextField(label="Digite seu nome...", width=300)
    entrada_senha = ft.TextField(label="Digite a sua senha...", password=True, width=300)

    page.add(
        ft.Column(
            [
                entrada_nome,
                entrada_senha,
                ft.ElevatedButton("Login", on_click=login),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


ft.app(target=main)