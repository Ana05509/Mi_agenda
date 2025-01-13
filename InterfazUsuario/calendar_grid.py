import wx
import wx.grid
from models.event_model import EventModel
from ui.add_event_dialog import AddEventDialog

class CalendarGrid(wx.Panel):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self.event_model = EventModel()
        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(6, 7)  # 6 filas (semanales), 7 columnas (días de la semana)

        # Configurar la visualización básica
        self.setup_grid()
        self.load_events()

        # Bind eventos de clic en celda
        self.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_cell_dclick)

    def setup_grid(self):
        for row in range(6):
            for col in range(7):
                self.grid.SetCellValue(row, col, "")
        
        self.grid.AutoSize()
        self.grid.SetRowLabelSize(0)  # Eliminar la etiqueta de fila
        self.grid.SetColLabelSize(0)  # Eliminar la etiqueta de columna
        self.grid.SetGridLineColour("WHITE")  # Cambiar el color de las líneas
        self.grid.SetDefaultCellBackgroundColour("WHITE")  # Cambiar el color de fondo de celda por defecto
        self.grid.SetDefaultCellTextColour("BLACK")  # Cambiar el color de texto de celda por defecto
        self.grid.SetDefaultCellFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

    def load_events(self):
        events = self.event_model.get_events()
        for event in events:
            # Aquí puedes agregar lógica para colocar los eventos en las celdas correctas
            # Por ejemplo, podrías usar la fecha del evento para determinar la celda
            pass

    def on_cell_dclick(self, event):
        row = event.GetRow()
        col = event.GetCol()
        date = self.get_date_from_cell(row, col)
        dialog = AddEventDialog(self, user=self.user)
        if dialog.ShowModal() == wx.ID_OK:
            event_name = dialog.event_name_text.GetValue()
            event_date = dialog.event_date_picker.GetValue().FormatISODate()
            self.event_model.create_event(event_name, event_date)
            self.load_events()
        dialog.Destroy()

    def get_date_from_cell(self, row, col):
        # Aquí puedes agregar lógica para obtener la fecha correspondiente a una celda
        # Por ejemplo, podrías usar el número de fila y columna para calcular la fecha
        return "2023-01-01"  # Ejemplo de fecha

if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, title="Calendario", size=(800, 600))
    panel = CalendarGrid(frame, user="current_user")
    frame.Show()
    app.MainLoop()
