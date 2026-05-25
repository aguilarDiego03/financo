import flet as ft

def MenuView(page: ft.Page, user_data):

    def cerrar_sesion(e):
        page.user_data = None
        page.go("/")

    def ir_cuenta(e):
        print("Ir a cuenta")

    def ir_consejos(e):
        print("Ir a consejos")

    def ir_inversiones(e):
        print("Ir a inversiones")

    return ft.View(
        route="/menu",
        bgcolor="#EAF0FF",
        controls=[
            ft.Container(
                bgcolor="#57689E",
                padding=20,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text("FinanceApp", size=30, weight="bold", color="white"),
                        ft.Row(
                            spacing=15,
                            controls=[
                                ft.TextButton("Inicio", style=ft.ButtonStyle(color="white")),
                                ft.TextButton("Cuenta", on_click=ir_cuenta, style=ft.ButtonStyle(color="white")),
                                ft.TextButton("Consejos", on_click=ir_consejos, style=ft.ButtonStyle(color="white")),
                                ft.TextButton("Inversiones", on_click=ir_inversiones, style=ft.ButtonStyle(color="white")),
                            ]
                        )
                    ]
                )
            ),
            ft.Container(
                padding=30,
                expand=True,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30,
                    controls=[
                        ft.Text(
                            f"¡Bienvenido {user_data.get('nombre', 'Usuario')}!",
                            size=40,
                            weight="bold",
                            color="#2D3E6F"
                        ),
                        ft.Card(
                            elevation=10,
                            content=ft.Container(
                                width=700,
                                padding=40,
                                bgcolor="white",
                                border_radius=20,
                                content=ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=20,
                                    controls=[
                                        ft.Text("💰", size=60),
                                        ft.Text(
                                            "¿Qué son las finanzas?",
                                            size=28,
                                            weight="bold",
                                            color="#57689E"
                                        ),
                                        ft.Text(
                                            "Las finanzas son la administración del dinero. "
                                            "Ayudan a controlar ingresos, gastos, ahorros "
                                            "e inversiones para tomar mejores decisiones económicas.",
                                            size=16,
                                            text_align=ft.TextAlign.CENTER
                                        ),
                                    ]
                                )
                            )
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20,
                            wrap=True,
                            controls=[
                                crear_tarjeta("💵", "Ahorro", "Guardar dinero para metas futuras"),
                                crear_tarjeta("📈", "Inversión", "Hacer crecer tu dinero"),
                                crear_tarjeta("📊", "Presupuesto", "Organiza tus ingresos y gastos"),
                            ]
                        ),
                        ft.ElevatedButton(
                            "Cerrar Sesión",
                            on_click=cerrar_sesion,
                            bgcolor="#57689E",
                            color="white",
                            width=200
                        )
                    ]
                )
            )
        ]
    )

def crear_tarjeta(icono, titulo, descripcion):
    return ft.Card(
        elevation=5,
        content=ft.Container(
            width=250,
            padding=20,
            bgcolor="white",
            border_radius=12,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    ft.Text(icono, size=45),
                    ft.Text(titulo, size=22, weight="bold"),
                    ft.Text(descripcion, text_align=ft.TextAlign.CENTER, color="#555555"),
                ]
            )
        )
    )