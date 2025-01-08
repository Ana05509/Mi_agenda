import wx
from controllers.auth_controller import AuthController
from ui.register_dialog import RegisterDialog
import os


class LoginDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Bienvenido a Mi Agenda", size=(500, 500), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.auth_controller = AuthController()

        # Panel principal
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Encabezado con imagen
        header_sizer = wx.BoxSizer(wx.VERTICAL)

        # Agregar imagen (reemplaza "logo.png" por el path de tu imagen)
        try:
            image_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'logo.png')
            image = wx.Image(image_path, wx.BITMAP_TYPE_PNG).Scale(100, 100).ConvertToBitmap()
            self.image_ctrl = wx.StaticBitmap(self.panel, bitmap=image)
            header_sizer.Add(self.image_ctrl, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")  # Imprimir el error si la imagen no se carga

        # Texto de bienvenida
        header_text = wx.StaticText(self.panel, label="Bienvenido a Mi Agenda")
        font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        header_text.SetFont(font)
        header_sizer.Add(header_text, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.sizer.Add(header_sizer, 0, wx.EXPAND)

        # Campos de inicio de sesión
        form_sizer = wx.BoxSizer(wx.VERTICAL)

        self.username_label = wx.StaticText(self.panel, label="Usuario:")
        self.username_text = wx.TextCtrl(self.panel, size=(300, -1))

        self.password_label = wx.StaticText(self.panel, label="Contraseña:")
        self.password_text = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD, size=(300, -1))

        form_sizer.Add(self.username_label, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        form_sizer.Add(self.username_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        form_sizer.Add(self.password_label, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        form_sizer.Add(self.password_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Botones
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.login_button = wx.Button(self.panel, label="Iniciar Sesión", size=(150, 50))
        self.register_button = wx.Button(self.panel, label="Registrarse", size=(150, 50))
        self.login_button.Bind(wx.EVT_BUTTON, self.on_login)
        self.register_button.Bind(wx.EVT_BUTTON, self.on_register)

        button_sizer.Add(self.login_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        button_sizer.Add(self.register_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        form_sizer.Add(button_sizer, 0, wx.ALIGN_CENTER)

        self.sizer.Add(form_sizer, 1, wx.EXPAND | wx.ALL, 10)

        self.panel.SetSizer(self.sizer)

    def on_login(self, event):
        username = self.username_text.GetValue()
        password = self.password_text.GetValue()

        if self.auth_controller.validate_credentials(username, password):
            wx.MessageBox("Inicio de sesión exitoso", "Información", wx.OK | wx.ICON_INFORMATION)
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox("Usuario o contraseña incorrectos", "Error", wx.OK | wx.ICON_ERROR)

    def on_register(self, event):
        register_dialog = RegisterDialog(self)
        register_dialog.ShowModal()
        register_dialog.Destroy()


class RegisterDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Registrar Usuario", size=(400, 400))

        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Encabezado
        header_text = wx.StaticText(self.panel, label="Registrar Nuevo Usuario")
        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        header_text.SetFont(font)

        self.sizer.Add(header_text, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        # Campos de registro
        form_sizer = wx.BoxSizer(wx.VERTICAL)

        self.username_label = wx.StaticText(self.panel, label="Usuario:")
        self.username_text = wx.TextCtrl(self.panel)

        self.password_label = wx.StaticText(self.panel, label="Contraseña:")
        self.password_text = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)

        form_sizer.Add(self.username_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.username_text, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.password_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.password_text, 0, wx.EXPAND | wx.ALL, 5)

        self.sizer.Add(form_sizer, 1, wx.EXPAND | wx.ALL, 10)

        # Botones
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.register_button = wx.Button(self.panel, label="Registrar")
        self.cancel_button = wx.Button(self.panel, label="Regresar")

        self.register_button.Bind(wx.EVT_BUTTON, self.on_register)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)

        button_sizer.Add(self.register_button, 1, wx.EXPAND | wx.ALL, 5)
        button_sizer.Add(self.cancel_button, 1, wx.EXPAND | wx.ALL, 5)

        self.sizer.Add(button_sizer, 0, wx.ALIGN_CENTER)

        self.panel.SetSizer(self.sizer)

    def on_register(self, event):
        username = self.username_text.GetValue()
        password = self.password_text.GetValue()

        if username and password:
            # Aquí puedes agregar lógica para guardar al usuario
            wx.MessageBox("Usuario registrado exitosamente", "Información", wx.OK | wx.ICON_INFORMATION)
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox("Todos los campos son obligatorios", "Error", wx.OK | wx.ICON_ERROR)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)


# Punto de entrada
if __name__ == "__main__":
    app = wx.App(False)
    login_dialog = LoginDialog(None)
    login_dialog.ShowModal()
    login_dialog.Destroy()
    app.MainLoop()
