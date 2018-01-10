# -*- coding:UTF-8 -*-
import wx
import v

class HistoryFrame(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,-1,'历史记录',size=(300,500))
        #创建，面板
        panel=wx.Panel(self)

        filename = v.username + "_history.txt"
        length = 0
        num = 0
        rate = 0
        with open(filename) as f:
            for line in f:
                length = length + 1
                l1 = line.split("||")
                if l1[1].rstrip() == l1[2].rstrip():
                    num = num + 1
        if length == 0:
            rate = 0
        else:
            rate = 100 * float(num) / float(length)
        #在面板上添加控件
        self.name=wx.StaticText(panel,label=v.username,pos=(10,20))
        self.qnum = wx.StaticText(panel, label="共%d题"%length, pos=(100, 20))
        self.rate = wx.StaticText(panel, label="正确率：%.2f"%rate+"%", pos=(190, 20))
        self.quesname=wx.StaticText(panel,label="题目：",pos=(10,250))
        self.quesans = wx.StaticText(panel, label="答案：", pos=(10, 280))
        self.history = wx.TextCtrl(panel, size=(270, 200), style=wx.TE_MULTILINE, pos=(10, 40))
        self.result = wx.TextCtrl(panel, size=(270, 100), style=wx.TE_MULTILINE, pos=(10, 315))
        self.qname = wx.TextCtrl(panel,size=(200,25), pos=(50, 250))
        self.qans = wx.TextCtrl(panel,size=(200,25), pos=(50, 280))
        exi = wx.Button(panel, label='退出', size=(70, 30), pos=(150, 420))
        search = wx.Button(panel, label='查询', size=(70, 30), pos=(50, 420))
        self.history.Clear()

        with open(filename) as f:
            for line in f:
                l1 = line.split("||")
                self.history.AppendText("题目："+l1[0].rstrip()+"\n"+"  正确答案："+l1[1].rstrip()+"  您的答案："+l1[2].rstrip()+"\n")

        self.Bind(wx.EVT_BUTTON, self.OnExi, exi)
        self.Bind(wx.EVT_BUTTON, self.OnSearch, search)

        self.Show(True)
    def OnSearch(self,e):
        if self.qname.GetValue()==""and self.qans.GetValue()=="":
            wx.MessageBox("请先输入搜索条件！")
        else:
            if self.qname.GetValue()=="":
                self.qname.SetValue(" ")
            elif self.qans.GetValue()=="":
                self.qans.SetValue(" ")
            self.result.Clear()
            filename = v.username + "_history.txt"
            with open(filename)as f:
                for line in f:
                    l=line.split("||")
                    label0=l[0].find(self.qname.GetValue())
                    label1 = l[1].find(self.qans.GetValue())
                    label2 = l[2].find(self.qans.GetValue())
                    if label0!=-1:
                        self.result.AppendText("题目："+l[0].rstrip()+"\n"+"  正确答案："+l[1].rstrip()+"  您的答案："+l[2].rstrip()+"\n")
                    elif label1!=-1:
                        self.result.AppendText("题目：" + l[0].rstrip() + "\n" + "  正确答案：" + l[1].rstrip() + "  您的答案：" + l[2].rstrip() + "\n")
                    elif label2!=-1:
                        self.result.AppendText("题目：" + l[0].rstrip() + "\n" + "  正确答案：" + l[1].rstrip() + "  您的答案：" + l[2].rstrip() + "\n")
    def OnExi(self,e):
        self.Close()
'''
app=wx.App(False)
frame=HistoryFrame(None,-1)
app.MainLoop()'''
