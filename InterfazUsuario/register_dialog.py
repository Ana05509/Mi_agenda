import wx
from controllers.auth_controller import AuthController

class RegisterDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Registrar Usuario", size=(300, 250))

        self.auth_controller = AuthController()
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Campos de registro
        self.username_label = wx.StaticText(self.panel, label="Usuario")
        self.username_text = wx.TextCtrl(self.panel)
        
        self.password_label = wx.StaticText(self.panel, label="Contraseña")
        self.password_text = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)

        self.confirm_password_label = wx.StaticText(self.panel, label="Confirmar Contraseña")
        self.confirm_password_text = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)

        self.sizer.Add(self.username_label, 0, flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.username_text, 0, flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.password_label, 0, flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.password_text, 0, flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.confirm_password_label, 0, flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.confirm_password_text, 0, flag=wx.EXPAND | wx.ALL, border=5)

        # Botones
        self.register_button = wx.Button(self.panel, label="Registrarse")
        self.register_button.Bind(wx.EVT_BUTTON, self.on_register)

        self.sizer.Add(self.register_button, 0, flag=wx.EXPAND | wx.ALL, border=5)

        self.panel.SetSizer(self.sizer)

    def on_register(self, event):
        username = self.username_text.GetValue()
        password = self.password_text.GetValue()
        confirm_password = self.confirm_password_text.GetValue()

        if password != confirm_password:
            wx.MessageBox("Las contraseñas no coinciden", "Error", wx.OK | wx.ICON_ERROR)
            return

        try:
            self.auth_controller.add_user(username, password)
            wx.MessageBox("Usuario registrado exitosamente", "Información", wx.OK | wx.ICON_INFORMATION)
            self.EndModal(wx.ID_OK)
        except ValueError as e:
            wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
            self.password_text.Clear() # Borrar campos de contraseña
            
        