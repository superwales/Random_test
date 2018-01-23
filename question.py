# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import random
import time
from fractions import Fraction
#getsymbol函数，返回一个运算符号
def getoperators():
    operatorslist=('+','-','×','÷','+','-')
    operators=random.choice(operatorslist)
    if operators=='×':
        length=2
    elif operators=='÷':
        length=2
    else:
        length=1
    return operators,length




#calculate函数，用于计算两个值的四则运算
def calculate(n1,n2,op):
    if op=='+':
      ans=n1+n2
    elif op=='-':
      ans=n1-n2
    elif op=='×':
      ans=n1*n2
    else:
        if n2==0:
          print '分母不能为零！'
        else:
          ans=n1/n2
    return ans

#getnumber函数，返回一个数，表示整数或者一个真分数，有两种形式，字符串和浮点数
def getoperands(range):
    operandstype=random.randint(1,2)
    degree=0
    if operandstype==1:
        operands=random.randint(1,range)
        operandsvalue=Fraction(operands,1)
        operands=str(operands)
        degree=1
        #print operands
    else:
        operands1=random.randint(1,range)
        operands2=random.randint(1,range)
        degree=1.5
        if operands1<operands2:
            operands1,operands2=operands2,operands1
        if operands1==operands2:
            operandsvalue=Fraction(1,2)
            operands='1/2'
        else:
            operandsvalue=Fraction(operands2,operands1)
            operands=str(Fraction(operands2,operands1))
    return operands,operandsvalue,degree

#getquestion函数，以字符串的形式返回一个题目
def getquestion(ran):#range是操作数的取值范围
    symbolnumber=random.randint(1,5)
    question=''
    questionstack=[]
    ans=0
    length_ques=0

    for i in range(1,symbolnumber+1):
        (op,va,de)=getoperands(ran)
        operands=op
        value=va
        (operators,length)=getoperators()
        question=question+operands+operators
        questionstack.append(value)
        questionstack.append(operators)
        length_ques=length_ques+length+de
    (op,va,de)=getoperands(ran)
    operands=op
    value=va
    question=question+operands
    questionstack.append(value)
    length_ques=length_ques+de
    #print question
    #print questionstack
    condition=0
    while len(questionstack)>1:
        for i in range(0,len(questionstack)):
          if questionstack[i]=='×':
            questionstack[i-1]=questionstack[i-1]*questionstack[i+1]
            del questionstack[i]
            del questionstack[i]
            break
          elif questionstack[i]=='÷':
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
    return question,ans,length_ques

def getquestionlist(num,ran):
    questionlist = []  # 题目存在一个列表中
    anslist = []  # 答案存在一个列表中
    lengthlist = []  # 权重存在一个列表中
    scorelist = []  # 分数存在一个列表中
    myanslist = []  # 回答答案存在一个列表中
    totalscore = 0

    #questionfile = file('questionlist.txt', 'w')
    # 根据输入的题目个数生成题目清单，每一个新生成的题会与现有题进行比较，重复不则重新生成
    # 将生成的题目写入文件中，便于查看与打印
    while len(questionlist) < num:
        (question, ans, length) = getlabelquestion('随机','随机',ran)
        cond = 0
        for element in questionlist:
            if element == question:
                cond = 1
        if cond == 0:
            questionlist.append(question)
            anslist.append(ans)
            myanslist.append("")
            lengthlist.append(length)
            totalscore = totalscore + length
            #questionfile.write(question + '\n')
    #questionfile.close()
    #print '题目已经生成完毕！'
    # 根据权重分配分值
    for i in range(0, len(lengthlist)):
        scorelist.append(round(lengthlist[i] * 100 / totalscore))
    return questionlist,anslist,scorelist,myanslist

def transtime(sec):
    hours=sec/3600
    tem1=sec-(hours*3600)
    minutes=tem1/60
    tem2=tem1-minutes*60
    seconds=tem2
    return hours,minutes,seconds

