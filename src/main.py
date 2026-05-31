import flet as ft
from controllers.UsuariosController import AuthController
from view.LoginView import LoginView
from view.RegisterView import RegisterView  
from view.MenuView import MenuView  
from view.olvidoView import OlvidoView
from view.ResetPasswordView import ResetPasswordView
from view.verificadorView import VerificadorView
from view.MetasView import MetasView

def start(page: ft.Page):
    page.title = "FinanCO"
    page.bgcolor = "#57689E" 
    
    auth_ctrl = AuthController()

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/register": 
            page.views.append(RegisterView(page, auth_ctrl))
        elif page.route == "/menu":  
            user_data = getattr(page, "user_data", None)
            if user_data:
                page.views.append(MenuView(page, user_data, auth_ctrl))
            else:
                page.go("/")
        elif page.route == "/forgot-password":
            page.views.append(OlvidoView(page, auth_ctrl))
        elif page.route == "/reset-password":
            page.views.append(ResetPasswordView(page, auth_ctrl))
        elif page.route == "/verify-otp":
            page.views.append(VerificadorView(page))
        elif page.route == "/metas":
            user_data = getattr(page, "user_data", None)
            if user_data:
                page.views.append(MetasView(page, user_data, auth_ctrl))
            else:
                page.go("/")
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error: Ruta no encontrada")], bgcolor="#57689E")
            )
        page.update()
        
    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
            
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    if page.route == "/":
        route_change(None)
    else:
        page.go("/")
    
def main():
    ft.app(start)

if __name__ == "__main__":
    main()