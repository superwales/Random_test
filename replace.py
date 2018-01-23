# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import wx
import v
import time
from question import *

class ReplaceFrame(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,-1,'针对练习',size=(500,350))
        #创建，面板
        panel=wx.Panel(self)

        #在面板上添加控件
        self.quesnum= wx.StaticText(panel, label="   原题:", pos=(7, 20))
        self.quesname = wx.StaticText(panel, label="题目:", pos=(20, 50))
        self.an = wx.StaticText(panel, label="作答:", pos=(20, 170))
        self.time = wx.StaticText(panel, label="用时:", pos=(330, 20))
        self.totalnum = wx.StaticText(panel, label="已答题数:"+str(v.total_num), pos=(330, 100))
        self.correctnum = wx.StaticText(panel, label="正确题数:"+str(v.correct_num), pos=(330, 60))
        self.c = wx.StaticText(panel, label="交互栏", pos=(330, 140))
        self.qran = wx.StaticText(panel, label=" ", pos=(60, 20))
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
        filename = v.username + "_error.txt"
        with open(filename)as f:
            for line in f:
                l = line.split("||")
                v.relist.append(l[0])
        quesname=random.choice(v.relist)
        name,ansr=replaceques(quesname)
        self.qran.SetLabel(quesname)
        v.reans=ansr
        self.question.AppendText(name)
        #v.total_num += 1
        self.totalnum.SetLabelText("已答题数:" + str(v.total_num))
        v.tstart = time.time()
        v.tstart1 = time.time()
        self.con.Clear()
        self.con.AppendText(str(ansr))

        '''self.question.Clear()
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
            self.con.AppendText(str(ans))'''


    def OnFirm(self,e):
        self.con.Clear()
        tend = time.time()
        tuse = tend - v.tstart
        filename1 = v.username + "_error.txt"
        filename2 = v.username + "_history.txt"
        with open(filename2, 'a') as fileobject:
            fileobject.write(self.question.GetValue() + "||" + str(v.reans) + "||" + self.answ.GetValue() + "\n")
        if self.answ.GetValue() == str(v.reans):
            self.con.SetValue("回答正确！\n本题用时%.2f秒\n" % tuse)
            v.correct_num += 1
            self.correctnum.SetLabelText("正确题数:" + str(v.correct_num))
        else:
            with open(filename1, 'a') as fileobject:
                fileobject.write(self.question.GetValue() + "||" + str(v.reans)+ "||" + self.answ.GetValue() + "\n")
            self.con.SetValue("回答错误！正确答案是" + str(v.reans) + "\n本题用时%.2f秒\n" % tuse)
        self.question.Clear()
        self.answ.Clear()
        quesname = random.choice(v.relist)
        name, ansr = replaceques(quesname)
        self.qran.SetLabel(quesname)
        v.total_num += 1
        self.totalnum.SetLabelText("已答题数:" + str(v.total_num))
        v.tstart = time.time()
        v.reans = ansr
        self.question.AppendText(name)
        self.con.AppendText(str(ansr))

    def OnNex(self,e):
        self.question.Clear()
        self.answ.Clear()
        self.con.Clear()
        quesname = random.choice(v.relist)
        name, ansr = replaceques(quesname)
        self.qran.SetLabel(quesname)
        #v.total_num += 1
        #self.totalnum.SetLabelText("已答题数:" + str(v.total_num))
        v.tstart = time.time()
        v.reans=ansr
        self.question.AppendText(name)
        self.con.AppendText(str(ansr))

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


'''app=wx.App(False)
frame=ReplaceFrame(None,-1)

app.MainLoop()'''