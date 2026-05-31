import flet as ft

def CalculadoraView(page: ft.Page, user_data, auth_controller):

    def volver_menu(e):
        page.views.pop()
        page.update()

    monto_input = ft.TextField(
        label="Monto inicial (USD)",
        width=300,
        bgcolor="#F0F0F0",
        border_radius=10,
    )

    porcentaje_input = ft.TextField(
        label="Porcentaje de interés (%)",
        width=300,
        bgcolor="#F0F0F0",
        border_radius=10,
    )

    meses_input = ft.TextField(
        label="Tiempo (meses)",
        width=300,
        bgcolor="#F0F0F0",
        border_radius=10,
    )

    resultado_texto = ft.Text("", size=18, color="#2D3E6F", weight="bold")
    mensaje = ft.Text("", color="red")

    tabla_calculos = ft.DataTable(
        width=900,
        columns=[
            ft.DataColumn(ft.Text("Monto", weight="bold")),
            ft.DataColumn(ft.Text("Interés", weight="bold")),
            ft.DataColumn(ft.Text("Meses", weight="bold")),
            ft.DataColumn(ft.Text("Rendimiento", weight="bold")),
            ft.DataColumn(ft.Text("Fecha", weight="bold")),
            ft.DataColumn(ft.Text("Acción", weight="bold")),
        ],
        rows=[],
    )

    def cargar_calculos():
        calculos = auth_controller.obtener_calculos_usuario(user_data['id_usuario'])
        tabla_calculos.rows.clear()
        
        for calc in calculos:
            id_calc = calc['id_calculo']
            
            tabla_calculos.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(f"${calc['monto_inicial']:,.2f}")),
                        ft.DataCell(ft.Text(f"{calc['porcentaje_interes']}%")),
                        ft.DataCell(ft.Text(str(calc['tiempo_meses']))),
                        ft.DataCell(ft.Text(f"${calc['rendimiento_final']:,.2f}", color="green", weight="bold")),
                        ft.DataCell(ft.Text(str(calc['fecha_calculo'])[:10])),
                        ft.DataCell(
                            ft.ElevatedButton(
                                "Eliminar",
                                bgcolor="red",
                                color="white",
                                width=80,
                                height=30,
                                on_click=lambda e, id_c=id_calc: eliminar_calculo(id_c),
                            )
                        ),
                    ]
                )
            )
        page.update()

    def eliminar_calculo(id_calculo):
        success, msg = auth_controller.eliminar_calculo(id_calculo, user_data['id_usuario'])
        
        if success:
            cargar_calculos()
            mensaje.value = msg
            mensaje.color = "green"
        else:
            mensaje.value = msg
            mensaje.color = "red"
        
        page.update()

    def calcular_click(e):
        try:
            monto = float(monto_input.value)
            porcentaje = float(porcentaje_input.value)
            meses = int(meses_input.value)

            rendimiento = auth_controller.calcular_rendimiento(monto, porcentaje, meses)
            
            if rendimiento:
                ganancia = rendimiento - monto
                resultado_texto.value = f"Rendimiento total: ${rendimiento:,.2f} (Ganancia: ${ganancia:,.2f})"
                mensaje.value = ""
            else:
                resultado_texto.value = ""
                mensaje.value = "Error en el cálculo"
            
            page.update()
        except ValueError:
            mensaje.value = "Por favor, ingrese valores válidos"
            resultado_texto.value = ""
            page.update()

    def guardar_click(e):
        try:
            monto = float(monto_input.value)
            porcentaje = float(porcentaje_input.value)
            meses = int(meses_input.value)
            
            success, msg = auth_controller.guardar_calculo(user_data['id_usuario'], monto, porcentaje, meses)
            mensaje.value = msg
            mensaje.color = "green" if success else "red"
            
            if success:
                cargar_calculos()  
                monto_input.value = ""
                porcentaje_input.value = ""
                meses_input.value = ""
                resultado_texto.value = ""
            
            page.update()
        except Exception as ex:
            mensaje.value = f"Error: {str(ex)}"
            mensaje.color = "red"
            page.update()

    cargar_calculos()

    return ft.View(
        route="/calculadora",
        bgcolor="#EAF0FF",
        padding=0,
        controls=[
            ft.Container(
                bgcolor="#57689E",
                padding=20,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text("FinanceApp - Calculadora de Rendimiento", size=28, weight="bold", color="white"),
                        ft.TextButton("Volver al Inicio", on_click=volver_menu, style=ft.ButtonStyle(color="white")),
                    ]
                )
            ),
            ft.Container(
                expand=True,
                padding=30,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=25,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Text(
                            "Calculadora de Rendimiento",
                            size=35,
                            weight="bold",
                            color="#2D3E6F"
                        ),
                        ft.Text(
                            "Calcula cuánto ganarías al invertir tu dinero",
                            size=18,
                            color="#555555",
                        ),
                        ft.Card(
                            elevation=8,
                            content=ft.Container(
                                width=600,
                                padding=30,
                                bgcolor="white",
                                border_radius=20,
                                content=ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=20,
                                    controls=[
                                        monto_input,
                                        porcentaje_input,
                                        meses_input,
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                ft.ElevatedButton(
                                                    "Calcular",
                                                    on_click=calcular_click,
                                                    bgcolor="#57689E",
                                                    color="white",
                                                    width=150,
                                                ),
                                                ft.ElevatedButton(
                                                    "Guardar Cálculo",
                                                    on_click=guardar_click,
                                                    bgcolor="#4CAF50",
                                                    color="white",
                                                    width=150,
                                                ),
                                            ]
                                        ),
                                        resultado_texto,
                                        mensaje,
                                    ]
                                )
                            )
                        ),
                        ft.Divider(height=20, color="transparent"),
                        ft.Text(
                            "Historial de Cálculos",
                            size=25,
                            weight="bold",
                            color="#2D3E6F"
                        ),
                        ft.Container(
                            width=1000,
                            padding=20,
                            bgcolor="white",
                            border_radius=15,
                            content=ft.Column(
                                scroll=ft.ScrollMode.AUTO,
                                controls=[tabla_calculos]
                            )
                        ),
                        ft.Container(height=30),
                    ]
                )
            )
        ]
    )