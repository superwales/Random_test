# -*- coding:UTF-8 -*-
import wx
import v
import time
from question import *

class PracFrame(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,-1,'随机练习',size=(500,350))
        #创建，面板
        panel=wx.Panel(self)

        #在面板上添加控件
        self.quesnum= wx.StaticText(panel, label="运算范围:", pos=(5, 20))
        self.quesname = wx.StaticText(panel, label="题目:", pos=(20, 50))
        self.an = wx.StaticText(panel, label="作答:", pos=(20, 170))
        self.time = wx.StaticText(panel, label="用时:", pos=(330, 20))
        self.totalnum = wx.StaticText(panel, label="已答题数:"+str(v.total_num), pos=(330, 100))
        self.correctnum = wx.StaticText(panel, label="正确题数:"+str(v.correct_num), pos=(330, 60))
        self.c = wx.StaticText(panel, label="交互栏", pos=(330, 140))
        self.qran = wx.TextCtrl(panel, pos=(60, 20))
        self.question = wx.TextCtrl(panel, size=(250,100),style=wx.TE_MULTILINE, pos=(60, 50))
        self.answ=wx.TextCtrl(panel,size=(250,70),pos=(60,170))
        self.con = wx.TextCtrl(panel, size=(150, 120), style=wx.TE_MULTILINE, pos=(330, 170))
        self.timer = wx.Timer(self)  # 创建定时器
        sta = wx.Button(panel, label='开始答题',size=(70,30) ,pos=(15, 270))
        firm=wx.Button(panel,label='确认',size=(70,30) ,pos=(95,270))
        nex = wx.Button(panel, label='下一题', size=(70,30) ,pos=(175, 270))
        en = wx.Button(panel, label='结束答题', size=(70,30) ,pos=(255, 270))

        self.Bind(wx.EVT_BUTTON, self.OnSta, sta)
        self.Bind(wx.EVT_BUTTON, self.OnFirm, firm)
        self.Bind(wx.EVT_BUTTON, self.OnNex, nex)
        self.Bind(wx.EVT_BUTTON,self.OnEn,en)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(1000)  # 设定时间间隔

        self.Show(True)

    def OnSta(self,e):
        self.question.Clear()
        if self.qran.GetValue()=='':
            wx.MessageBox("请输入运算范围！")
        else:
            ran = self.qran.GetValue()
            (ques, ans, length) = getquestion(int(ran))
            v.answer = str(ans)
            self.question.AppendText(ques)
            v.total_num+=1
            self.totalnum.SetLabelText("已答题数:"+str(v.total_num))
            v.tstart = time.time()
            v.tstart1=time.time()
            self.con.Clear()
            self.con.AppendText(str(ans))


    def OnFirm(self,e):
        self.con.Clear()

        if self.qran.GetValue() == '':
            wx.MessageBox("请输入运算范围！")
        elif self.question.GetValue()=='':
            wx.MessageBox("尚未开始答题！")
        else:
            tend=time.time()
            tuse=tend-v.tstart
            if self.answ.GetValue()==v.answer:
                self.con.SetValue("回答正确！\n本题用时%.2f秒"%tuse)
                v.correct_num+=1
                self.correctnum.SetLabelText("正确题数:" + str(v.correct_num))
            else:
                self.con.SetValue("回答错误！正确答案是"+v.answer+"\n本题用时%.2f秒"%tuse)

    def OnNex(self,e):
        if self.qran.GetValue() == '':
            wx.MessageBox("请输入运算范围！")
        elif self.question.GetValue() == '':
            wx.MessageBox("尚未开始答题！")
        else:
            self.question.Clear()
            self.answ.Clear()
            self.con.Clear()
            ran = self.qran.GetValue()
            (ques, ans, length) = getquestion(int(ran))
            v.total_num += 1
            self.totalnum.SetLabelText("已答题数:" + str(v.total_num))
            v.tstart=time.time()

            v.answer = str(ans)
            self.question.AppendText(ques)
            self.con.AppendText(str(ans))

    def OnEn(self,e):
        tend1=time.time()
        tuse1=int(tend1-v.tstart1)
        (h,m,s)=transtime(tuse1)
        if v.total_num==0:
            rate=0.00
        else:
            rate=100.0*float(v.correct_num)/float(v.total_num)
        self.Close(True)
        wx.MessageBox("答题结束！本次共答%d题\n用时%d分%d秒，正确率%.2f"%(v.total_num,m,s,rate)+"%")

    def OnTimer(self,e):
        t=time.localtime(time.time())
        st = time.asctime(t)
        self.time.SetLabel(st)

'''
app=wx.App(False)
frame=PracFrame(None,-1)

app.MainLoop()'''