import wx
from ui.calendar_grid import CalendarGrid
from ui.add_event_dialog import AddEventDialog
from controllers.event_controller import EventController

class MainFrame(wx.Frame):
    def __init__(self, parent, user, *args, **kw):
        super(MainFrame, self).__init__(parent, *args, **kw)

        self.user = user
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Crear el calendario
        self.calendar_grid = CalendarGrid(self.panel, self.user)
        self.sizer.Add(self.calendar_grid, 1, flag=wx.EXPAND)

        # Agregar botón para añadir evento
        self.add_event_button = wx.Button(self.panel, label="Agregar Evento")
        self.add_event_button.Bind(wx.EVT_BUTTON, self.on_add_event)
        self.sizer.Add(self.add_event_button, 0, flag=wx.EXPAND | wx.ALL, border=5)

        self.panel.SetSizer(self.sizer)

    def on_add_event(self, event):
        dialog = AddEventDialog(self, user=self.user)
        if dialog.ShowModal() == wx.ID_OK:
            self.calendar_grid.load_events()
        dialog.Destroy()