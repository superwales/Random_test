# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from Wr_quesframe import *
from testframe import *
from historyframe import *
from collectframe import *
from replace import *
from diyques import *
import wx
#创建主界面
class MainFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,-1,'四则运算',size=(200,350))
        #创建，面板
        panel=wx.Panel(self)
        #在面板上添加控件
        self.usinamelabel= wx.StaticText(panel, label=" ", pos=(60, 10))
        self.usinamelabel.SetLabel(v.username)
        #self.correct_rate= wx.StaticText(panel, label="成功率", pos=(100, 30))
        randprac = wx.Button(panel, label="随机练习", pos=(50, 30))
        prac = wx.Button(panel, label="针对练习", pos=(50, 70))
        exam = wx.Button(panel, label="测试模式", pos=(50, 110))
        diyques = wx.Button(panel, label="题目工厂", pos=(50, 150))
        rew = wx.Button(panel, label="收藏夹", pos=(50, 190))
        reh = wx.Button(panel, label="历史记录", pos=(50, 230))
        exi = wx.Button(panel, label="退出", pos=(50, 270))

        self.Bind(wx.EVT_BUTTON, self.Onrandprac, randprac)
        self.Bind(wx.EVT_BUTTON, self.Onprac, prac)
        self.Bind(wx.EVT_BUTTON, self.Onexam, exam)
        self.Bind(wx.EVT_BUTTON, self.Ondiyques, diyques)
        self.Bind(wx.EVT_BUTTON, self.Onrew, rew)
        self.Bind(wx.EVT_BUTTON, self.Onreh, reh)
        self.Bind(wx.EVT_BUTTON, self.Onexi, exi)

        self.Show(True)

    def Onrandprac(self,e):
        #self.Close(True)
        rand=PracFrame(None,-1)
    def Onprac(self,e):
        replace=ReplaceFrame(None,-1)
    def Onexam(self,e):
        exam=PreFrame(None,-1)
    def Ondiyques(self,e):
        diy=DiyFrame(None,-1)
    def Onrew(self,e):
        collect=CollectFrame(None,-1)
    def Onreh(self,e):
        his=HistoryFrame(None,-1)
    def Onexi(self,e):
        self.Close(True)

#创建登录界面
class LoFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,-1,'炜柒运算',size=(280,200))
        #创建，面板
        panel=wx.Panel(self)
        #在面板上添加控件
        self.usinamelabel= wx.StaticText(panel, label="用户名:", pos=(40, 30))
        self.passwordlabel= wx.StaticText(panel, label="密码：", pos=(40, 70))
        self.usrname=wx.TextCtrl(panel,pos=(80,30))
        self.password=wx.TextCtrl(panel,style=wx.TE_PASSWORD,pos=(80,70))
        login=wx.Button(panel,label="登录",pos=(40,100))
        register=wx.Button(panel,label="注册",pos=(130,100))

        self.Bind(wx.EVT_BUTTON,self.OnLogin,login)
        self.Bind(wx.EVT_BUTTON,self.Onreg,register)

        self.Show(True)

    def OnLogin(self,e):
        text_usr=wx.TextDataObject()
        text_usr.SetText(self.usrname.GetValue())
        text_pwd=wx.TextDataObject()
        text_pwd.SetText(self.password.GetValue())

        if text_usr.GetText() == "":
            wx.MessageBox('请输入用户名！')
        elif text_pwd.GetText()== "":
            wx.MessageBox('请输入密码！')
        else:
            with open("username.txt")as file_object:
                result=False
                for line in file_object:
                    l1 = line.split("||")
                    if l1[0].rstrip()==text_usr.GetText() and l1[1].rstrip()==text_pwd.GetText():
                        result=True
                if result==True:
                    wx.MessageBox("登录成功！")
                    v.username=text_usr.GetText()
                    filename1=v.username+"_error.txt"
                    filename2=v.username+"_history.txt"
                    f=open(filename1,'a')
                    f.close()
                    f=open(filename2,'a')
                    f.close()
                    self.Close(True)
                    #打开主界面
                    mainframe=MainFrame(None,-1)
                else:
                    wx.MessageBox("用户名或者密码错误！")


    def Onreg(self,e):
        text_usr = wx.TextDataObject()
        text_usr.SetText(self.usrname.GetValue())
        text_pwd = wx.TextDataObject()
        text_pwd.SetText(self.password.GetValue())

        if text_usr.GetText() == "":
            wx.MessageBox('请输入用户名！')
        elif text_pwd.GetText()== "":
            wx.MessageBox('请输入密码！')
        else:
            with open("username.txt", 'r+')as file_object:
                result = True
                for line in file_object:
                    l1 = line.split("||")
                    if l1[0].rstrip() == text_usr.GetText():
                        result = False
                if result == True:
                    info = "\n" + text_usr.GetText() + "||" + text_pwd.GetText()
                    file_object.write(info)
                    wx.MessageBox("注册成功！现在可以登录！")
                else:
                    wx.MessageBox("用户名已被使用！")

def main():
    app=wx.App(False)
    frame=LoFrame(None,-1)
    app.MainLoop()

if __name__=='__main__':
    main()