#coding=utf-8
import wx
import os

class Bucky(wx.Frame):
    
    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'Test', size=(300,200))
        panel = wx.Panel(self)

        test=wx.TextEntryDialog(None,"enter (freq) here:", 'Title', 'enter')
        if test.ShowModal()==wx.ID_OK:
             apples=test.GetValue()
             #i=apples.find('+')
             print apples;
             os.system('echo 555');

        wx.StaticText(panel, -1, apples, (10,10))
