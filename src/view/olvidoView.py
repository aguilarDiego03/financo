import flet as ft


def OlvidoView(page: ft.Page, auth_controller):
    correo = ft.TextField(
        label="Correo electrónico",
        width=350,
        bgcolor="#F0F0F0",
        border_radius=10,
    )

    mensaje = ft.Text("", color="red")

    def recuperar_click(e):
        if not correo.value:
            mensaje.value = "Ingrese un correo"
            page.update()
            return

        success, msg = auth_controller.recover_password(
            correo.value
        )

        if success:
            page.recovery_email = correo.value
            page.go("/reset-password")

        else:
            mensaje.color = "red"
            mensaje.value = msg

        page.update()

    btn_recuperar = ft.ElevatedButton(
        "Recuperar contraseña",
        width=200,
        bgcolor="#57689E",
        color=ft.Colors.WHITE,
        on_click=recuperar_click,
    )

    btn_volver = ft.TextButton(
        "Volver al login",
        on_click=lambda _: page.go("/"),
    )

    return ft.View(
        route="/forgot-password",
        bgcolor="#57689E",
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Column(
                [
                    ft.Text(
                        "Recuperar contraseña",
                        size=30,
                        weight="bold",
                        color=ft.Colors.WHITE,
                    ),

                    ft.Container(height=30),

                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    correo,
                                    mensaje,
                                    btn_recuperar,
                                    btn_volver,
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