import flet as ft

def MenuView(page: ft.Page, user_data):

    # ======================================================
    # FUNCIONES
    # ======================================================

    def cerrar_sesion(e):
        page.go("/")

    def ir_inicio(e):
        print("Inicio")

    def ir_consejos(e):
        print("Consejos")

    def ir_inversiones(e):
        print("Inversiones")

    def ir_perfil(e):
        print("Perfil")

    # ======================================================
    # VIEW
    # ======================================================

    return ft.View(
        "/menu",
        bgcolor="#EAF0FF",
        scroll="auto",

        controls=[

            # ======================================================
            # BARRA SUPERIOR
            # ======================================================

            ft.Container(
                bgcolor="#57689E",
                padding=20,

                content=ft.Row(
                    alignment="spaceBetween",

                    controls=[

                        # TITULO

                        ft.Text(
                            "FinanceApp",
                            size=30,
                            weight="bold",
                            color="white"
                        ),

                        # BOTONES MENU

                        ft.Row(
                            spacing=15,

                            controls=[

                                ft.ElevatedButton(
                                    "Inicio",
                                    bgcolor="white",
                                    color="#57689E",
                                    on_click=ir_inicio
                                ),

                                ft.ElevatedButton(
                                    "Consejos",
                                    bgcolor="white",
                                    color="#57689E",
                                    on_click=ir_consejos
                                ),

                                ft.ElevatedButton(
                                    "Inversiones",
                                    bgcolor="white",
                                    color="#57689E",
                                    on_click=ir_inversiones
                                ),

                                ft.ElevatedButton(
                                    "Perfil",
                                    bgcolor="white",
                                    color="#57689E",
                                    on_click=ir_perfil
                                ),
                            ]
                        )
                    ]
                )
            ),

            # ======================================================
            # CONTENIDO PRINCIPAL
            # ======================================================

            ft.Container(
                padding=30,

                content=ft.Column(
                    horizontal_alignment="center",
                    spacing=25,

                    controls=[

                        # BIENVENIDA

                        ft.Text(
                            "¡Bienvenido {}!".format(
                                user_data.get("nombre", "Usuario")
                            ),
                            size=38,
                            weight="bold",
                            color="#2D3E6F"
                        ),

                        ft.Text(
                            "Tu espacio para aprender y mejorar tus finanzas personales.",
                            size=18,
                            color="#555555",
                            text_align="center"
                        ),

                        # ======================================================
                        # TARJETA PRINCIPAL
                        # ======================================================

                        ft.Card(
                            elevation=8,

                            content=ft.Container(
                                width=700,
                                padding=30,
                                border_radius=15,
                                bgcolor="white",

                                content=ft.Column(
                                    spacing=15,
                                    horizontal_alignment="center",

                                    controls=[

                                        ft.Text(
                                            "💰",
                                            size=60
                                        ),

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
                                            color="#444444",
                                            text_align="center"
                                        ),
                                    ]
                                )
                            )
                        ),

                        # ======================================================
                        # TARJETAS DE CONCEPTOS
                        # ======================================================

                        ft.Row(
                            alignment="center",
                            spacing=20,

                            controls=[

                                # AHORRO

                                ft.Card(
                                    elevation=5,

                                    content=ft.Container(
                                        width=250,
                                        padding=20,
                                        bgcolor="white",
                                        border_radius=12,

                                        content=ft.Column(
                                            horizontal_alignment="center",

                                            controls=[

                                                ft.Text(
                                                    "💵",
                                                    size=45
                                                ),

                                                ft.Text(
                                                    "Ahorro",
                                                    size=22,
                                                    weight="bold"
                                                ),

                                                ft.Text(
                                                    "Guardar dinero para metas futuras.",
                                                    text_align="center",
                                                    color="#555555"
                                                )
                                            ]
                                        )
                                    )
                                ),

                                # INVERSIONES

                                ft.Card(
                                    elevation=5,

                                    content=ft.Container(
                                        width=250,
                                        padding=20,
                                        bgcolor="white",
                                        border_radius=12,

                                        content=ft.Column(
                                            horizontal_alignment="center",

                                            controls=[

                                                ft.Text(
                                                    "📈",
                                                    size=45
                                                ),

                                                ft.Text(
                                                    "Inversiones",
                                                    size=22,
                                                    weight="bold"
                                                ),

                                                ft.Text(
                                                    "Hacer crecer el dinero mediante activos.",
                                                    text_align="center",
                                                    color="#555555"
                                                )
                                            ]
                                        )
                                    )
                                ),

                                # PRESUPUESTO

                                ft.Card(
                                    elevation=5,

                                    content=ft.Container(
                                        width=250,
                                        padding=20,
                                        bgcolor="white",
                                        border_radius=12,

                                        content=ft.Column(
                                            horizontal_alignment="center",

                                            controls=[

                                                ft.Text(
                                                    "📊",
                                                    size=45
                                                ),

                                                ft.Text(
                                                    "Presupuesto",
                                                    size=22,
                                                    weight="bold"
                                                ),

                                                ft.Text(
                                                    "Organiza ingresos y gastos correctamente.",
                                                    text_align="center",
                                                    color="#555555"
                                                )
                                            ]
                                        )
                                    )
                                ),
                            ]
                        ),

                        # ======================================================
                        # INFORMACION DEL USUARIO
                        # ======================================================

                        ft.Card(
                            elevation=6,

                            content=ft.Container(
                                width=500,
                                padding=25,
                                border_radius=15,
                                bgcolor="white",

                                content=ft.Column(
                                    spacing=10,
                                    horizontal_alignment="center",

                                    controls=[

                                        ft.Text(
                                            "Información de la cuenta",
                                            size=24,
                                            weight="bold",
                                            color="#57689E"
                                        ),

                                        ft.Divider(),

                                        ft.Text(
                                            "📧 Email: {}".format(
                                                user_data.get("email", "")
                                            ),
                                            size=16
                                        ),

                                        ft.Text(
                                            "🆔 ID Usuario: {}".format(
                                                user_data.get("id_usuario", "")
                                            ),
                                            size=16
                                        ),

                                        ft.Text(
                                            "📅 Fecha registro: {}".format(
                                                user_data.get("fecha_registro", "")
                                            ),
                                            size=16
                                        ),

                                        ft.Container(height=10),

                                        ft.ElevatedButton(
                                            "Cerrar Sesión",
                                            on_click=cerrar_sesion,
                                            bgcolor="#57689E",
                                            color="white",
                                            width=220,
                                            height=45
                                        )
                                    ]
                                )
                            )
                        )
                    ]
                )
            )
        ]
    )
