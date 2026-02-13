import flet as ft

class Checkbox(ft.Row):                 # Herda de ft.Row
    def __init__(self, text):           # Construtor recebe o texto da tarefa
        super().__init__()              # Chama o construtor da classe pai (ft.Row)
        self.text_view = ft.Text(text)  # Componente de texto
        
        # Campo de edição, inicialmente invisível
        self.text_edit = ft.TextField(value=text, visible=False) 
        
        # Botão de editar
        self.edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=self.edit) 
        
        # Botão de salvar, inicialmente invisível
        self.save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=self.save, visible=False, icon_color="green") 
        
        # Botão de deletar
        self.delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=self.delete, icon_color="red") 
        
        # Row é um container horizontal que organiza seus filhos em linha
        # Controls é uma lista de controles filhos do Row
        self.controls = [ # Adiciona os controles ao Row (O Row é um container horizontal)
            ft.Checkbox(),          # Caixa de seleção
            self.text_view,         # Componente de texto
            self.text_edit,         # Campo de edição
            self.edit_button,       # Botão de editar
            self.save_button,       # Botão de salvar
            self.delete_button      # Botão de deletar
        ]
        
    def edit(self, e):
        self.edit_button.visible = False   # Botão de editar fica invisível
        self.save_button.visible = True    # Botão de salvar fica visível
        self.delete_button.visible = False # Botão de deletar fica invisível
        self.text_view.visible = False     # Texto fica invisível
        self.text_edit.visible = True      # Campo de edição fica visível
        self.update()
        
    def save(self, e):
        self.save_button.visible = False   # Botão de salvar fica invisível
        self.edit_button.visible = True    # Botão de editar fica visível
        self.text_view.visible = True      # Texto fica visível
        self.text_edit.visible = False     # Campo de edição fica invisível
        self.delete_button.visible = True  # Botão de deletar fica visível
        if self.text_edit.value.strip() == "":  # Verifica se o campo de edição não está vazio
            self.text_edit.value = self.text_view.value  # Se estiver vazio, mantém o texto original            
        self.text_view.value = self.text_edit.value  # Atualiza o texto com o valor do campo de edição
        self.update()                      # Atualiza a interface
            
    def delete(self, e):
        self.visible = False              
        self.update()                 
        