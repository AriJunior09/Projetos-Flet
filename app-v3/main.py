import flet as ft
import json
import os

FILE_NAME = "tasks.json"

def main(page: ft.Page):
    page.title = "Minhas tarefas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 420
    page.window.height = 650
    page.padding = ft.padding.only(top=20, left=20,right=20, bottom=20)
    page.bottom_appbar = ft.BottomAppBar(
        content=ft.Row(
            controls=[
                ft.Text("Autor: Ari Júnior - Versão: 1.0"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    tasks_column = ft.Column()

    # -------------------------
    # SALVAR EM JSON
    # -------------------------
    def save_tasks():
        tasks_data = []
        for row in tasks_column.controls:
            checkbox = row.controls[0]
            tasks_data.append({
                "text": checkbox.label,
                "done": checkbox.value
            })

        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(tasks_data, f, indent=4)

    # -------------------------
    # CRIAR TAREFA
    # -------------------------
    def create_task(text, done=False):

        def on_change(e):
            save_tasks()

        def delete_task(e):
            tasks_column.controls.remove(task_row)
            save_tasks()
            page.update()

        task_checkbox = ft.Checkbox(
            label=text,
            value=done,
            on_change=on_change
        )

        task_row = ft.Row(
            controls=[
                task_checkbox,
                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color="gray",
                    on_click=delete_task
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        return task_row

    # -------------------------
    # ADICIONAR
    # -------------------------
    async def add_task(e):
        if new_task.value.strip():
            task_row = create_task(new_task.value)
            tasks_column.controls.append(task_row)
            new_task.value = ""
            save_tasks()
            page.update()
            await new_task.focus()

    # -------------------------
    # CARREGAR
    # -------------------------
    def load_tasks():
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                tasks = json.load(f)
                for task in tasks:
                    task_row = create_task(task["text"], task["done"])
                    tasks_column.controls.append(task_row)

    new_task = ft.TextField(
        hint_text="Insira uma tarefa...",
        on_submit=add_task
    )

    new_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        on_click=add_task
    )

    page.add(
        ft.Column(
            [
                ft.Row([new_task, new_button]),
                tasks_column
            ]
        )
    )

    load_tasks()
    page.update()

ft.run(main)