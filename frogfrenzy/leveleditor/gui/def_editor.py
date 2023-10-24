import wx


class DefEditor(wx.Panel):

    def __init__(self, parent):
        super(DefEditor, self).__init__(parent)

        text = wx.StaticText(self, label="Definitions Editor")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.SetSizer(sizer)
