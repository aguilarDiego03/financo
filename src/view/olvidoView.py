import flet as ft
import random
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def OlvidoView(page: ft.Page, auth_controller):

    correo = ft.TextField(
        label="Correo electronico",
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

        if not success:

            mensaje.value = msg

            page.update()

            return

        codigo = random.randint(100000, 999999)

        remitente = "supercubano3.0@gmail.com"

        password = "ixiz smfg dqji ghrr"

        email = MIMEMultipart()

        email["From"] = remitente
        email["To"] = correo.value
        email["Subject"] = "Recuperacion de contrasena"

        cuerpo = f"""
    Hola.

    Tu codigito es:

    {codigo}

    Ignora este correo si no lo solicitaste.
    """

        email.attach(
            MIMEText(cuerpo, "plain")
        )

        print("Codigito:", codigo)
        print("Destino:", correo.value)

        servidor = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        servidor.starttls()

        servidor.login(
            remitente,
            password
        )

        servidor.send_message(email)

        servidor.quit()

        page.otp_code = str(codigo)

        page.recovery_email = correo.value

        page.go("/verify-otp")
    btn_recuperar = ft.ElevatedButton(
        "Recuperar contrasena",
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
                        "Recuperar contrasena",
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