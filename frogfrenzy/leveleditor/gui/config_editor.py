import wx


class ConfigEditor(wx.Panel):

    def __init__(self, parent):
        super(ConfigEditor, self).__init__(parent=parent)

        text = wx.StaticText(self, label="Config Editor but what if\nthe text is really reaslly\nlong like does it wrap to a\nnew line or is it just all cut off or what the fuck is gonna happen")
        font = text.GetFont()
        font.PointSize += 10
        font = font.Bold()
        text.SetFont(font)
        text.Wrap(5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.SetSizer(sizer)