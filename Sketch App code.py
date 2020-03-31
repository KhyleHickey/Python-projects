
"""
name: Khyle Hickey
ID#: 20170449
Class: B.Eng, Year 3, Stream 3
"""


import wx

class Mainframe(wx.Frame): #Frame object
    def __init__(self): 
        wx.Frame.__init__(self, None, title="Sketch Frame", size=(800, 600))
        self.InitUI()
        self.Show()
        self.Center()

    def InitUI(self):

        menubar = wx.MenuBar() #creates menubar
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Open', 'Open Application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        statusbar = self.CreateStatusBar(3) #creates statusbar
        statusbar.SetStatusText("Pos: x, y", 0)
        statusbar.SetStatusText("Current Pt: 1", 1)
        statusbar.SetStatusText("Line Count: 1", 2)

        toolbar = self.CreateToolBar() #creates toolbar
        Ntool = toolbar.AddTool(wx.ID_ANY, "New", wx.Bitmap("new-icon.bmp"))
        Otool = toolbar.AddTool(wx.ID_ANY, "Open", wx.Bitmap("open-file.bmp"))
        SAtool = toolbar.AddTool(wx.ID_ANY, "Save as", wx.Bitmap("save-as.bmp"))
        toolbar.Realize()
         

        panel_1 = wx.Panel(self) #creates panel object with gridbag sizer
        sizer = wx.GridBagSizer(20, 20)
        panel_1.SetSizer(sizer)

       
        
        draw_space = wx.StaticText(panel_1, label="") #whitespace for drawing
        draw_space.SetBackgroundColour("white")
        sizer.Add(draw_space, pos=(0, 4), span=(10, 21), flag= wx.GROW|wx.ALIGN_RIGHT, border=5)

        x=20 #variables to control size of buttons
        y=20

        """
        pictures for colors
        """
        
        pic4 = "black.bmp"
        pic5 = "blue.bmp"
        pic6 = "brown.bmp"
        pic7 = "yellow.bmp"
        pic8 = "white.bmp"
        pic9 = "sky-blue.bmp"
        pic4 = "red.bmp"
        pic10 = "purple.bmp"
        pic11 = "pink.bmp"
        pic12 = "orange.bmp"
        pic13 = "gray.bmp"
        pic14 = "color-11.bmp"
        pic15 = "color-12.bmp"
        pic16 = "color-13.bmp"
        pic17 = "color-14.bmp"
        pic18 = "color-15.bmp"
        pic19 = "color-16.bmp"

        bmp4 = wx.Image(pic4, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap() #subsequent bitmap images
        bmp5 = wx.Image(pic5, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp6 = wx.Image(pic6, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp7 = wx.Image(pic7, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp8 = wx.Image(pic8, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp9 = wx.Image(pic9, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp10 = wx.Image(pic10, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp11 = wx.Image(pic11, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp12 = wx.Image(pic12, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp13 = wx.Image(pic13, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp14 = wx.Image(pic14, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp15 = wx.Image(pic15, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp16 = wx.Image(pic16, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp17 = wx.Image(pic17, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp18 = wx.Image(pic18, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp19 = wx.Image(pic19, type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        
        btn4 = wx.BitmapButton(panel_1, bitmap = bmp4, size=(x, y)) #buttons for colour
        btn5 = wx.BitmapButton(panel_1, bitmap = bmp5, size=(x, y))
        btn6 = wx.BitmapButton(panel_1, bitmap = bmp6, size=(x, y))
        btn7 = wx.BitmapButton(panel_1, bitmap = bmp7, size=(x, y))
        btn8 = wx.BitmapButton(panel_1, bitmap = bmp8, size=(x, y))
        btn9 = wx.BitmapButton(panel_1, bitmap = bmp9, size=(x, y))
        btn10 = wx.BitmapButton(panel_1, bitmap = bmp10, size=(x, y))
        btn11 = wx.BitmapButton(panel_1, bitmap = bmp11, size=(x, y))
        btn12 = wx.BitmapButton(panel_1, bitmap = bmp12, size=(x, y)) 
        btn13 = wx.BitmapButton(panel_1, bitmap = bmp13, size=(x, y))
        btn14 = wx.BitmapButton(panel_1, bitmap = bmp14, size=(x, y))
        btn15 = wx.BitmapButton(panel_1, bitmap = bmp15, size=(x, y))
        btn16 = wx.BitmapButton(panel_1, bitmap = bmp16, size=(x, y))
        btn17 = wx.BitmapButton(panel_1, bitmap = bmp17, size=(x, y))
        btn18 = wx.BitmapButton(panel_1, bitmap = bmp18, size=(x, y))
        btn19 = wx.BitmapButton(panel_1, bitmap = bmp19, size=(x, y))

        
        sizer.Add(btn4, pos=(2, 0), span=(1, 1), border=0) #positioning buttons with gridbag sizer
        sizer.Add(btn5, pos=(2, 1), span=(1, 1), border=5)
        sizer.Add(btn6, pos=(2, 2), span=(1, 1), border=5)
        sizer.Add(btn7, pos=(2, 3), span=(1, 1), border=5)
        sizer.Add(btn8, pos=(3, 0), span=(1, 1), border=5)
        sizer.Add(btn9, pos=(3, 1), span=(1, 1), border=5)
        sizer.Add(btn10, pos=(3, 2), span=(1, 1), border=5)
        sizer.Add(btn11, pos=(3, 3), span=(1, 1), border=5)
        sizer.Add(btn12, pos=(4, 0), span=(1, 1), border=5)
        sizer.Add(btn13, pos=(4, 1), span=(1, 1), border=5)
        sizer.Add(btn14, pos=(4, 2), span=(1, 1), border=5)
        sizer.Add(btn15, pos=(4, 3), span=(1, 1), border=5)
        sizer.Add(btn16, pos=(5, 0), span=(1, 1), border=5)
        sizer.Add(btn17, pos=(5, 1), span=(1, 1), border=5)
        sizer.Add(btn18, pos=(5, 2), span=(1, 1), border=5)
        sizer.Add(btn19, pos=(5, 3), span=(1, 1), border=5)
        

        """
        buttons for brush size
        """

        btn_4 = wx.Button(panel_1, label="1", size=(x, y))
        btn_5 = wx.Button(panel_1, label="2", size=(x, y))
        btn_6 = wx.Button(panel_1, label="3", size=(x, y))
        btn_7 = wx.Button(panel_1, label="4", size=(x, y))
        btn_8 = wx.Button(panel_1, label="5", size=(x, y))
        btn_9 = wx.Button(panel_1, label="6", size=(x, y))
        btn_10 = wx.Button(panel_1, label="7", size=(x, y))
        btn_11 = wx.Button(panel_1, label="8", size=(x, y))
        btn_12 = wx.Button(panel_1, label="9", size=(x, y))
        btn_13 = wx.Button(panel_1, label="10", size=(x, y))
        btn_14 = wx.Button(panel_1, label="11", size=(x, y))
        btn_15 = wx.Button(panel_1, label="12", size=(x, y))
        btn_16 = wx.Button(panel_1, label="13", size=(x, y))
        btn_17 = wx.Button(panel_1, label="14", size=(x, y))
        btn_18 = wx.Button(panel_1, label="15", size=(x, y))
        btn_19 = wx.Button(panel_1, label="16", size=(x, y))

        sizer.Add(btn_4, pos=(7, 0), span=(1, 1), border=5)
        sizer.Add(btn_5, pos=(7, 1), span=(1, 1), border=5)
        sizer.Add(btn_6, pos=(7, 2), span=(1, 1), border=5)
        sizer.Add(btn_7, pos=(7, 3), span=(1, 1), border=5)
        sizer.Add(btn_8, pos=(8, 0), span=(1, 1), border=5)
        sizer.Add(btn_9, pos=(8, 1), span=(1, 1), border=5)
        sizer.Add(btn_10, pos=(8, 2), span=(1, 1), border=5)
        sizer.Add(btn_11, pos=(8, 3), span=(1, 1), border=5)
        sizer.Add(btn_12, pos=(9, 0), span=(1, 1), border=5)
        sizer.Add(btn_13, pos=(9, 1), span=(1, 1), border=5)
        sizer.Add(btn_14, pos=(9, 2), span=(1, 1), border=5)
        sizer.Add(btn_15, pos=(9, 3), span=(1, 1), border=5)
        sizer.Add(btn_16, pos=(10, 0), span=(1, 1), border=5)
        sizer.Add(btn_17, pos=(10, 1), span=(1, 1), border=5)
        sizer.Add(btn_18, pos=(10, 2), span=(1, 1), border=5)
        sizer.Add(btn_19, pos=(10, 3), span=(1, 1), border=5)

if __name__ == '__main__':
    app = wx.App(False)
    frame = Mainframe()
    app.MainLoop()

    
        
