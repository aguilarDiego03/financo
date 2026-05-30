import flet as ft


def VerificadorView(page: ft.Page):

    codigo = ft.TextField(
        label="Codigo de seguridad",
        width=350,
        bgcolor="#F0F0F0",
        border_radius=10,
        max_length=6,
    )

    mensaje = ft.Text("", color="red")

    def verificar_click(e):

        if not codigo.value:

            mensaje.value = "Ingrese el codigo"

            page.update()

            return

        if codigo.value == page.otp_code:

            page.go("/reset-password")

        else:

            mensaje.value = "Codigo incorrecto"

            page.update()

    return ft.View(
        route="/verify-otp",
        bgcolor="#57689E",
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Column(
                [
                    ft.Text(
                        "Verificar codigo",
                        size=30,
                        weight="bold",
                        color=ft.Colors.WHITE,
                    ),

                    ft.Container(height=20),

                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(
                                        "Ingresa el codigo enviado a tu correo"
                                    ),

                                    codigo,

                                    mensaje,

                                    ft.ElevatedButton(
                                        "Verificar",
                                        width=200,
                                        bgcolor="#57689E",
                                        color=ft.Colors.WHITE,
                                        on_click=verificar_click,
                                    ),

                                    ft.TextButton(
                                        "Volver",
                                        on_click=lambda _: page.go("/forgot-password")
                                    )
                                ],
                                spacing=15,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            padding=30,
                            bgcolor=ft.Colors.WHITE,
                        ),
                        elevation=5,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]
    )