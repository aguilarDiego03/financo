import flet as ft

def InversionesView(page: ft.Page, user_data):

    def volver_menu(e):
        page.views.pop()
        page.update()

    inversiones = [
        {"icono": "🏦", "titulo": "Plazos Fijos", "descripcion": "Inversión de bajo riesgo con rendimientos garantizados.", "riesgo": "Bajo"},
        {"icono": "📊", "titulo": "Acciones", "descripcion": "Compra de participaciones en empresas. Potencial de alto rendimiento.", "riesgo": "Alto"},
        {"icono": "🏠", "titulo": "Bienes Raíces", "descripcion": "Inversión en propiedades para renta o plusvalía.", "riesgo": "Medio"},
        {"icono": "💎", "titulo": "Criptomonedas", "descripcion": "Activos digitales con alta volatilidad y potencial.", "riesgo": "Muy Alto"},
        {"icono": "🥇", "titulo": "Oro y Metales", "descripcion": "Valor refugio tradicional contra la inflación.", "riesgo": "Bajo"},
        {"icono": "📚", "titulo": "Fondos de Inversión", "descripcion": "Diversificación automática con gestión profesional.", "riesgo": "Variable"},
    ]

    def get_color_riesgo(riesgo):
        if riesgo == "Bajo":
            return "#4CAF50"
        elif riesgo == "Medio":
            return "#FF9800"
        elif riesgo == "Alto":
            return "#F44336"
        elif riesgo == "Muy Alto":
            return "#9C27B0"
        else:
            return "#607D8B"

    return ft.View(
        route="/inversiones",
        bgcolor="#EAF0FF",
        controls=[
            ft.Container(
                bgcolor="#57689E",
                padding=20,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text("FinanCO - Inversiones", size=30, weight="bold", color="white"),
                        ft.TextButton("Volver al Inicio", on_click=volver_menu, style=ft.ButtonStyle(color="white")),
                    ]
                )
            ),
            ft.Container(
                padding=30,
                expand=True,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Text(
                            "📈 Tipos de Inversiones",
                            size=35,
                            weight="bold",
                            color="#2D3E6F"
                        ),
                        ft.Text(
                            "Conoce las diferentes opciones para hacer crecer tu dinero",
                            size=18,
                            color="#555555",
                        ),
                        ft.Container(height=10),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=30,
                            wrap=True,
                            controls=[
                                crear_tarjeta_inversion(
                                    inv["icono"],
                                    inv["titulo"],
                                    inv["descripcion"],
                                    inv["riesgo"],
                                    get_color_riesgo(inv["riesgo"])
                                ) for inv in inversiones
                            ]
                        ),
                    ]
                )
            )
        ]
    )

def crear_tarjeta_inversion(icono, titulo, descripcion, riesgo, color_riesgo):
    return ft.Card(
        elevation=5,
        content=ft.Container(
            width=300,
            padding=20,
            bgcolor="white",
            border_radius=15,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text(icono, size=40),
                    ft.Text(titulo, size=20, weight="bold", color="#57689E"),
                    ft.Text(descripcion, size=13, color="#666666", text_align=ft.TextAlign.CENTER),
                    ft.Container(
                        padding=5,
                        bgcolor=color_riesgo,
                        border_radius=10,
                        content=ft.Text(f"Riesgo: {riesgo}", size=12, color="white", weight="bold"),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )