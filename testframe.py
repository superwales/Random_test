# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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
        self.questime = wx.StaticText(panel, label="考试时间(min):", pos=(7, 120))
        self.num = wx.TextCtrl(panel,size=(70,25), pos=(90, 20))
        self.ran = wx.TextCtrl(panel, size=(70,25), pos=(90, 70))
        self.time = wx.TextCtrl(panel, size=(70,25), pos=(90, 120))

        sta = wx.Button(panel, label='开始测试',pos=(50, 160))

        if v.username!="":
            filename = v.username + "_setting.txt"
            ownsetlist = []
            with open(filename) as file_object:
                for line in file_object:
                    ownsetlist.append(line)
            ownlist = ownsetlist[0].split("||")
            #print ownlist
            if ownlist[3].rstrip() != '':
                self.num.SetValue(ownlist[3])
            if ownlist[4].rstrip() != '':
                self.ran.SetValue(ownlist[4])
            if ownlist[5].rstrip() != '':
                self.time.SetValue(ownlist[5])

        self.Bind(wx.EVT_BUTTON, self.OnSta, sta)

        self.Show(True)

    def OnSta(self,e):
        try:
            if self.num.GetValue() == "":
                wx.MessageBox("请输入题目个数！")
            elif self.ran.GetValue() == "":
                wx.MessageBox("请输入运算范围！")
            elif self.time.GetValue() == "":
                wx.MessageBox("请输入考试时间！")
            else:
                v.ownsetlist[3] = self.num.GetValue()
                v.ownsetlist[4] = self.ran.GetValue()
                v.ownsetlist[5] = self.time.GetValue()
                filename = v.username + "_setting.txt"
                customset(filename, v.ownsetlist)
                v.ques_num = int(self.num.GetValue())
                v.ques_ran = int(self.ran.GetValue())
                v.ques_time = int(self.time.GetValue())
                v.ques_time = v.ques_time * 60
                (q, a, s, m) = getquestionlist(v.ques_num, v.ques_ran)
                v.questionlist = q
                v.anslist = a
                v.scorelist = s
                v.myanslist = m
                self.Close()
                testframe = TestFrame(None, -1)
        except ValueError:
            wx.MessageBox("输入类型错误！")



class TestFrame(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,-1,'测试模式',size=(350,200))
        #创建，面板
        panel=wx.Panel(self)

        #在面板上添加控件
        self.questh= wx.StaticText(panel, label="第1题", pos=(5, 20))
        self.ques = wx.StaticText(panel, label=v.questionlist[0], pos=(40, 20))
        self.qnum = wx.StaticText(panel,  pos=(200, 20))
        self.time = wx.StaticText(panel,  pos=(200, 70))
        self.ans = wx.StaticText(panel, label="作答:", pos=(5, 70))
        self.an = wx.TextCtrl(panel, pos=(40, 70))

        self.timer = wx.Timer(self)  # 创建定时器
        las = wx.Button(panel, label='上一题',size=(70,30) ,pos=(10, 120))
        firm=wx.Button(panel,label='提交',size=(70,30) ,pos=(250,120))
        nex = wx.Button(panel, label='下一题', size=(70,30) ,pos=(90, 120))
        #tem = wx.Button(panel, label='缓存', size=(70, 30), pos=(90, 120))

        self.Bind(wx.EVT_BUTTON, self.OnLas, las)
        self.Bind(wx.EVT_BUTTON, self.OnFirm, firm)
        self.Bind(wx.EVT_BUTTON, self.OnNex, nex)
        #self.Bind(wx.EVT_BUTTON, self.OnTem,tem)

        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(1000)  # 设定时间间隔
        (h, m, s) = transtime(v.ques_time)
        self.time.SetLabel("剩余时间：" + str(h) + ":" + str(m) + ":" + str(s))
        self.qnum.SetLabel("已答题数：" + str(0) + "/" + str(v.ques_num))
        self.Show(True)

    def OnLas(self,e):

        if v.quesorder==0:
            wx.MessageBox("已经是第一题！")
        else:
            v.myanslist[v.quesorder] = self.an.GetValue()
            t = 0
            for ietms in v.myanslist:
                if ietms != "":
                    t = t + 1
            self.qnum.SetLabel("已答题数：" + str(t) + "/" + str(v.ques_num))
            v.quesorder=v.quesorder-1
            order=v.quesorder+1
            self.questh.SetLabel("第%d题"%order)
            self.ques.SetLabel(str(v.questionlist[v.quesorder]))
            self.an.SetValue(v.myanslist[v.quesorder])
    def OnFirm(self,e):
        for i in range(0,v.ques_num):
            if str(v.myanslist[i]) == str(v.anslist[i]):
                v.grade=v.grade+v.scorelist[i]
        gra=GradeFrame(None,-1)
        self.Close()
    def OnNex(self,e):

        if v.quesorder==v.ques_num-1:
            wx.MessageBox("已经是最后一题！")
        else:
            v.myanslist[v.quesorder] = self.an.GetValue()
            t = 0
            for ietms in v.myanslist:
                if ietms != "":
                    t = t + 1
            self.qnum.SetLabel("已答题数：" + str(t) + "/" + str(v.ques_num))
            v.quesorder = v.quesorder + 1
            order = v.quesorder + 1
            self.questh.SetLabel("第%d题"%order)
            self.ques.SetLabel(str(v.questionlist[v.quesorder]))
            self.an.SetValue(v.myanslist[v.quesorder])
    def OnTem(self,e):
        v.myanslist[v.quesorder] = self.an.GetValue()
        t=0
        for ietms in v.myanslist:
            if ietms!="":
                t=t+1
        self.qnum.SetLabel("已答题数："+str(t)+"/"+str(v.ques_num))
    def OnTimer(self,e):
        v.ques_time=v.ques_time-1
        (h,m,s)=transtime(v.ques_time)
        self.time.SetLabel("剩余时间："+str(h)+":"+str(m)+":"+str(s))
        if v.ques_time==300:
            wx.MessageBox("答题时间还有5分钟！")
        elif v.ques_time==0:
            self.Close()
            grade = GradeFrame(None, -1)

class GradeFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,-1,'测试结果',size=(300,450))
        #创建，面板
        panel=wx.Panel(self)

        #在面板上添加控件
        self.n= wx.StaticText(panel, label="成绩单", pos=(120, 20))
        self.detail = wx.TextCtrl(panel, size=(270, 300),style=wx.TE_MULTILINE, pos=(10, 40))
        save = wx.Button(panel, label='保存', size=(70, 30), pos=(50, 370))
        exi = wx.Button(panel, label='退出', size=(70, 30), pos=(150, 370))

        self.detail.SetValue(str(v.username)+"    您本次的成绩为："+str(v.grade)+"分\n")

        for i in range(0,v.ques_num):
            self.detail.AppendText("第%d题："%(i+1)+str(v.questionlist[i])+str(v.scorelist[i])+"\n")
            if str(v.myanslist[i])==str(v.anslist[i]):
                self.detail.AppendText("回答正确！  正确答案是："+str(v.anslist[i])+"("+str(v.myanslist[i])+")\n")
            else:
                self.detail.AppendText("回答错误！  正确答案是："+str(v.anslist[i])+"("+str(v.myanslist[i])+")\n")

        self.Bind(wx.EVT_BUTTON, self.OnSave, save)
        self.Bind(wx.EVT_BUTTON, self.OnExi, exi)


        self.Show()
    def OnSave(self,e):
        filename=v.username+"_test.txt"
        filename1 = v.username + "_error.txt"
        filename2 = v.username + "_history.txt"
        with open(filename,'w') as file_object:
            file_object.write(str(v.username)+"    您本次的成绩为："+str(v.grade)+"分\n")
            for i in range(0, v.ques_num):
                with open(filename2,'a') as fileobject:
                    fileobject.write(str(v.questionlist[i]) + "||" + str(v.anslist[i]) + "||" + str(v.myanslist[i]) + "\n")
                file_object.write("第%d题：" % (i + 1) + str(v.questionlist[i]) + "\n")
                if str(v.myanslist[i]) == str(v.anslist[i]):
                    file_object.write("回答正确！  正确答案是："+str(v.anslist[i])+"("+str(v.myanslist[i])+")\n")
                else:
                    file_object.write("回答错误！  正确答案是：" + str(v.anslist[i]) + "(" + str(v.myanslist[i]) + ")\n")
                    with open(filename1,'a') as fileobject:
                        fileobject.write(str(v.questionlist[i]) + "||" + str(v.anslist[i]) + "||" + str(v.myanslist[i]) + "\n")

    def OnExi(self,e):
        self.Close()
'''
app=wx.App(False)
frame=PreFrame(None,-1)

app.MainLoop()'''