def deletei(txtname,i):
    with open(txtname, 'r') as old_file:
        with open(txtname, 'r+') as new_file:

            current_line = 0

            # 定位到需要删除的行
            while current_line < (i - 1):
                old_file.readline()
                current_line += 1

            # 当前光标在被删除行的行首，记录该位置
            seek_point = old_file.tell()

            # 设置光标位置
            new_file.seek(seek_point, 0)

            # 读需要删除的行，光标移到下一行行首
            old_file.readline()

            # 被删除行的下一行读给 next_line
            next_line = old_file.readline()

            # 连续覆盖剩余行，后面所有行上移一行
            while next_line:
                new_file.write(next_line)
                next_line = old_file.readline()
            # 写完最后一行后截断文件，因为删除操作，文件整体少了一行，原文件最后一行需要去掉
            new_file.truncate()

def vfraction(str):
    str1='1'
    str2='1'
    con=0
    for i in range(0,len(str)-1):
        if str[i]=='/':
            str1=str[0:i]
            str2=str[i+1:len(str)]
            con=1
    if con==0:
        str1=str
    return Fraction(int(str1),int(str2))

def replacestr(ques,ques_1):
    question = ques.encode('utf8')
    # print question
    queslist = []
    requeslist = ''
    requesstack = []
    k = 0
    for i in range(0, len(question) - 1):
        # print question[i:i+2]
        if question[i] == "+":  # 前处理
            queslist.append(question[k:i])
            queslist.append(question[i])
            k = i + 1
        elif question[i] == '-':
            queslist.append(question[k:i])
            queslist.append(question[i])
            k = i + 1
        elif question[i:i + 2] == '×':
            queslist.append(question[k:i])
            queslist.append(question[i:i + 2])
            k = i + 2
        elif question[i:i + 2] == '÷':
            queslist.append(question[k:i])
            queslist.append(question[i:i + 2])
            k = i + 2
    queslist.append(question[k:len(question)])
    # print queslist
    # print len(queslist)
    for i in range(0, len(queslist) - 1):
        # print i
        if queslist[i] == '+' or queslist[i] == '-' or queslist[i] == '×' or queslist[i] == '÷':
            if queslist[i-1]==ques_1:
                requeslist = requeslist + queslist[i - 1] + queslist[i]
                requesstack.append(vfraction(queslist[i - 1]))
                requesstack.append(queslist[i])
                continue
            else:
                deal = random.randint(1, 10)
                if deal < 2:  # 删
                    continue
                    # del queslist[i - 1]
                    # del queslist[i]
                elif deal > 1 and deal < 7:  # 增
                    # dd = random.randint(-1 * int(queslist[i - 1])+1, int(queslist[i - 1]))
                    add = random.randint(-1 * int(vfraction(queslist[i - 1])), int(vfraction(queslist[i - 1])))
                    queslist[i - 1] = str(vfraction(queslist[i - 1]) + add)
                    requeslist = requeslist + queslist[i - 1] + queslist[i]
                    requesstack.append(vfraction(queslist[i - 1]))
                    requesstack.append(queslist[i])
                else:
                    o, w = getoperators()
                    queslist[i] = o
                    requeslist = requeslist + queslist[i - 1] + queslist[i]
                    requesstack.append(vfraction(queslist[i - 1]))
                    requesstack.append(queslist[i])

    requeslist = requeslist + queslist[len(queslist) - 1]
    requesstack.append(vfraction(queslist[len(queslist) - 1]))
    # for i in range(0,len(requesstack)-1):
    # if requesstack[i]=='÷':
    # frac=Fraction(requesstack[i-1],requesstack[i+1])
    # requesstack[i-1]=frac.numerator
    # requesstack[i+1]=frac.denominator

    condition = 0
    while len(requesstack) > 1:
        for i in range(0, len(requesstack)):
            if requesstack[i] == '×':
                requesstack[i - 1] = requesstack[i - 1] * requesstack[i + 1]
                del requesstack[i]
                del requesstack[i]
                break
            elif requesstack[i:i] == '÷':
                requesstack[i - 1] = requesstack[i - 1] / requesstack[i + 1]
                del requesstack[i]
                del requesstack[i]
                break
            else:
                condition = 1
        if condition == 1:
            if len(requesstack) > 1:
                requesstack[0] = calculate(requesstack[0], requesstack[2], requesstack[1])
                del requesstack[1]
                del requesstack[1]
                # print question
                # print questionstack
    else:
        ans = requesstack[0]
    return requeslist, ans

