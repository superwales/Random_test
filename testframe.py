# -*- coding:UTF-8 -*-
import wx
import v
import time
from question import *

class PreFrame(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,-1,'测试模式',size=(200,250))
        #创建，面板
        panel=wx.Panel(self)

        #在面板上添加控件
        self.quesnum= wx.StaticText(panel, label="题目个数:", pos=(20, 20))
        self.quesran = wx.StaticText(panel, label="运算范围:", pos=(20, 70))
        self.questime = wx.StaticText(panel, label="考试时间:", pos=(20, 120))
        self.num = wx.TextCtrl(panel,size=(70,25), pos=(90, 20))
        self.ran = wx.TextCtrl(panel, size=(70,25), pos=(90, 70))
        self.time = wx.TextCtrl(panel, size=(70,25), pos=(90, 120))

        sta = wx.Button(panel, label='开始测试',pos=(50, 160))

        self.Bind(wx.EVT_BUTTON, self.OnSta, sta)

        self.Show(True)

    def OnSta(self,e):
        if self.num.GetValue()=="":
            wx.MessageBox("请输入题目个数！")
        elif self.ran.GetValue()=="":
            wx.MessageBox("请输入运算范围！")
        elif self.time.GetValue()=="":
            wx.MessageBox("请输入考试时间！")
        else:
            v.ques_num=self.num.GetValue()
            v.ques_ran=self.ran.GetValue()
            v.ques_time=self.time.GetValue()
            self.Close()
            testframe=TestFrame(None,-1)

class TestFrame(wx.Frame):

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

        #self.Bind(wx.EVT_BUTTON, self.OnSta, sta)
        #self.Bind(wx.EVT_BUTTON, self.OnFirm, firm)
        #self.Bind(wx.EVT_BUTTON, self.OnNex, nex)
        #self.Bind(wx.EVT_BUTTON,self.OnEn,en)
        #self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
        #self.timer.Start(1000)  # 设定时间间隔

        self.Show(True)


app=wx.App(False)
frame=TestFrame(None,-1)

app.MainLoop()
