# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
        self.quesnum= wx.StaticText(panel, label="运算范围:", pos=(5, 15))
        self.opec = wx.StaticText(panel, label="操作符:", pos=(10, 55))
        self.numc = wx.StaticText(panel, label="数据类型:", pos=(150, 55))
        self.quesname = wx.StaticText(panel, label="题目:", pos=(20, 150))
        self.an = wx.StaticText(panel, label="作答:", pos=(20, 170))
        self.time = wx.StaticText(panel, label="用时:", pos=(330, 20))
        self.totalnum = wx.StaticText(panel, label="已答题数:"+str(v.total_num), pos=(330, 100))
        self.correctnum = wx.StaticText(panel, label="正确题数:"+str(v.correct_num), pos=(330, 60))
        self.c = wx.StaticText(panel, label="交互栏", pos=(330, 140))
        self.qran = wx.TextCtrl(panel,size=(250,25) ,pos=(60, 15))
        self.question=wx.StaticText(panel,pos=(60,150))
        #self.question = wx.TextCtrl(panel, size=(250,100),style=wx.TE_MULTILINE, pos=(60, 50))
        self.answ=wx.TextCtrl(panel,size=(250,80),pos=(60,170))
        self.con = wx.TextCtrl(panel, size=(150, 80), style=wx.TE_MULTILINE, pos=(330, 170))
        self.timer = wx.Timer(self)  # 创建定时器
        sta = wx.Button(panel, label='开始答题',size=(70,30) ,pos=(10, 270))
        firm=wx.Button(panel,label='确认',size=(70,30) ,pos=(90,270))
        nex = wx.Button(panel, label='跳过', size=(70,30) ,pos=(170, 270))
        en = wx.Button(panel, label='结束答题', size=(70,30) ,pos=(410, 270))
        add=wx.Button(panel,label='添加',size=(70,30),pos=(250,270))
        prompt=wx.Button(panel,label='提示',size=(70,30),pos=(330,270))
        self.opecombo=wx.ComboBox(panel,choices=v.opelabels,pos=(60,50),style=wx.CB_READONLY)
        self.numcombo = wx.ComboBox(panel, choices=v.numlabels, pos=(210, 50),style=wx.CB_READONLY)
        self.introduction1=wx.StaticText(panel,label="请先输入运算范围，选择操作符和数据类型\n              然后选择开始答题\n  还可以在主界面的设置中管理操作符标签",pos=(60,80))

        if v.username!="":
            filename = v.username + "_setting.txt"
            ownsetlist = []
            with open(filename) as file_object:
                for line in file_object:
                    ownsetlist.append(line)
            ownlist = ownsetlist[0].split("||")
            #print ownlist
            if ownlist[0].rstrip() != '':
                self.qran.SetValue(ownlist[0])
            if ownlist[1].rstrip() != '':
                self.opecombo.Select(int(ownlist[1]))
            if ownlist[2].rstrip() != '':
                self.numcombo.Select(int(ownlist[2]))



        self.Bind(wx.EVT_BUTTON, self.OnSta, sta)
        self.Bind(wx.EVT_BUTTON, self.OnFirm, firm)
        self.Bind(wx.EVT_BUTTON, self.OnNex, nex)
        self.Bind(wx.EVT_BUTTON,self.OnEn,en)
        self.Bind(wx.EVT_BUTTON,self.OnAdd,add)
        self.Bind(wx.EVT_BUTTON,self.OnPro,prompt)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(1000)  # 设定时间间隔

        self.Show(True)

    def OnSta(self,e):
        #self.question.Clear()
        try:
            if self.qran.GetValue() == '':
                wx.MessageBox("请输入运算范围！")
            elif self.opecombo.GetValue() == '':
                wx.MessageBox("请选择操作类型！")
            elif self.numcombo.GetValue() == '':
                wx.MessageBox("请选择数据类型！")
            else:
                ran = self.qran.GetValue()
                opestr = self.opecombo.GetValue().encode('utf-8')
                numstr = self.numcombo.GetValue().encode('utf-8')
                (ques, ans, length) = getlabelquestion(opestr, numstr, int(ran))
                v.answer = str(ans)
                self.question.SetLabel(ques)

                self.totalnum.SetLabelText("已答题数:" + str(v.total_num))
                v.tstart = time.time()
                v.tstart1 = time.time()
                self.con.Clear()
                self.con.AppendText(str(ans) + '\n')
        except ValueError:
            self.con.AppendText('输入类型错误！')



    def OnFirm(self,e):
        self.con.Clear()

        if self.question.GetLabel()=='':
            wx.MessageBox("尚未开始答题！")
        else:
            tend=time.time()
            tuse=tend-v.tstart
            filename2 = v.username + "_history.txt"
            t = time.localtime(time.time())
            st = time.asctime(t)
            st1=st.split(' ')
            date=st1[4]+'_'+st1[1]+'_'+st1[2]
            if self.answ.GetValue()==v.answer:
                with open(filename2, 'a') as fileobject:
                    fileobject.write(str(self.question.GetLabel()) + "||" + v.answer + "||" + str(self.answ.GetValue())+ "||"  + '1'+ "||" +date+"\n")
                self.con.SetValue("回答正确！\n本题用时%.2f秒\n"%tuse)
                v.correct_num+=1
                self.correctnum.SetLabelText("正确题数:" + str(v.correct_num))
            else:
                with open(filename2,'a') as fileobject:
                    fileobject.write(str(self.question.GetLabel()) + "||" + v.answer + "||" + str(self.answ.GetValue()) + "||" + '0'+ "||" +date+"\n")
                self.con.SetValue("回答错误！正确答案是"+v.answer+"\n本题用时%.2f秒\n"%tuse)
            self.question.SetLabel("")
            self.answ.Clear()

            ran = self.qran.GetValue()
            opestr = self.opecombo.GetValue()
            numstr = self.numcombo.GetValue()
            (ques, ans, length) = getlabelquestion(opestr, numstr, int(ran))
            v.total_num += 1
            self.totalnum.SetLabelText("已答题数:" + str(v.total_num))
            v.tstart = time.time()

            v.answer = str(ans)
            self.question.SetLabel(ques)
            self.con.AppendText(str(ans)+'\n')


    def OnNex(self,e):
        if self.question.GetLabel() == '':
            wx.MessageBox("尚未开始答题！")
        else:
            self.question.SetLabel("")
            self.answ.Clear()
            self.con.Clear()
            ran = self.qran.GetValue()
            opestr = self.opecombo.GetValue().encode('utf-8')
            numstr = self.numcombo.GetValue().encode('utf-8')
            (ques, ans, length) = getlabelquestion(opestr, numstr, int(ran))

            self.totalnum.SetLabelText("已答题数:" + str(v.total_num))
            v.tstart=time.time()

            v.answer = str(ans)
            self.question.SetLabel(ques)
            self.con.AppendText(str(ans)+'\n')

    def OnEn(self,e):
        v.ownsetlist[0]=self.qran.GetValue()
        v.ownsetlist[1] = self.opecombo.GetCurrentSelection()
        v.ownsetlist[2] = self.numcombo.GetCurrentSelection()
        filename = v.username + "_setting.txt"
        customset(filename, v.ownsetlist)
        tend1=time.time()
        tuse1=int(tend1-v.tstart1)
        (h,m,s)=transtime(tuse1)
        if v.total_num==0:
            rate=0.00
        else:
            rate=100.0*float(v.correct_num)/float(v.total_num)
        self.Close(True)
        wx.MessageBox("答题结束！本次共答%d题\n用时%d分%d秒，正确率%.2f"%(v.total_num,m,s,rate)+"%")

    def OnAdd(self,e):
        try:
            filename1 = v.username + "_error.txt"
            with open(filename1, 'a') as fileobject:
                fileobject.write(
                    str(self.question.GetLabel()) + "||" + v.answer + "||" + str(self.answ.GetValue()) + "\n")
            self.con.AppendText("已经添加到收藏夹！\n")
        except TypeError:
            self.con.AppendText("收藏序列没有题目！\n（尚未开始答题！）\n")

    def OnPro(self,e):
        qwe=1

    def OnTimer(self,e):
        t=time.localtime(time.time())
        st = time.asctime(t)
        self.time.SetLabel(st)


'''app=wx.App(False)
frame=PracFrame(None,-1)

app.MainLoop()'''