def calcustr(ques):
    question = ques.encode('utf8')
    # print question
    queslist = []
    requeslist = ''
    requesstack = []
    k = 0
    for i in range(0, len(question) - 1):
        # print question[i:i+2]
        if question[i] == "+":  # 前处理
            queslist.append(question[k:i])
            queslist.append(question[i])
            k = i + 1
        elif question[i] == '-':
            queslist.append(question[k:i])
            queslist.append(question[i])
            k = i + 1
        elif question[i:i + 2] == '×':
            queslist.append(question[k:i])
            queslist.append(question[i:i + 2])
            k = i + 2
        elif question[i:i + 2] == '÷':
            queslist.append(question[k:i])
            queslist.append(question[i:i + 2])
            k = i + 2
    queslist.append(question[k:len(question)])
    for i in range(0, len(queslist) - 1):
        # print i
        if queslist[i] == '+' or queslist[i] == '-' or queslist[i] == '×' or queslist[i] == '÷':
            queslist[i-1]=vfraction(queslist[i-1])
    queslist[len(queslist)-1]=vfraction(queslist[len(queslist) - 1])
    condition = 0
    while len(requesstack) > 1:
        for i in range(0, len(requesstack)):
            if requesstack[i] == '×':
                requesstack[i - 1] = requesstack[i - 1] * requesstack[i + 1]
                del requesstack[i]
                del requesstack[i]
                break
            elif requesstack[i:i] == '÷':
                requesstack[i - 1] = requesstack[i - 1] / requesstack[i + 1]
                del requesstack[i]
                del requesstack[i]
                break
            else:
                condition = 1
        if condition == 1:
            if len(requesstack) > 1:
                requesstack[0] = calculate(requesstack[0], requesstack[2], requesstack[1])
                del requesstack[1]
                del requesstack[1]
                # print question
                # print questionstack
    else:
        ans = requesstack[0]
    return ans

def replaceques(ques):
    con=0
    if '(' in ques:
        con=1
    if con==0:
        requeslist,ans=replacestr(ques,'')
    elif con==1:
        k1=ques.find('(')
        k2=ques.find(')')
        quesin=ques[k1+1:k2]
        questem,anstem=replacestr(quesin,' ')
        if '-' not in str(anstem):
            quesin = '(' + quesin + ')'
            ques = ques.replace(quesin, str(anstem))
            requeslist, ans = replacestr(ques, str(anstem))
            questem = '(' + questem + ')'
            requeslist = requeslist.replace(str(anstem), questem)
        else:
            requeslist=questem
            ans=anstem

    return requeslist,ans
#(9×4/9×2/7-6-6×1/2)+2/5
#a='(3/5+2/3×6×2/9÷9-8-1/2)×8'
#list,ans=replaceques(a)
#print list
#print ans
#for i in range(0,len(a)):
    #print a[i]
#b=a[0:7]
#c=a[6:11]
#print b
#print c

def getoperatorslist(st):
    if st=="随机":
        list=['+','-','×','÷','+','-']
    elif st=="无乘":
        list = ['+', '-',  '÷', '+', '-']
    elif st=="无除":
        list = ['+', '-',  '×', '+', '-']
    elif st=="无加":
        list = ['×', '-',  '÷',  '-']
    elif st=="无减":
        list = ['+', '×',  '÷', '+']
    elif st=="仅乘除":
        list = ['×', '÷']
    elif st=="仅加减":
        list = ['+', '-']
    elif st=="连乘":
        list = ['×']
    elif st=="连除":
        list = ['÷']
    elif st=="连加":
        list = ['+']
    elif st=="连减":
        list = ['-']
    return list

