import flet as ft

def ConsejosView(page: ft.Page, user_data):

    def volver_menu(e):
        page.views.pop()
        page.update()

    consejos = [
        {"icono": "💡", "titulo": "Ahorra el 20% de tus ingresos", 
         "descripcion": "La regla 50/30/20 es una excelente guía: 50% necesidades, 30% deseos, 20% ahorro."},
        {"icono": "🆘", "titulo": "Crea un fondo de emergencia", 
         "descripcion": "Ahorra de 3 a 6 meses de gastos para imprevistos como pérdida de empleo o emergencias médicas."},
        {"icono": "💳", "titulo": "Evita deudas de alto interés", 
         "descripcion": "Las tarjetas de crédito pueden tener intereses del 30% o más. Paga el total cada mes."},
        {"icono": "📈", "titulo": "Invierte temprano", 
         "descripcion": "El interés compuesto es tu mejor aliado. Comienza a invertir cuanto antes, aunque sea con poco dinero."},
        {"icono": "🥚", "titulo": "Diversifica tus inversiones", 
         "descripcion": "No pongas todos los huevos en la misma canasta. Distribuye tu dinero en diferentes activos."},
        {"icono": "📚", "titulo": "Educación financiera continua", 
         "descripcion": "Lee libros, toma cursos y mantente actualizado sobre finanzas personales."},
    ]

    return ft.View(
        route="/consejos",
        bgcolor="#EAF0FF",
        controls=[
            ft.Container(
                bgcolor="#57689E",
                padding=20,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text("FinanCO - Consejos Financieros", size=30, weight="bold", color="white"),
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
                            "📚 Consejos Financieros",
                            size=35,
                            weight="bold",
                            color="#2D3E6F"
                        ),
                        ft.Text(
                            "Mejora tu salud financiera con estos consejos prácticos",
                            size=18,
                            color="#555555",
                        ),
                        ft.Container(height=10),
                        ft.Column(
                            spacing=15,
                            controls=[
                                ft.Card(
                                    elevation=4,
                                    content=ft.Container(
                                        padding=20,
                                        bgcolor="white",
                                        border_radius=12,
                                        content=ft.Row(
                                            controls=[
                                                ft.Text(c["icono"], size=40),
                                                ft.Column(
                                                    spacing=10,
                                                    expand=True,
                                                    controls=[
                                                        ft.Text(c["titulo"], size=18, weight="bold", color="#57689E"),
                                                        ft.Text(c["descripcion"], size=14, color="#555555"),
                                                    ]
                                                ),
                                            ]
                                        )
                                    )
                                ) for c in consejos
                            ]
                        ),
                    ]
                )
            )
        ]
    )