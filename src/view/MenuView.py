import flet as ft

def MenuView(page: ft.Page, user_data, auth_controller):

    def cerrar_sesion(e):
        page.user_data = None
        page.go("/")

    def ir_cuenta(e):
        from view.CuentaView import CuentaView
        page.views.append(CuentaView(page, user_data))
        page.update()

    def ir_consejos(e):
        from view.ConsejosView import ConsejosView
        page.views.append(ConsejosView(page, user_data))
        page.update()

    def ir_inversiones(e):
        from view.InversionesView import InversionesView
        page.views.append(InversionesView(page, user_data))
        page.update()

    def ir_calculadora(e):
        from view.CalculadoraView import CalculadoraView
        page.views.append(CalculadoraView(page, user_data, auth_controller))
        page.update()

    return ft.View(
        route="/menu",
        bgcolor="#EAF0FF",
        padding=0,
        spacing=0,
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
                                ft.TextButton("Calculadora", on_click=ir_calculadora, style=ft.ButtonStyle(color="white")),
                            ]
                        )
                    ]
                )
            ),
            ft.Container(
                expand=True,
                padding=30,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Container(height=20),
                        ft.Text(
                            f"¡Bienvenido {user_data.get('nombre', 'Usuario')}!",
                            size=40,
                            weight="bold",
                            color="#2D3E6F",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            "Tu plataforma de educación financiera",
                            size=20,
                            color="#555555",
                            text_align=ft.TextAlign.CENTER,
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
                                            color="#57689E",
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                        ft.Text(
                                            "Las finanzas son la administración del dinero. "
                                            "Ayudan a controlar ingresos, gastos, ahorros "
                                            "e inversiones para tomar mejores decisiones económicas.",
                                            size=16,
                                            text_align=ft.TextAlign.CENTER,
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
                            width=200,
                        ),
                        ft.Container(height=20),
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