import wx
class OtherFrame(wx.Frame):
    """
    Class used for creating the main farme for blackjack game
    """
    
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title, size=(1000, 900))
        self.Show()
    

    
class MainFrame(wx.Frame):
    """
    Class used to create Frame for Start page
    """

    def __init__(self):
        wx.Frame.__init__(self, None, title='Main Frame', size=(300, 200))
        self.InitUI()
        self.Show()
        self.Center()
  
    def InitUI(self):
        """
        method to create widgets on start page
        """
        
        panel = wx.Panel(self)
        panel.SetBackgroundColour("white")

        sizer = wx.GridBagSizer(4, 4)
        btn = wx.Button(panel, label='Start')
        btn.Bind(wx.EVT_BUTTON, self.on_new_frame)
        self.frame_number = 1
        
        text = wx.StaticText(panel, label="Enter player name")
        tctrl = wx.TextCtrl(panel)
        

        sizer.Add(text, pos=(0, 0), flag=wx.TOP|wx.BOTTOM, border=5)
        sizer.Add(tctrl, pos=(0, 2), span=(1, 3), border=5)
        sizer.Add(btn, pos=(4, 4), span=(1, 3), border=5)
      
        panel.SetSizer(sizer)
        
    def on_new_frame(self, event):
        title = 'SubFrame {}'.format(self.frame_number)
        frame = OtherFrame(title=title)
        self.frame_number += 1
        
        

        
        
if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