def getlabeloperators(st):
    operatorslist=getoperatorslist((st))
    operators = random.choice(operatorslist)
    if operators == '×':
        length = 2
    elif operators == '÷':
        length = 2
    else:
        length = 1
    return operators, length

def getlabeloperands(st,range):
    if st=="随机":
        operandstype = random.randint(1, 2)
        degree = 0
        if operandstype == 1:
            operands = random.randint(1, range)
            operandsvalue = Fraction(operands, 1)
            operands = str(operands)
            degree = 1
            # print operands
        else:
            operands1 = random.randint(1, range)
            operands2 = random.randint(1, range)
            degree = 1.5
            if operands1 < operands2:
                operands1, operands2 = operands2, operands1
            if operands1 == operands2:
                operandsvalue = Fraction(1, 2)
                operands = '1/2'
            else:
                operandsvalue = Fraction(operands2, operands1)
                operands = str(Fraction(operands2, operands1))
    elif st=="整数":
        operands = random.randint(1, range)
        operandsvalue = Fraction(operands, 1)
        operands = str(operands)
        degree = 1
    elif st=="真分数":
        operands1 = random.randint(1, range)
        operands2 = random.randint(1, range)
        degree = 1.5
        if operands1 < operands2:
            operands1, operands2 = operands2, operands1
        if operands1 == operands2:
            operandsvalue = Fraction(1, 2)
            operands = '1/2'
        else:
            operandsvalue = Fraction(operands2, operands1)
            operands = str(Fraction(operands2, operands1))
    return operands, operandsvalue, degree

def getlabelquestionbyn(opestr,numstr,ran,n):
    symbolnumber = n
    question = ''
    questionstack = []
    ans = 0
    length_ques = 0

    for i in range(1, symbolnumber + 1):
        (op, va, de) = getlabeloperands(numstr, ran)
        operands = op
        value = va
        (operators, length) = getlabeloperators(opestr)
        question = question + operands + operators
        questionstack.append(value)
        questionstack.append(operators)
        length_ques = length_ques + length + de
    (op, va, de) = getlabeloperands(numstr, ran)
    operands = op
    value = va
    question = question + operands
    questionstack.append(value)
    length_ques = length_ques + de
    # print question
    # print questionstack
    condition = 0
    while len(questionstack) > 1:
        for i in range(0, len(questionstack)):
            if questionstack[i] == '×':
                questionstack[i - 1] = questionstack[i - 1] * questionstack[i + 1]
                del questionstack[i]
                del questionstack[i]
                break
            elif questionstack[i] == '÷':
                questionstack[i - 1] = questionstack[i - 1] / questionstack[i + 1]
                del questionstack[i]
                del questionstack[i]
                break
            else:
                condition = 1
        if condition == 1:
            if len(questionstack) > 1:
                questionstack[0] = calculate(questionstack[0], questionstack[2], questionstack[1])
                del questionstack[1]
                del questionstack[1]
                # print question
                # print questionstack
    else:
        ans = questionstack[0]
    return question, ans, length_ques

