import wx


class ConfigEditor(wx.Panel):

    def __init__(self, parent):
        super(ConfigEditor, self).__init__(parent=parent)

        text = wx.StaticText(self, label="Config Editor")
        font = text.GetFont()
        font.PointSize += 10
        font = font.Bold()
        text.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.SetSizer(sizer)