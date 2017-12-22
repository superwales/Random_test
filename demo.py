#!/usr/bin/python
#Filename:helloworld.py

import random
from fractions import Fraction
#getsymbol函数，返回一个运算符号
def getoperators():
    operatorslist=('+','-','*','/','+','-')#调节运算符号的比例
    operators=random.choice(operatorslist)
    return operators


#calculate函数，用于计算两个值的四则运算
def calculate(n1,n2,op):
    if op=='+':
      ans=n1+n2
    elif op=='-':
      ans=n1-n2
    elif op=='*':
      ans=n1*n2
    else:
        if n2==0:
          print '分母不能为零！'
        else:
          ans=n1/n2
    return ans

#getnumber函数，返回两个参数，operands是字符串，value是其数值，用Fraction类表示
def getoperands(range):
    operandstype=random.randint(1,2)
    if operandstype==1:
        operands=random.randint(1,range)
        operandsvalue=Fraction(operands,1)
        operands=str(operands)
        #print operands
    else:
        operands1=random.randint(1,range)
        operands2=random.randint(1,range)
        if operands1<operands2:
            operands1,operands2=operands2,operands1
        if operands1==operands2:
            operandsvalue=Fraction(1,2)
            operands='(1/2)'
        else:
            operandsvalue=Fraction(operands2,operands1)
            operands=str(Fraction(operands2,operands1))
    return operands,operandsvalue

'''
#for i in range(1,11):
    #operators=getoperators()
    #print operators
for i in range(1,200):
    (operands,value)=getoperands(200)
    print operands,value
    '''
#getquestion函数，返回两个参数，以字符串的形式返回一个题目，以fraction类返回答案
def getquestion(ran):#range是操作数的取值范围
    symbolnumber=random.randint(1,10)#随机生成操作符个数
    question=''
    questionstack=[]
    ans=0

    for i in range(1,symbolnumber+1):
        (op,va)=getoperands(ran)
        operands=op
        value=va
        operators=getoperators()
        question=question+operands+operators
        questionstack.append(value)
        questionstack.append(operators)
    (op,va)=getoperands(ran)
    operands=op
    value=va
    question=question+operands
    questionstack.append(value)
    #print question
    #print questionstack
    condition=0
    while len(questionstack)>1:#自定义的不涉及括号的运算
        for i in range(0,len(questionstack)):
          if questionstack[i]=='*':
            questionstack[i-1]=questionstack[i-1]*questionstack[i+1]
            del questionstack[i]
            del questionstack[i]
            break
          elif questionstack[i]=='/':
            questionstack[i-1]=questionstack[i-1]/questionstack[i+1]
            del questionstack[i]
            del questionstack[i]
            break
          else:
            condition=1
        if condition==1:
            if len(questionstack)>1:
                questionstack[0]=calculate(questionstack[0],questionstack[2],questionstack[1])
                del questionstack[1]
                del questionstack[1]
        #print question
        #print questionstack
    else:
        ans=questionstack[0]       
    return question,ans

#确定题目的个数和运算范围
questionnumber=int(raw_input('请输入题目的个数：'))
ran=int(raw_input('请输入运算范围：'))
questionlist=[]#题目存在一个列表中
anslist=[]#答案存在一个列表中

while len(questionlist)<questionnumber:
    (question,ans)=getquestion(ran)
    cond=0
    for element in questionlist:
        if element==question:
            cond=1
    if cond==0:
        questionlist.append(question)
        anslist.append(ans)
print '题目已经生成完毕！'
#print questionlist
correct_number=0
total_number=questionnumber
print '本次答题开始！共',questionnumber,'题，总分100分，答题时间45分钟！'
#time_start=time.time()
for i in range(0,questionnumber):
    print'第',i+1,'题是：'
    print questionlist[i],'='
    #ans_user=raw_input('请输入你的答案：')
    print '答案是：',anslist[i]
    #time_end=time.time()
    #if time_end-time_start>10:
    #    print '时间到！请停止答题！'
    #    break
    ans_user=raw_input('请输入你的答案：')
    #if time_end-time_start>10:
    #    print '时间到！请停止答题！'
    #    break
    print '您的答案是：',ans_user
    if ans_user==str(anslist[i]):
        print'回答正确！'
        correct_number=correct_number+1
    else:
        print'回答错误！'
#time_end=time.time()
correct_rate=correct_number*100.0/total_number
print '答题结束！您本次的得分为：',round(correct_rate,1),'分'
