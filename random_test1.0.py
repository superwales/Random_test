import random
import time
from fractions import Fraction
#getsymbol函数，返回一个运算符号
def getoperators():
    operatorslist=('+','-','*','/','+','-')
    operators=random.choice(operatorslist)
    if operators=='*':
        length=2
    elif operators=='/':
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
    elif op=='*':
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
            operands='(1/2)'
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
    return question,ans,length_ques

#确定题目的个数和运算范围
questionnumber=int(raw_input('请输入题目的个数：'))
ran=int(raw_input('请输入运算范围：'))
questionlist=[]#题目存在一个列表中
anslist=[]#答案存在一个列表中
lengthlist=[]#权重存在一个列表中
scorelist=[]#分数存在一个列表中
totalscore=0
questionfile=file('questionlist.txt','w')
#根据输入的题目个数生成题目清单，每一个新生成的题会与现有题进行比较，重复不则重新生成
#将生成的题目写入文件中，便于查看与打印
while len(questionlist)<questionnumber:
    (question,ans,length)=getquestion(ran)
    cond=0
    for element in questionlist:
        if element==question:
            cond=1
    if cond==0:
        questionlist.append(question)
        anslist.append(ans)
        lengthlist.append(length)
        totalscore=totalscore+length
        questionfile.write(question+'\n')
questionfile.close()
print '题目已经生成完毕！'
#根据权重分配分值
for i in range(0,len(lengthlist)):
    scorelist.append(round(lengthlist[i]*100/totalscore))         
grade=0
print '本次答题开始！共',questionnumber,'题，总分100分，答题时间45分钟！'
time_start=time.time()
for i in range(0,questionnumber):
    print'第',i+1,'题是：'
    print questionlist[i],'='
    print'分值为',scorelist[i],'分'
    print '答案是：',anslist[i]
    ans_user=raw_input('请输入你的答案：')
    print '您的答案是：',ans_user
    if ans_user==str(anslist[i]):
        print'回答正确！'
        grade=grade+scorelist[i]
    else:
        print'回答错误！'
time_end=time.time()
time_use=time_end-time_start
#这里设置一个题目权重与时间花费的关系k，默认为1
k=1
if time_use<totalscore*k:
    grade=grade
else:
    grade=round(totalscore*grade/time_use)
print '答题结束！您本次的得分为：',grade,'分'

