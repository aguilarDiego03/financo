import flet as ft

def CuentaView(page: ft.Page, user_data):

    def volver_menu(e):
        page.views.pop()
        page.update()

    def cerrar_sesion(e):
        page.user_data = None
        page.go("/")

    return ft.View(
        route="/cuenta",
        bgcolor="#EAF0FF",
        padding=0,
        controls=[
            ft.Container(
                bgcolor="#57689E",
                padding=20,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text("FinanCO - Mi Cuenta", size=30, weight="bold", color="white"),
                        ft.TextButton("Volver al Inicio", on_click=volver_menu, style=ft.ButtonStyle(color="white")),
                    ]
                )
            ),
            ft.Container(
                expand=True,
                padding=30,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Text(
                            "👤 Mi Cuenta",
                            size=35,
                            weight="bold",
                            color="#2D3E6F"
                        ),
                        ft.Card(
                            elevation=8,
                            content=ft.Container(
                                width=500,
                                padding=30,
                                bgcolor="white",
                                border_radius=20,
                                content=ft.Column(
                                    spacing=15,
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Text("👤", size=30),
                                                ft.Text("Nombre:", size=16, weight="bold"),
                                                ft.Text(user_data.get('nombre', 'No disponible'), size=16),
                                            ]
                                        ),
                                        ft.Divider(),
                                        ft.Row(
                                            controls=[
                                                ft.Text("📧", size=30),
                                                ft.Text("Email:", size=16, weight="bold"),
                                                ft.Text(user_data.get('email', 'No disponible'), size=16),
                                            ]
                                        ),
                                        ft.Divider(),
                                        ft.Row(
                                            controls=[
                                                ft.Text("🆔", size=30),
                                                ft.Text("ID Usuario:", size=16, weight="bold"),
                                                ft.Text(str(user_data.get('id_usuario', 'No disponible')), size=16),
                                            ]
                                        ),
                                        ft.Divider(),
                                        ft.Row(
                                            controls=[
                                                ft.Text("📅", size=30),
                                                ft.Text("Miembro desde:", size=16, weight="bold"),
                                                ft.Text(user_data.get('fecha_registro', 'No disponible'), size=16),
                                            ]
                                        ),
                                        ft.Container(height=20),
                                        ft.ElevatedButton(
                                            "Cerrar Sesión",
                                            on_click=cerrar_sesion,
                                            bgcolor="#57689E",
                                            color="white",
                                            width=200,
                                        ),
                                    ]
                                )
                            )
                        ),
                    ]
                )
            )
        ]
    )