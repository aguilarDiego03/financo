import flet as ft


def ResetPasswordView(page: ft.Page, auth_controller):

    nueva_password = ft.TextField(
        label="Nueva contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
    )

    confirmar_password = ft.TextField(
        label="Confirmar contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
    )

    mensaje = ft.Text("", color="red")

    def cambiar_password(e):
        if not nueva_password.value or not confirmar_password.value:
            mensaje.value = "Complete todos los campos"
            page.update()
            return

        if nueva_password.value != confirmar_password.value:
            mensaje.value = "Las contraseñas no coinciden"
            page.update()
            return

        correo = page.recovery_email
        success, msg = auth_controller.reset_password(
            correo,
            nueva_password.value
        )

        if success:
            mensaje.color = "green"
            mensaje.value = msg
            page.update()
            page.go("/")

        else:
            mensaje.color = "red"
            mensaje.value = msg
            page.update()

    return ft.View(
        route="/reset-password",
        bgcolor="#57689E",
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Column(
                [
                    ft.Text(
                        "Nueva contraseña",
                        size=30,
                        weight="bold",
                        color="white",
                    ),
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    nueva_password,
                                    confirmar_password,
                                    mensaje,
                                    ft.ElevatedButton(
                                        "Guardar contraseña",
                                        on_click=cambiar_password,
                                    ),
                                ],
                                spacing=15,
                            ),
                            padding=30,
                            bgcolor="white",
                        )
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]
    )