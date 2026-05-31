from models.UsuariosModel import UsuarioModel


class AuthController:

    def __init__(self):

        self.usuario_model = UsuarioModel()


    def login(self, email, password):

        try:

            user_db = self.usuario_model.validar_login(
                email,
                password
            )

            if not user_db:

                return None, "Correo o contraseña incorrectos"

            user = {
                "id_usuario": user_db["id_usuario"],
                "nombre": user_db["nombre"],
                "email": user_db["correo"],
                "fecha_registro": user_db["fecha_registro"],
            }

            return user, "Login exitoso"

        except Exception as e:

            return None, f"Error en login: {str(e)}"


    def registrar(self, usuario_data):

        try:

            if self.usuario_model.email_existe(
                usuario_data.email
            ):

                return (
                    False,
                    "El correo electrónico ya está registrado"
                )

            exito = self.usuario_model.registrar(
                usuario_data
            )

            if exito:

                return (
                    True,
                    "Usuario registrado exitosamente"
                )

            else:

                return (
                    False,
                    "Error al registrar usuario"
                )

        except Exception as e:

            return (
                False,
                f"Error en registro: {str(e)}"
            )



    def recover_password(self, correo):

        try:

            usuario = self.usuario_model.verificar_correo(
                correo
            )

            if usuario:

                return True, "Correo encontrado"

            return False, "Correo no existe"

        except Exception as e:

            return (
                False,
                f"Error: {str(e)}"
            )
    def reset_password(self, correo, nueva_password):

        try:

            self.usuario_model.actualizar_password(
                correo,
                nueva_password
            )

            return True, "Contraseña actualizada"

        except Exception as e:

            return False, f"Error: {str(e)}"


    def calcular_rendimiento(self, monto_inicial, porcentaje, meses):
        try:
            monto = float(monto_inicial)
            interes = float(porcentaje)
            tiempo = int(meses)
            
            rendimiento = monto * (1 + (interes / 100) * (tiempo / 12))
            return round(rendimiento, 2)
        except Exception as e:
            return None

    def guardar_calculo(self, id_usuario, monto_inicial, porcentaje_interes, tiempo_meses):
        try:
            rendimiento_final = self.calcular_rendimiento(monto_inicial, porcentaje_interes, tiempo_meses)
            
            if rendimiento_final is None:
                return False, "Error en el cálculo"
            
            self.usuario_model.guardar_calculo(
                id_usuario, 
                monto_inicial, 
                porcentaje_interes, 
                tiempo_meses, 
                rendimiento_final
            )
            return True, "Cálculo guardado exitosamente"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def obtener_calculos_usuario(self, id_usuario):
        try:
            return self.usuario_model.obtener_calculos_usuario(id_usuario)
        except Exception as e:
            return []

    def eliminar_calculo(self, id_calculo, id_usuario):
        try:
            self.usuario_model.eliminar_calculo(id_calculo, id_usuario)
            return True, "Cálculo eliminado exitosamente"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def guardar_meta(self, id_usuario, nombre_meta, monto_objetivo, monto_actual, fecha_limite):
        try:
            self.usuario_model.guardar_meta(id_usuario, nombre_meta, monto_objetivo, monto_actual, fecha_limite)
            return True, "Meta guardada exitosamente"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def obtener_metas_usuario(self, id_usuario):
        try:
            return self.usuario_model.obtener_metas_usuario(id_usuario)
        except Exception as e:
            return []

    def actualizar_meta(self, id_meta, monto_actual, estado):
        try:
            self.usuario_model.actualizar_meta(id_meta, monto_actual, estado)
            return True, "Meta actualizada"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def eliminar_meta(self, id_meta, id_usuario):
        try:
            self.usuario_model.eliminar_meta(id_meta, id_usuario)
            return True, "Meta eliminada"
        except Exception as e:
            return False, f"Error: {str(e)}"