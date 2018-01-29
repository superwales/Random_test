# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import wx
import v
import time
from question import *

class DiyFrame(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,-1,'题目工厂',size=(300,400))
        #创建，面板
        panel=wx.Panel(self)

        self.optype=wx.StaticText(panel,label='操作符类型',pos=(5,15))
        self.nutype = wx.StaticText(panel, label='数据类型', pos=(5, 55))
        self.btype=wx.StaticText(panel,label='有无括号',pos=(150,55))
        self.ran = wx.StaticText(panel, label='运算范围', pos=(5, 90))
        self.j1 = wx.StaticText(panel, label='加', pos=(90, 5))
        self.j2 = wx.StaticText(panel, label='减', pos=(140, 5))
        self.j3 = wx.StaticText(panel, label='乘', pos=(190, 5))
        self.j4 = wx.StaticText(panel, label='除', pos=(240, 5))
        self.n=wx.StaticText(panel,label='题目数量',pos=(150,90))
        self.ques = wx.StaticText(panel, label='题目', pos=(5, 270))
        self.ans=wx.StaticText(panel,label='答案',pos=(5,290))
        self.numtype = wx.ComboBox(panel, choices=['随机','整数','真分数'], pos=(75, 50), style=wx.CB_READONLY)
        self.bratype=wx.ComboBox(panel,choices=['有','无'],pos=(220,50),style=wx.CB_READONLY)
        self.jia=wx.TextCtrl(panel,size=(40,20),pos=(75,25))
        self.jian = wx.TextCtrl(panel, size=(40, 20), pos=(125, 25))
        self.cheng = wx.TextCtrl(panel, size=(40, 20), pos=(175, 25))
        self.chu = wx.TextCtrl(panel, size=(40, 20), pos=(225, 25))
        self.ran=wx.TextCtrl(panel,size=(50,20),pos=(75,90))
        self.number=wx.TextCtrl(panel,size=(50,20),pos=(220,90))
        self.quesname=wx.StaticText(panel,label='',pos=(40,270))
        self.answer = wx.StaticText(panel, label='', pos=(40, 290))
        self.con=wx.StaticText(panel,label='',pos=(10,345))

        queslist=[]
        self.listbox=wx.ListBox(panel,-1,pos=(5,120),size=(270,150),choices=queslist,style=wx.LB_HSCROLL)

        if v.username!="":
            filename = v.username + "_setting.txt"
            ownsetlist = []
            with open(filename) as file_object:
                for line in file_object:
                    ownsetlist.append(line)
            ownlist = ownsetlist[0].split("||")
            #print ownlist
            if ownlist[6].rstrip() != '':
                self.jia.SetValue(ownlist[6])
            if ownlist[7].rstrip() != '':
                self.jian.SetValue(ownlist[7])
            if ownlist[8].rstrip() != '':
                self.cheng.SetValue(ownlist[8])
            if ownlist[9].rstrip() != '':
                self.chu.SetValue(ownlist[9])
            if ownlist[10].rstrip() != '':
                self.numtype.Select(int(ownlist[10]))
            if ownlist[11].rstrip() != '':
                self.bratype.Select(int(ownlist[11]))
            if ownlist[12].rstrip() != '':
                self.ran.SetValue(ownlist[12])
            if ownlist[13].rstrip() != '':
                self.number.SetValue(ownlist[13])


        sta = wx.Button(panel, label='开始出题', size=(70, 30), pos=(3, 310))
        add = wx.Button(panel, label='添加', size=(70, 30), pos=(73, 310))
        ex = wx.Button(panel, label='退出', size=(70, 30), pos=(213, 310))
        cl = wx.Button(panel, label='清空', size=(70, 30), pos=(143, 310))


        self.Bind(wx.EVT_BUTTON, self.OnSta, sta)
        self.Bind(wx.EVT_BUTTON, self.OnAdd, add)
        self.Bind(wx.EVT_BUTTON, self.OnEx, ex)
        self.Bind(wx.EVT_BUTTON, self.OnCl, cl)
        self.Bind(wx.EVT_LISTBOX,self.OnClick,self.listbox)

        self.Show(True)
    def OnClick(self,e):
        n=self.listbox.GetSelection()
        if n%2==0:
            str1=self.listbox.GetString(n)
            str1=str1.replace('题目：','')
            self.quesname.SetLabel(str1.strip())
            str2=self.listbox.GetString(n+1)
            str2=str2.replace('正确答案：','')
            self.answer.SetLabel(str2.strip())
        elif n%2==1:
            str1 = self.listbox.GetString(n-1)
            str1 = str1.replace('题目：', '')
            self.quesname.SetLabel(str1.strip())
            str2 = self.listbox.GetString(n)
            str2 = str2.replace('正确答案：', '')
            self.answer.SetLabel(str2.strip())
        self.con.SetLabel("")

    def OnSta(self,e):
        try:
            if self.jia.GetValue() == '' and self.jian.GetValue() == '' and self.cheng.GetValue() == '' and self.chu.GetValue() == '':
                wx.MessageBox("请至少输入一项操作符个数！")
            elif self.numtype.GetValue().encode('utf-8') == "":
                wx.MessageBox("请选择数据类型！")
            elif self.ran.GetValue() == '':
                wx.MessageBox("请输入运算范围！")
            elif self.bratype.GetValue().encode('utf-8') == "":
                wx.MessageBox("请选择有无括号！")
            elif self.number.GetValue() == '':
                wx.MessageBox("请选择出题数量！")
            else:
                self.listbox.Clear()
                n = int(self.number.GetValue())
                for i in range(1, n + 1):
                    list = []
                    numstr = self.numtype.GetValue().encode('utf-8')
                    brastr = self.bratype.GetValue().encode('utf-8')
                    ran = int(self.ran.GetValue())
                    if self.jia.GetValue() == '':
                        i = 0
                    else:
                        i = int(self.jia.GetValue())
                    for i in range(0, i):
                        list.append('+')
                    if self.jian.GetValue() == '':
                        i = 0
                    else:
                        i = int(self.jian.GetValue())
                    for i in range(0, i):
                        list.append('-')
                    if self.cheng.GetValue() == '':
                        i = 0
                    else:
                        i = int(self.cheng.GetValue())
                    for i in range(0, i):
                        list.append('×')
                    if self.chu.GetValue() == '':
                        i = 0
                    else:
                        i = int(self.chu.GetValue())
                    for i in range(0, i):
                        list.append('÷')
                    (ques, ans, length) = getdiyquestion(list, numstr, ran, brastr)
                    quesname = ques + '||' + str(ans) + '||'
                    v.queslist.append(quesname)
                    # self.ques.SetLabel(ques)
                    self.listbox.Append('题目：' + ques)
                    self.listbox.Append('    正确答案：' + str(ans))
            self.con.SetLabel("题目已经更新完毕！")
        except ValueError:
            if self.jia.GetValue() == '1' or self.jian.GetValue() == '1' or self.cheng.GetValue() == '1' or self.chu.GetValue() == '1':
                if self.bratype.GetCurrentSelection()==0:
                    self.con.SetLabel("有括号时运算符数量应当大于1！")
            else:
                self.con.SetLabel("输入类型错误！")




    def OnAdd(self,e):
        filename=v.username + "_error.txt"
        with open(filename, 'a') as fileobject:
            fileobject.write(str(self.quesname.GetLabel()) + "||" + str(self.answer.GetLabel()) + "||" +' 来源于题目工厂' + "\n")
        self.con.SetLabel("已经添加到收藏夹！")

    def OnEx(self,e):
        v.ownsetlist[6] = self.jia.GetValue()
        v.ownsetlist[7] = self.jian.GetValue()
        v.ownsetlist[8] = self.cheng.GetValue()
        v.ownsetlist[9] = self.chu.GetValue()
        v.ownsetlist[10] = self.numtype.GetCurrentSelection()
        v.ownsetlist[11] = self.bratype.GetCurrentSelection()
        v.ownsetlist[12] = self.ran.GetValue()
        v.ownsetlist[13] = self.number.GetValue()
        filename = v.username + "_setting.txt"
        customset(filename, v.ownsetlist)
        self.Close(True)

    def OnCl(self,e):
        self.listbox.Clear()
        self.con.SetLabel("已经清空！")
        self.quesname.SetLabel("")
        self.answer.SetLabel("")




'''app=wx.App(False)
frame=DiyFrame(None,-1)

app.MainLoop()'''