import flet as ft

def MenuView(page: ft.Page, user_data):
    
    def cerrar_sesion(e):
        page.go("/")
    
    return ft.View(
        route="/menu",
        bgcolor="#57689E",
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Column(
                [
                    ft.Text(" MENÚ PRINCIPAL ", size=40, weight="bold", color=ft.Colors.WHITE),
                    ft.Container(height=20),
                    ft.Text(
                        f"Bienvenido {user_data.get('nombre', 'Usuario')}!", 
                        size=32, 
                        weight="bold", 
                        color=ft.Colors.YELLOW_400
                    ),
                    ft.Container(height=30),
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text("Has iniciado sesión correctamente", size=18, color="#333"),
                                ft.Divider(),
                                ft.Text(f" Email: {user_data.get('email', '')}", size=14, color="#666"),
                                ft.Text(f" ID Usuario: {user_data.get('id_usuario', '')}", size=12, color="#999"),
                                ft.Text(f" Fecha registro: {user_data.get('fecha_registro', '')}", size=12, color="#999"),
                                ft.Container(height=20),
                                ft.ElevatedButton(
                                    "Cerrar Sesión",
                                    on_click=cerrar_sesion,
                                    bgcolor="#57689E",
                                    color="white",
                                    width=200,
                                ),
                            ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            padding=40,
                            bgcolor=ft.Colors.WHITE,
                        ),
                        elevation=5,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]
    )