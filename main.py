import flet as ft 
def main(page):
    page.title = "pruebas"
    page.window_width = 400
    page.window_heigth = 300
    page.theme_mode = "dark"
    page.scroll = "adaptive"
    page.update()
    #funciones del programa
    def añadir(e):
        c1.controls.append(ft.Checkbox(label=texto.value))
        c1.update()
    def eliminar(e):
        c1.clean()
        c1.update()
    def notas(e):
        c4.controls.append(ft.Text(texto2.value))
        c4.update()
    #bases de la aplicacion 
    texto = ft.TextField(hint_text="ponga su tarea")
    boton = ft.TextButton(text="añadir",on_click=añadir)
    boton2 = ft.TextButton(text="delete",on_click=eliminar)
    boton_boton2 = ft.Column(controls=[boton,boton2])
    c1 = ft.Column()
    c3 =  ft.Column()
    c2 = ft.Row(spacing=0,controls=[c1,c3])
    #containers
    contenedor1 = ft.Container(ft.Row(controls=[texto,boton_boton2]))
    contenedor2 = ft.Container(c2)
    contenedor3 = ft.Container(ft.Column(controls=[contenedor1,contenedor2]))
    #creando anotaciones
    texto2 = ft.TextField(hint_text="anotacion que quiere recordar")
    boton2 = ft.TextButton(text="añadir",on_click=notas)
    c4 = ft.Column()
    contenedor4 = ft.Container(c4)
    contenedor5 = ft.Container(ft.Row(controls=[texto2,boton2]))
    contenedor6 = ft.Container(ft.Column(controls=[contenedor5,contenedor4]))
    #navegacion del menu
    activas = ft.Tab(text="tareas",content=contenedor3)
    terminadas = ft.Tab(text="terminadas",content=contenedor6)
    #menu
    menu = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            activas,
            terminadas
        ]
    )
    page.add(menu)
ft.app(target=main)