def getlabelquestion(opestr,numstr,ran):
    questiontype=random.randint(1,6)
    if questiontype<4:
        symbolnumber = random.randint(1, 5)
        question = ''
        questionstack = []
        ans = 0
        length_ques = 0

        for i in range(1, symbolnumber + 1):
            (op, va, de) = getlabeloperands(numstr, ran)
            operands = op
            value = va
            (operators, length) = getlabeloperators(opestr)
            question = question + operands + operators
            questionstack.append(value)
            questionstack.append(operators)
            length_ques = length_ques + length + de
        (op, va, de) = getlabeloperands(numstr, ran)
        operands = op
        value = va
        question = question + operands
        questionstack.append(value)
        length_ques = length_ques + de
        # print question
        # print questionstack
        condition = 0
        while len(questionstack) > 1:
            for i in range(0, len(questionstack)):
                if questionstack[i] == '×':
                    questionstack[i - 1] = questionstack[i - 1] * questionstack[i + 1]
                    del questionstack[i]
                    del questionstack[i]
                    break
                elif questionstack[i] == '÷':
                    questionstack[i - 1] = questionstack[i - 1] / questionstack[i + 1]
                    del questionstack[i]
                    del questionstack[i]
                    break
                else:
                    condition = 1
            if condition == 1:
                if len(questionstack) > 1:
                    questionstack[0] = calculate(questionstack[0], questionstack[2], questionstack[1])
                    del questionstack[1]
                    del questionstack[1]
                    # print question
                    # print questionstack
        else:
            ans = questionstack[0]
    else:
        n1=random.randint(1,5)
        n2=random.randint(1,3)
        n3=random.randint(1,5)
        symbolnumber = n1
        question = ''
        questionstack = []
        ans = 0
        length_ques = 0

        for i in range(1, symbolnumber + 1):
            if i==n3:
                (op,va,de)=getlabelquestionbyn(opestr,numstr,ran,n2)
                operands = op
                value = va
                (operators, length) = getlabeloperators(opestr)
                question = question +'('+ operands +')'+ operators
                questionstack.append(value)
                questionstack.append(operators)
                length_ques = length_ques + length + de
            else:
                (op, va, de) = getlabeloperands(numstr, ran)
                operands = op
                value = va
                (operators, length) = getlabeloperators(opestr)
                question = question + operands + operators
                questionstack.append(value)
                questionstack.append(operators)
                length_ques = length_ques + length + de

        (op, va, de) = getlabeloperands(numstr, ran)
        operands = op
        value = va
        question = question + operands
        questionstack.append(value)
        length_ques = length_ques + de
        # print question
        # print questionstack
        condition = 0
        while len(questionstack) > 1:
            for i in range(0, len(questionstack)):
                if questionstack[i] == '×':
                    questionstack[i - 1] = questionstack[i - 1] * questionstack[i + 1]
                    del questionstack[i]
                    del questionstack[i]
                    break
                elif questionstack[i] == '÷':
                    questionstack[i - 1] = questionstack[i - 1] / questionstack[i + 1]
                    del questionstack[i]
                    del questionstack[i]
                    break
                else:
                    condition = 1
            if condition == 1:
                if len(questionstack) > 1:
                    questionstack[0] = calculate(questionstack[0], questionstack[2], questionstack[1])
                    del questionstack[1]
                    del questionstack[1]
                    # print question
                    # print questionstack
        else:
            ans = questionstack[0]

    return question, ans, length_ques

def getdiyoperators(list):
    operators = random.choice(list)
    list.remove(operators)
    if operators == '×':
        length = 2
    elif operators == '÷':
        length = 2
    else:
        length = 1
    return operators, length,list

def getdiyquestionbylist(list,numstr,ran):
    question = ''
    questionstack = []
    ans = 0
    length_ques = 0

    for i in range(1, len(list) + 1):
        (op, va, de) = getlabeloperands(numstr, ran)
        operands = op
        value = va
        (operators, length, list1) = getdiyoperators(list)
        list = list1
        question = question + operands + operators
        questionstack.append(value)
        questionstack.append(operators)
        length_ques = length_ques + length + de
    (op, va, de) = getlabeloperands(numstr, ran)
    operands = op
    value = va
    question = question + operands
    questionstack.append(value)
    length_ques = length_ques + de
    # print question
    # print questionstack
    condition = 0
    while len(questionstack) > 1:
        for i in range(0, len(questionstack)):
            if questionstack[i] == '×':
                questionstack[i - 1] = questionstack[i - 1] * questionstack[i + 1]
                del questionstack[i]
                del questionstack[i]
                break
            elif questionstack[i] == '÷':
                questionstack[i - 1] = questionstack[i - 1] / questionstack[i + 1]
                del questionstack[i]
                del questionstack[i]
                break
            else:
                condition = 1
        if condition == 1:
            if len(questionstack) > 1:
                questionstack[0] = calculate(questionstack[0], questionstack[2], questionstack[1])
                del questionstack[1]
                del questionstack[1]
                # print question
                # print questionstack
    else:
        ans = questionstack[0]
    return question, ans, length_ques

