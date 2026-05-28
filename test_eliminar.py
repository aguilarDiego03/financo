from controllers.UsuariosController import AuthController

ctrl = AuthController()

# Probar eliminar cálculo ID 2 para usuario 1
id_calculo = 2
id_usuario = 1  # Cambia esto por el ID del usuario que está logueado

print(f"Intentando eliminar cálculo ID: {id_calculo}, usuario: {id_usuario}")

# Obtener cálculos antes
calculos_antes = ctrl.obtener_calculos_usuario(id_usuario)
print(f"Cálculos antes: {len(calculos_antes)}")

# Eliminar
success, msg = ctrl.eliminar_calculo(id_calculo, id_usuario)
print(f"Resultado: {success}, Mensaje: {msg}")

# Obtener cálculos después
calculos_despues = ctrl.obtener_calculos_usuario(id_usuario)
print(f"Cálculos después: {len(calculos_despues)}")