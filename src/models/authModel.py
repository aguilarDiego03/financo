class AuthModel:

    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    # LOGIN
    def login(self, correo, contraseña):

        query = """
        SELECT * FROM usuarios
        WHERE correo = %s AND contraseña = %s
        """

        self.cursor.execute(query, (correo, contraseña))

        return self.cursor.fetchone()

    # RECUPERAR PASSWORD
    def verificar_correo(self, correo):

        query = """
        SELECT * FROM usuarios
        WHERE correo = %s
        """

        self.cursor.execute(query, (correo,))

        return self.cursor.fetchone()