import flet as ft 
from custom_checkbox import Checkbox

def main(page: ft.Page):
    page.title = "Minhas tarefas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 450
    page.window.height = 650
    page.padding = ft.padding.only(top=20, left=20, right=20, bottom=20)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    
    async def add_task(e):
        if new_task.value.strip() == "":
            return # Não adiciona tarefas vazias
        
        task_list.controls.append(Checkbox(new_task.value))
        new_task.value = ''
        page.update()
        await new_task.focus()    # Foca o campo de texto após adicionar a tarefa
        
        
    
    new_task = ft.TextField(hint_text='Insira uma tarefa...', expand=True, on_submit=add_task)
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD
, on_click=add_task)

    task_list = ft.Column(spacing=4) # Adiciona um espaçamento entre as tarefas
    
    card = ft.Column(
        width=400,
            controls=[
                ft.Row(
                    controls=[
                        new_task,
                        new_button
                    ]
                ),
                task_list,
            ]
    )
    

    page.add(card)


ft.app(target=main)


