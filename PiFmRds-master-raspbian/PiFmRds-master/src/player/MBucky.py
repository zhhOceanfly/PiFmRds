#coding=utf-8
import wx
import os

class Bucky(wx.Frame):
    
    def __init__(self, music_name, parent, id):
        wx.Frame.__init__(self, parent, id, 'Test', size=(300,200))
        panel = wx.Panel(self)

        test=wx.TextEntryDialog(None,"enter (freq) here:", 'Title', 'enter')
        if test.ShowModal()==wx.ID_OK:
             apples=test.GetValue();
	     str = 'sudo ../pi_fm_rds -audio ' + music_name + ' -freq ' + apples + ' &';
             print str;
	     os.system(str);

        #wx.StaticText(panel, -1, apples, (10,10))
