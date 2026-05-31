import flet as ft

def MetasView(page: ft.Page, user_data, auth_controller):

    def volver_menu(e):
        page.views.pop()
        page.update()

    nombre_meta = ft.TextField(
        label="Nombre de la meta",
        width=300,
        bgcolor="#F0F0F0",
        border_radius=10,
    )

    monto_objetivo = ft.TextField(
        label="Monto objetivo (USD)",
        width=300,
        bgcolor="#F0F0F0",
        border_radius=10,
    )

    monto_actual = ft.TextField(
        label="Monto actual (USD)",
        width=300,
        bgcolor="#F0F0F0",
        border_radius=10,
        value="0",
    )

    mensaje = ft.Text("", color="red")

    tabla_metas = ft.DataTable(
        width=800,
        columns=[
            ft.DataColumn(ft.Text("Meta", weight="bold")),
            ft.DataColumn(ft.Text("Objetivo", weight="bold")),
            ft.DataColumn(ft.Text("Actual", weight="bold")),
            ft.DataColumn(ft.Text("Progreso", weight="bold")),
            ft.DataColumn(ft.Text("Acción", weight="bold")),
        ],
        rows=[],
    )

    def cargar_metas():
        metas = auth_controller.obtener_metas_usuario(user_data['id_usuario'])
        tabla_metas.rows.clear()
        
        for meta in metas:
            id_meta = meta['id_meta']
            monto_obj = float(meta['monto_objetivo'])
            monto_act = float(meta['monto_actual'])
            progreso = (monto_act / monto_obj * 100) if monto_obj > 0 else 0
            
            progress_bar = ft.ProgressBar(value=progreso/100, width=150, height=10)
            progreso_texto = ft.Text(f"{progreso:.1f}%", size=12)
            
            tabla_metas.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(meta['nombre_meta'], weight="bold")),
                        ft.DataCell(ft.Text(f"${monto_obj:,.2f}")),
                        ft.DataCell(
                            ft.TextField(
                                value=f"{monto_act:,.2f}",
                                width=120,
                                height=40,
                                text_align=ft.TextAlign.RIGHT,
                                on_submit=lambda e, id_m=id_meta: actualizar_monto(id_m, e.control.value),
                            )
                        ),
                        ft.DataCell(ft.Column([progress_bar, progreso_texto], spacing=5)),
                        ft.DataCell(
                            ft.ElevatedButton(
                                "Eliminar",
                                bgcolor="red",
                                color="white",
                                width=80,
                                height=30,
                                on_click=lambda e, id_m=id_meta: eliminar_meta(id_m),
                            )
                        ),
                    ]
                )
            )
        page.update()

    def guardar_meta(e):
        if not nombre_meta.value or not monto_objetivo.value:
            mensaje.value = "Nombre y monto objetivo son obligatorios"
            mensaje.color = "red"
            page.update()
            return
        
        try:
            monto_obj = float(monto_objetivo.value)
            monto_act = float(monto_actual.value) if monto_actual.value else 0
            
            success, msg = auth_controller.guardar_meta(
                user_data['id_usuario'],
                nombre_meta.value,
                monto_obj,
                monto_act,
                None
            )
            
            mensaje.value = msg
            mensaje.color = "green" if success else "red"
            
            if success:
                nombre_meta.value = ""
                monto_objetivo.value = ""
                monto_actual.value = "0"
                cargar_metas()
            
            page.update()
        except ValueError:
            mensaje.value = "Ingrese montos válidos"
            mensaje.color = "red"
            page.update()

    def actualizar_monto(id_meta, nuevo_monto_str):
        try:
            nuevo_monto = float(nuevo_monto_str.replace(",", ""))
            success, msg = auth_controller.actualizar_meta(id_meta, nuevo_monto, "En progreso")
            
            if success:
                mensaje.value = msg
                mensaje.color = "green"
                cargar_metas()
            else:
                mensaje.value = msg
                mensaje.color = "red"
            page.update()
        except ValueError:
            mensaje.value = "Monto inválido"
            mensaje.color = "red"
            page.update()

    def eliminar_meta(id_meta):
        # Eliminar directamente sin diálogo como en calculadora
        success, msg = auth_controller.eliminar_meta(id_meta, user_data['id_usuario'])
        
        if success:
            cargar_metas()
            mensaje.value = msg
            mensaje.color = "green"
        else:
            mensaje.value = msg
            mensaje.color = "red"
        
        page.update()

    cargar_metas()

    return ft.View(
        route="/metas",
        bgcolor="#EAF0FF",
        padding=0,
        controls=[
            ft.Container(
                bgcolor="#57689E",
                padding=20,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text("FinanCO - Metas Financieras", size=28, weight="bold", color="white"),
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
                            "Metas Financieras",
                            size=35,
                            weight="bold",
                            color="#2D3E6F"
                        ),
                        ft.Text(
                            "Define tus metas y sigue tu progreso",
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
                                        nombre_meta,
                                        monto_objetivo,
                                        monto_actual,
                                        ft.ElevatedButton(
                                            "Guardar Meta",
                                            on_click=guardar_meta,
                                            bgcolor="#4CAF50",
                                            color="white",
                                            width=200,
                                        ),
                                        mensaje,
                                    ]
                                )
                            )
                        ),
                        ft.Divider(height=20, color="transparent"),
                        ft.Text(
                            "Mis Metas",
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
                                controls=[tabla_metas]
                            )
                        ),
                        ft.Container(height=30),
                    ]
                )
            )
        ]
    )