import bcrypt
from .databaseModel import Database


class UsuarioModel:

    def __init__(self):
        self.db = Database()


    def email_existe(self, email):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = "SELECT id_usuario FROM usuarios WHERE correo = %s"
        cursor.execute(query, (email,))
        existe = cursor.fetchone() is not None
        conn.close()
        return existe


    def registrar(self, usuario_data):

        salt = bcrypt.gensalt()

        hashed_pw = bcrypt.hashpw(
            usuario_data.password.encode("utf-8"),
            salt
        )

        conn = self.db.get_connection()

        cursor = conn.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO usuarios
                (nombre, correo, contraseña)
                VALUES (%s, %s, %s)
                """,
                (
                    usuario_data.nombre,
                    usuario_data.email,
                    hashed_pw.decode("utf-8")
                )
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()


    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE correo = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.checkpw(
            password.encode("utf-8"),
            user["contraseña"].encode("utf-8")
        ):

            return user

        return None



    def verificar_correo(self, correo):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE correo = %s"
        cursor.execute(query, (correo,))
        usuario = cursor.fetchone()
        conn.close()
        return usuario



    def obtener_por_id(self, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE id_usuario = %s"
        cursor.execute(query, (id_usuario,))
        user = cursor.fetchone()
        conn.close()
        return user
    
    def actualizar_password(self, correo, nueva_password):

        salt = bcrypt.gensalt()

        hashed_pw = bcrypt.hashpw(
            nueva_password.encode("utf-8"),
            salt
        )

        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE usuarios
        SET contraseña = %s
        WHERE correo = %s
        """

        cursor.execute(
            query,
            (
                hashed_pw.decode("utf-8"),
                correo
            )
        )

        conn.commit()

        conn.close()

        return True


    def guardar_calculo(self, id_usuario, monto_inicial, porcentaje_interes, tiempo_meses, rendimiento_final):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        query = """
        INSERT INTO calculos_rendimiento 
        (id_usuario, monto_inicial, porcentaje_interes, tiempo_meses, rendimiento_final)
        VALUES (%s, %s, %s, %s, %s)
        """
        
        cursor.execute(query, (id_usuario, monto_inicial, porcentaje_interes, tiempo_meses, rendimiento_final))
        conn.commit()
        conn.close()
        return True

    def obtener_calculos_usuario(self, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
        SELECT id_calculo, monto_inicial, porcentaje_interes, tiempo_meses, 
            rendimiento_final, fecha_calculo
        FROM calculos_rendimiento 
        WHERE id_usuario = %s
        ORDER BY fecha_calculo DESC
        """
        
        cursor.execute(query, (id_usuario,))
        calculos = cursor.fetchall()
        conn.close()
        return calculos

    def eliminar_calculo(self, id_calculo, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        query = "DELETE FROM calculos_rendimiento WHERE id_calculo = %s AND id_usuario = %s"
        cursor.execute(query, (id_calculo, id_usuario))
        conn.commit()
        conn.close()
        return True