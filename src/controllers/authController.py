class AuthController:

    def __init__(self, auth_model):
        self.auth_model = auth_model

    def login(self, correo, contraseña):

        usuario = self.auth_model.login(correo, contraseña)

        if usuario:
            return usuario, "Login correcto"

        return None, "Correo o contraseña incorrectos"

    def recover_password(self, correo):

        usuario = self.auth_model.verificar_correo(correo)

        if usuario:
            return True, "Correo encontrado"

        return False, "Correo no existe"