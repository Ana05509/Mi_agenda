import wx.adv
from ui.main_frame import MainFrame
from ui.login_dialog import LoginDialog

def run_app():
    app = wx.App(False)
    
    login_dialog = LoginDialog(None)
    if login_dialog.ShowModal() == wx.ID_OK:
        user = login_dialog.username_text.GetValue()
        login_dialog.Destroy()  # Asegúrate de destruir el diálogo después de obtener el usuario
        frame = MainFrame(None, user=user, title="Mi Calendario", size=(800, 600))
        frame.Show()
        app.MainLoop()
    else:
        wx.MessageBox("Debe iniciar sesión para usar la aplicación", "Error", wx.OK | wx.ICON_ERROR)
        app.Exit()

if __name__ == "__main__":
    run_app()