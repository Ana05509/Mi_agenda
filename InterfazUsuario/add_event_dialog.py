import wx
from models.event_model import EventModel

class AddEventDialog(wx.Dialog):
    def __init__(self, parent, user):
        super().__init__(parent, title="Agregar Evento", size=(300, 250))

        self.user = user
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Campos del evento
        self.event_name_label = wx.StaticText(self.panel, label="Nombre del Evento")
        self.event_name_text = wx.TextCtrl(self.panel)
        
        self.event_date_label = wx.StaticText(self.panel, label="Fecha")
        self.event_date_picker = wx.DatePickerCtrl(self.panel)

        self.sizer.Add(self.event_name_label, 0, flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.event_name_text, 0, flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.event_date_label, 0, flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.event_date_picker, 0, flag=wx.EXPAND | wx.ALL, border=5)

        # Botones
        self.ok_button = wx.Button(self.panel, label="Aceptar")
        self.cancel_button = wx.Button(self.panel, label="Cancelar")
        self.ok_button.Bind(wx.EVT_BUTTON, self.on_ok)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)

        self.sizer.Add(self.ok_button, 0, flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.cancel_button, 0, flag=wx.EXPAND | wx.ALL, border=5)

        self.panel.SetSizer(self.sizer)

    def on_ok(self, event):
        event_name = self.event_name_text.GetValue()
        event_date = self.event_date_picker.GetValue().FormatISODate()
        
        if event_name and event_date:
            event_model = EventModel()
            event_model.create_event(event_name, event_date)
            wx.MessageBox("Evento creado exitosamente", "Información", wx.OK | wx.ICON_INFORMATION)
            self.Close()
        else:
            wx.MessageBox("Por favor, complete todos los campos", "Error", wx.OK | wx.ICON_ERROR)

    def on_cancel(self, event):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    dialog = AddEventDialog(None, user="test_user")
    dialog.ShowModal()
    app.MainLoop()