def getdiyquestion(list,numstr,ran,brastr):
    if brastr=="无":
        question = ''
        questionstack = []
        ans = 0
        length_ques = 0

        for i in range(1, len(list) + 1):
            (op, va, de) = getlabeloperands(numstr, ran)
            operands = op
            value = va
            (operators, length, list1) = getdiyoperators(list)
            list = list1
            question = question + operands + operators
            questionstack.append(value)
            questionstack.append(operators)
            length_ques = length_ques + length + de
        (op, va, de) = getlabeloperands(numstr, ran)
        operands = op
        value = va
        question = question + operands
        questionstack.append(value)
        length_ques = length_ques + de
        # print question
        # print questionstack
        condition = 0
        while len(questionstack) > 1:
            for i in range(0, len(questionstack)):
                if questionstack[i] == '×':
                    questionstack[i - 1] = questionstack[i - 1] * questionstack[i + 1]
                    del questionstack[i]
                    del questionstack[i]
                    break
                elif questionstack[i] == '÷':
                    questionstack[i - 1] = questionstack[i - 1] / questionstack[i + 1]
                    del questionstack[i]
                    del questionstack[i]
                    break
                else:
                    condition = 1
            if condition == 1:
                if len(questionstack) > 1:
                    questionstack[0] = calculate(questionstack[0], questionstack[2], questionstack[1])
                    del questionstack[1]
                    del questionstack[1]
                    # print question
                    # print questionstack
        else:
            ans = questionstack[0]
    elif brastr=="有":
        n1=random.randint(1,len(list)-1)
        n2=len(list)-n1
        n3=random.randint(1,n2)
        list_in=[]
        for i in range(1,n1+1):
            kop=random.choice(list)
            list_in.append(kop)
            list.remove(kop)

        question = ''
        questionstack = []
        ans = 0
        length_ques = 0

        for i in range(1, n2 + 1):
            if i==n3:
                (op,va,de)=getdiyquestionbylist(list_in,numstr,ran)
                operands = op
                value = va
                (operators, length, list1) = getdiyoperators(list)
                list = list1
                question = question + '('+operands+')' + operators
                questionstack.append(value)
                questionstack.append(operators)
                length_ques = length_ques + length + de
            else:
                (op, va, de) = getlabeloperands(numstr, ran)
                operands = op
                value = va
                (operators, length, list1) = getdiyoperators(list)
                list = list1
                question = question + operands + operators
                questionstack.append(value)
                questionstack.append(operators)
                length_ques = length_ques + length + de
        (op, va, de) = getlabeloperands(numstr, ran)
        operands = op
        value = va
        question = question + operands
        questionstack.append(value)
        length_ques = length_ques + de
        # print question
        # print questionstack
        condition = 0
        while len(questionstack) > 1:
            for i in range(0, len(questionstack)):
                if questionstack[i] == '×':
                    questionstack[i - 1] = questionstack[i - 1] * questionstack[i + 1]
                    del questionstack[i]
                    del questionstack[i]
                    break
                elif questionstack[i] == '÷':
                    questionstack[i - 1] = questionstack[i - 1] / questionstack[i + 1]
                    del questionstack[i]
                    del questionstack[i]
                    break
                else:
                    condition = 1
            if condition == 1:
                if len(questionstack) > 1:
                    questionstack[0] = calculate(questionstack[0], questionstack[2], questionstack[1])
                    del questionstack[1]
                    del questionstack[1]
                    # print question
                    # print questionstack
        else:
            ans = questionstack[0]
    return question, ans, length_ques
