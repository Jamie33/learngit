
# Print Function

https://www.hackerrank.com/challenges/python-print/problem

打印出123...N 之间的整数

<span class="girk">方法一</span> 用 for 循环依次打印出


```python
n = 3
for i in range(1,n+1):
    print(i,end='')
print('')
```

    123


<span class="girk">方法二</span> 用 print 内置函数的参数


```python
n=3
print(*range(1, n+1), sep='')  
```

    123


<h2>print()函数</h2>
<span class="mark">知识点</span>  print(\*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

objects -- object 复数形式，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。

sep -- 用来间隔多个对象，默认值是一个空格。

end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。

file -- 要写入的文件对象。

\*objects -- 表示可以用可变参数

在函数调用时，在 str/list/tuple/range 参数前加 \*，意思是把 str/list/tuple/range 序列中的元素一个一个传到函数里面






```python
a = '123456'
b = ['1','2','3','4','5','6']
c = ('1','2','3','4','5','6')
d = range(1,7)

print(*a)
print(*b)
print(*c)
print(*d)

print('ju','p','t','er',sep='-')
print(*['ju','p','t','er'],sep='-')
print(*('ju','p','t','er'),sep='-')
print(*(range(1,7)),sep='-')
```

    1 2 3 4 5 6
    1 2 3 4 5 6
    1 2 3 4 5 6
    1 2 3 4 5 6
    ju-p-t-er
    ju-p-t-er
    ju-p-t-er
    1-2-3-4-5-6


# Lists

https://www.hackerrank.com/challenges/python-lists/problem

根据输入执行相应的命令

<span class="girk">方法一</span>  if...elif


```python
# 正常思路

L = []
N = int(input())
   
for i in range(N):
    c = input().split(' ')
    for i in range(1,len(c)):
        c[i] = int(c[i])
    command = c[0]
        
    if command == 'insert':
        L.insert(c[1],c[2])
    elif command == 'print':
        print(L)
    elif command == 'remove':
        L.remove(c[1])
    elif command == 'append':
        L.append(c[1])
    elif command == 'extend':
        L.extend(c[1:])
    elif command == 'sort':
        L.sort()
    elif command == 'pop':
        L.pop()
    elif command == 'reverse':
        L.reverse()
```

    2
    append 9
    print
    [9]


<span class="girk">方法二</span>  eval()


```python
#简化

n = int(input())
l = []
for i in range(n):
    c = input().split()
    command = c[0]
    if len(c) > 0:
        args = c[1:]
    print(args)
    if command !="print":
        command += "("+ ",".join(args) +")"
        eval("l."+command)
    else:
        print(l)
```

    2
    append 9
    ['9']
    print
    []
    [9]


<h2>join() 函数</h2>

<span class="mark">知识点</span> 'sep'.join(seq)

将字符串、列表、元组、字典中的元素以指定的字符(分隔符)连接生成一个新的字符串,

sep -- 分隔符。可以为空

seq -- 要连接的元素序列:字符串、列表、元组、字典。

以sep作为分隔符，将seq所有的元素合并成一个新的字符串。返回一个以分隔符sep连接各个元素后生成的字符串


```python
#seq内元素只能是可迭代字符串类型，数字不可以

#对字符串进行操作
seq1 = 'HelloWorldIamaprogrammer'
print((' ').join(seq1))

#对列表进行操作
seq2 = ['Hello','World','I','am','a','programmer']
print((' ').join(seq2))

#对元祖进行操作
seq3 = ('Hello','World','I','am','a','programmer')
print(('：').join(seq3))

#对字典进行操作
seq4 = {'hello':1,'world':2,'I':3,'am':4,'a':5,'programmer':6}
print(('-').join(seq4))


#seq内元素数量的不同，结果不同

#元素有2或多个个

num3 = ['9','9','9']
print((',').join(num3))

#元素只有1个,结果没有分隔符

num1 =['9']
print((',').join(num1))

#应用：合并参数

print('('+','.join(['0', '5'])+')')
print('('+','.join(['0'])+')')
```

    H e l l o W o r l d I a m a p r o g r a m m e r
    Hello World I am a programmer
    Hello：World：I：am：a：programmer
    hello-world-I-am-a-programmer
    9,9,9
    9
    (0,5)
    (0)


<h2>eval()函数</h2>
<span class="mark">知识点</span>  eval()函数  

将字符串str当成有效的表达式来求值并返回计算结果。所以，结合math当成一个计算器很好用。


```python
#计算字符串中有效的表达式
print(eval('pow(2,2)'))
print(eval('2+2'))

#将字符串转成相应的对象（如list、tuple、dict和string之间的转换）
a="[[1,2], [3,4], [5,6], [7,8], [9,0]]"
b="(1,2,3,4)"
c="{1:'xx',2:'yy'}"

print(eval(a))
print(eval(b))
print(eval(c))
```

    4
    4
    [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
    (1, 2, 3, 4)
    {1: 'xx', 2: 'yy'}


# List Comprehensions

https://www.hackerrank.com/challenges/list-comprehensions/problem

根据要求属于三维坐标

<span class="girk">方法一</span> for 循环


```python
# 正常思路
x = int(input())
y = int(input())
z = int(input())
n = int(input())
l = []
for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if a+b+c != n:
                l.append([a,b,c])
print(l)
```

    1
    1
    1
    2
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


<span class="girk">方法二</span> 简化方法


```python
# 简化4次input，列表生成式
x,y,z,n = [int(input()) for i in range(4)]
l = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if (a+b+c) != n]

print(l)
```

    1
    1
    1
    2
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


# Find the Runner-Up Score!

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/editorial

找到列表中第二大的数字

<span class="girk">方法一</span> 用 set() , sorted()


```python
n = int(input())
l = set(map(int,input().split()))
print(sorted(l)[-2])
```

    5
    2 3 6 6 5
    5


<span class="girk">方法二</span>  不用 set() , sorted()


```python
#最基本的算法
n = int(input())
l = list(map(int,input().split()))
maximum = max(l)
m = -999999
for i in l:
    if i > m and i != maximum:
        m = i
   
print(m)
```

    5
    2 3 6 6 5
    5


<span class="girk">方法三</span>  collections.Counter() 


```python
from collections import Counter
n = int(input())
l = Counter(map(int,input().split())).keys()
sorted(l)[-2]
```

    5
    2 3 6 6 5





    5



<span class="girk">方法四</span>  函数


```python
l = [2, 3, 6, 1, 5]
# 列表最大值
def maximum(l): 
    d = -9999999
    for i in l:
        if i > d:
            d = i
    return(d)

#maximum(l)

#列表第二大值
def second(l): 
    m = maximum(l)
    e = -9999999
    for i in l:
        if (i > e) and (i != m):
            e = i
    return(e)

second(l)

```




    5



<span class="girk">拓展</span>  求列表最大值


```python
# 列表最大值
from functools import reduce
def get_max(x,y):
    if x > y:
        return x
    else:
        return y
l = [2, 3, 6, 1, 5]
reduce(get_max,l)

#简化
from functools import reduce
reduce(lambda x,y:x if x>y else y,l)
```




    6



# Nested Lists

https://www.hackerrank.com/challenges/nested-list/problem

找到成绩排名第二的学生

<span class="girk">第一种</span>   用字典


```python
#创建数据
students = []  
for i in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
print(students)

#简化
students=[[input(),float(input())] for i in range(int(input()))]
```

    5
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39
    [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]



```python
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
c = dict(students)
print(c)
second = sorted(set(c.values()))[1]
s = [i[0] for i in students if i[1] == second]

#第一种打印方式
for i in sorted(s):
    print(i)

#第二种打印方式    
print('\n'.join(sorted(s)))
```

    {'Harry': 37.21, 'Berry': 37.21, 'Tina': 37.2, 'Akriti': 41.0, 'Harsh': 39.0}
    Berry
    Harry
    Berry
    Harry


<span class="girk">第二种</span>   不用字典 简化


```python
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

second = sorted(set([i[1] for i in students]))[1]
for i in sorted([i[0] for i in students if i[1] == second]):
    print(i)
```

    Berry
    Harry


<span class="girk">第三种</span>   


```python
#第三种方法
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

second_highest = sorted(set([y for x,y in students]))[1]
print('\n'.join([a for a,b in sorted(students) if b == second_highest]))
```

    Berry
    Harry


<h2>迭代嵌套列表</h2>
<span class="burk">知识点</span>  迭代嵌套列表


```python
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
a = []
b = []
for i,x in students:
    a.append(i)
    b.append(x)
print(a)
print(b)

c = [['Harry', 37.21,3], ['Berry', 37.21,2], ['Tina', 37.2,1], ['Akriti', 41.0,4], ['Harsh', 39.0,4]]
print([z for x,y,z in c])
```

    ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
    [37.21, 37.21, 37.2, 41.0, 39.0]
    [3, 2, 1, 4, 4]


<h2>通过字典的value获取其key</h2>
<span class="burk">知识点</span>  通过字典的value获取其key,这个方法只适合没有相同value的字典


```python
d = {'a':'001', 'b':'002'}
list(d.keys())[list(d.values()).index("001")]
#index() 函数用于从列表中找出某个值第一个匹配项的索引位置。

#？？？如果要获取所有的索引位置
```




    'a'



# Finding the percentage

https://www.hackerrank.com/challenges/finding-the-percentage/problem

把学生和3门成绩的平均值一起存在字典中


```python
#创建数据
n = int(input())
d = {}
for i in range(n):
    text = input().split()
    d[text[0]] = list(map(float,text[1:])) #d[text[0]] = [float(i) for i in text[1:]]
print(d)
```

    3
    Krishna 67 68 69 
    Arjun 70 98 63 
    Malika 52 56 60
    {'Krishna': [67, 68, 69], 'Arjun': [70, 98, 63], 'Malika': [52, 56, 60]}



```python
scores = {'Krishna': [67, 68, 69], 'Arjun': [70, 98, 63], 'Malika': [52, 56, 60]}
name = input()
sum = 0
for i in scores[name]:
    sum += i
    average_score = sum/len(scores[name])
print('{:.2f}'.format(average_score))
```

    Krishna
    68.00



```python
# 把学生和3门成绩的平均值一起存在字典中

n = int(input())

d = {}
for i in range(n):
    text = input().split()
    d[text[0]] ='{:.2f}'.format(sum((map(float,text[1:]))/3)
print(d[input()])
```

    3
    Krishna 67 68 69 
    Arjun 70 98 63 
    Malika 52 56 60
    Krishna
    68.00



```python
s = 'HackerRan.' 
def swap_case(s):
    for i in s:
       
        if i.islower():
            i.upper()
        else :
            i.lower()
        
    return s

swap_case(s)

#没有任何改变
#因为字符串是不可变类型，而且方法有返回值的，一定要储存，要不然就白弄了
```




    'HackerRan.'




```python
s = 'HackerRan.' 
S = []
def swap_case(s):
    for i in s:
       
        if i.islower():
            S.append(i.upper())
        else :
            S.append(i.lower())
        
    return ''.join(S)

swap_case(s)
```




    'hACKERrAN.'




```python
[for i in s if]
```


```python
s.swapcase()
```




    'hACKERrAN.'



# String Formatting
https://www.hackerrank.com/challenges/python-string-formatting/problem


```python
#第一种方法

n = 17
width = len(bin(n)[2:])
for i in range(1,n+1):
    print(str(i).rjust(width),str(oct(i))[2:].rjust(width),str(hex(i))[2:].upper().rjust(width),str(bin(i))[2:].rjust(width))
    
```

        1     1     1     1
        2     2     2    10
        3     3     3    11
        4     4     4   100
        5     5     5   101
        6     6     6   110
        7     7     7   111
        8    10     8  1000
        9    11     9  1001
       10    12     A  1010
       11    13     B  1011
       12    14     C  1100
       13    15     D  1101
       14    16     E  1110
       15    17     F  1111
       16    20    10 10000
       17    21    11 10001



```python
#第二种方法
n = 17
width = len(bin(n))-2
for i in range(1,n+1):
    print('{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}'.format(i,width = width))
```

        1     1     1     1
        2     2     2    10
        3     3     3    11
        4     4     4   100
        5     5     5   101
        6     6     6   110
        7     7     7   111
        8    10     8  1000
        9    11     9  1001
       10    12     a  1010
       11    13     b  1011
       12    14     c  1100
       13    15     d  1101
       14    16     e  1110
       15    17     f  1111
       16    20    10 10000
       17    21    11 10001


# Alphabet Rangoli
https://www.hackerrank.com/challenges/alphabet-rangoli/problem


```python
n = 5
alpha = [chr(i) for i in range(97,123)]
print(alpha)

#top corn
for i in range(n-1,-1,-1):
    print(+alpha[i].center(4*n-3,'-')+)  

#middle belt
print(alpha[0].center(4*n-3,'-'))  
#below corn
for i in range(n):
    print(alpha[i].center(4*n-3,'-'))  
```

    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    --------e--------
    --------d--------
    --------c--------
    --------b--------
    --------a--------
    --------a--------
    --------a--------
    --------b--------
    --------c--------
    --------d--------
    --------e--------



```python
n = 5
a = 'a-'

#top corn

for i in range(0,2*n-2,2):
    print((a*(i+1)).center(4*n-3,'-'))  

#middle belt

print(((a*(2*n-1)).center(4*n-3,'-').rstrip('-')))  

#below corn

for i in range(2*n-4,-2,-2):
   print((a*(i+1)).center(4*n-3,'-'))
```

    --------a--------
    ------a-a-a------
    ----a-a-a-a-a----
    --a-a-a-a-a-a-a--
    a-a-a-a-a-a-a-a-a
    --a-a-a-a-a-a-a--
    ----a-a-a-a-a----
    ------a-a-a------
    --------a--------



```python
n = 5
icon = 'e-'

alpha = [chr(i) for i in range(97,123)]


for i in range(5):
    s  = alpha[i:n]
    b = alpha[i+1:n]
    line = ('-').join(s[::-1]+b)
    print(line.center(4*n-3,'-'))
    

```

    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------



```python
#方法一
n = 5

alpha = [chr(i) for i in range(97,123)]
line = []

for i in range(5):
    rstr  = alpha[i:n]
    lstr = alpha[i+1:n]
    line.append('-'.join(lstr[::-1]+rstr))
print(line)


for l in line[:0:-1]:
    print(l.center(4*n-3,'-'))
    
for l in line:
    print(l.center(4*n-3,'-'))
```

    ['e-d-c-b-a-b-c-d-e', 'e-d-c-b-c-d-e', 'e-d-c-d-e', 'e-d-e', 'e']
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------



```python
#方法二
n = 5

alpha = [chr(i) for i in range(97,123)]
line = []

for i in range(5):
    s = '-'.join(alpha[i:n])
    print(s)
    line.append((s[::-1]+s[1:]).center(4*n-3,'-'))
print(line)
print('\n'.join(line[:1:-1]+line))
print('\n'.join(line[-1:1:-1]+line))
print('\n'.join(line[:-4:-1]+line))
print('\n'.join(line[-1:-4:-1]+line))
```

    a-b-c-d-e
    b-c-d-e
    c-d-e
    d-e
    e
    ['e-d-c-b-a-b-c-d-e', '--e-d-c-b-c-d-e--', '----e-d-c-d-e----', '------e-d-e------', '--------e--------']
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------



```python
name = 'chris alan'
for n in name.split(' '):
    print(n.capitalize(),end=' ')
```

    Chris Alan 


```python
(' ').join([n.capitalize() for n in name.split(' ')])
```




    'Chris Alan'



<h2>title() 与 capitalize() 的区别</h2>

capitalize()与title()都可以实现字符串首字母大写.

主要区别在于：
capitalize(): 字符串第一个字母大写
title(): 字符串内的所有单词的首字母大写



```python
# 字母开头的情况

str='huang bi quan'
print(str.capitalize())       #第一个字母大写  
print(str.title())  #所有单词的首字母大写


#非字母开头的情况

str='深圳luohu'
print(str.capitalize())              #输出内容不变
print(str.title())           #第一个字母大写

```

    Huang bi quan
    Huang Bi Quan
    深圳luohu
    深圳Luohu



```python
print('title()方法')
a = 'abcd'
print(a.title())

b = '12abcd'
print(b.title())

c = 'ab cd'
print(c.title())

print('capitalize()方法')
d = 'abcd'
print(d.capitalize())

e = '12abcd'
print(e.capitalize())

f = 'ab cd'
print(f.capitalize())
```

    title()
    Abcd
    12Abcd
    Ab Cd
    capitalize()
    Abcd
    12abcd
    Ab cd


# The Minion Game 
https://www.hackerrank.com/challenges/the-minion-game/problem


```python
#方法一  但是当string很多的时候，就不行了
string = 'BANANA'
S_score = 0
K_score = 0
vowel = 'AEIOU'

for cut_len in range(len(string)):
    for s in range(len(string)):
        if len(string[s:s+cut_len+1]) == cut_len+1:
            if string[s:s+cut_len+1][0] in vowel:
                K_score += 1
            else:
                S_score += 1
      
if S_score > K_score:
    print('Stuart',S_score)
elif S_score < K_score:
    print('Kevin',K_score)
elif S_score == K_score:
    print('Draw')
```

    Stuart 12



```python
#方法二
string = 'BANANA'
S_score = 0
K_score = 0
vowel = 'AEIOU'

for i in range(len(string)):
    if string[i] in vowel:
        K_score += len(string) - i
    else:
        S_score += len(string) - i
        
if S_score > K_score:
    print('Stuart',S_score)
elif S_score < K_score:
    print('Kevin',K_score)
elif S_score == K_score:
    print('Draw')
```

    Stuart 12



```python
string = 'BANANA'
combstr = []
for i in range(len(string)):
    combstr.append(string[i:])
    combstr.append(string[:i+1])
    combstr.append(string[i])
    
    
print(set(combstr))
print(len(combstr))
```

    {'N', 'BA', 'B', 'NANA', 'BANAN', 'ANA', 'ANANA', 'BANA', 'BANANA', 'NA', 'BAN', 'A'}
    18



```python
string = 'BANANA'
substrings = []

for cut_len in range(len(string)):
    for s in range(len(string)):
        if len(string[s:s+cut_len+1]) == cut_len+1:
            substrings.append(string[s:s+cut_len+1])

substrings = set(substrings)
print(substrings)
print(len(substrings))

palyers = {'Stuart':[],'Kevin':[]}

vowel = 'AEIOU'
for i in substrings:
    if i[0] in vowel:
        palyers['kevin'].append(i)
    else:
        palyers['Stuart'].append(i)
print(palyers)
```

    {'ANAN', 'N', 'BA', 'B', 'NANA', 'BANAN', 'ANA', 'BANA', 'ANANA', 'AN', 'NAN', 'BANANA', 'NA', 'BAN', 'A'}
    15
    {'Stuart': ['N', 'BA', 'B', 'NANA', 'BANAN', 'BANA', 'NAN', 'BANANA', 'NA', 'BAN'], 'Kevin': ['ANAN', 'ANA', 'ANANA', 'AN', 'A']}



```python
string = 'BANANA'
substrings = []

for cut_len in range(len(string)):
    for s in range(len(string)):
        if len(string[s:s+cut_len+1]) == cut_len+1:
            substrings.append(string[s:s+cut_len+1])

print(substrings)

Stuart = []
Kevin = []
vowel = 'AEIOU'
for i in substrings:
    if i[0] in vowel:
        Kevin.append(i)
    else:
        Stuart.append(i)

from collections import Counter


S_dict = dict(Counter(Stuart))
K_dict = dict(Counter(Kevin))

S_score = 0
K_score = 0

for v in S_dict.values():
        S_score += v

for v in K_dict.values():
        K_score += v
        
print(S_score,K_score)

if S_score > K_score:
    print('Stuart',S_score)
elif S_score < K_score:
    print('Kevin',K_score)
elif S_score == K_score:
    print('Draw')
```

    ['B', 'A', 'N', 'A', 'N', 'A', 'BA', 'AN', 'NA', 'AN', 'NA', 'BAN', 'ANA', 'NAN', 'ANA', 'BANA', 'ANAN', 'NANA', 'BANAN', 'ANANA', 'BANANA']
    12 9
    Stuart 12



```python
#按照长度切分字符串，变成n个子字符串
string = 'BANANA'

def cut_word(n,string):
    substrings = []
    for i in range(len(string)):
        if len(string[i:i+n]) == n:
            substrings.append(string[i:i+n])
    print(substrings)
    
for n in range(len(string)):
    cut_word(n+1,string)
```

    ['B', 'A', 'N', 'A', 'N', 'A']
    ['BA', 'AN', 'NA', 'AN', 'NA']
    ['BAN', 'ANA', 'NAN', 'ANA']
    ['BANA', 'ANAN', 'NANA']
    ['BANAN', 'ANANA']
    ['BANANA']



```python
#切分子字符串
string = 'BANANA'

def cut_word(string):
    substrings = []
    for n in range(len(string)):
        for i in range(len(string)):
            if len(string[i:i+n+1]) == n+1:
                substrings.append(string[i:i+n+1])
    print(substrings)
    
cut_word(string)
```

    ['B', 'A', 'N', 'A', 'N', 'A', 'BA', 'AN', 'NA', 'AN', 'NA', 'BAN', 'ANA', 'NAN', 'ANA', 'BANA', 'ANAN', 'NANA', 'BANAN', 'ANANA', 'BANANA']



```python
s = 'BANANA'
vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print "Kevin", kevsc
elif kevsc < stusc:
    print "Stuart", stusc
else:
    print "Draw"
```

# Merge the Tools!
https://www.hackerrank.com/challenges/merge-the-tools/problem


```python
string = 'AABCAAADA'
k = 3
cut_len = int(len(string)/k)
cut_word = []
for i in range(0,len(string),cut_len):
        cut_word.append(string[i:i+cut_len])
print(cut_word)
```

    ['AAB', 'CAA', 'ADA']



```python
string = 'AABCAAADA'
s = list(string)
k = 3
split_number = int(len(string)/k)
i = 0
while i < len(s)-1:
    if s[i] == s[i+1]:
        del s[i]
    else:
        i += 1


```

    ['A', 'B', 'C', 'A', 'D', 'A']



```python
9/3
```




    3.0




```python
#方法一
string = 'AABCAAADA'
k = 3

for i in range(0,len(string),k):
        s = []
        for item in string[i:i+k]:
            if item not in s:
                s.append(item)
        print(''.join(s))
```

    AB
    CA
    AD


<h2>列表生成式理解出错的例子</h2>


```python
string = 'AABCAAADA'
k = 3
s = []

for item in string:
    if item not in s:
        s.append(item)
print(s)

#我们把上面的代码块简化成下面的
a = []
print([item for item in string if item not in a]) #2

#但是结果却不一样，原因在哪里？
'''
#2处，因为比较的a列表中一直都是空的，所以条件一直都是True
'''

# 或者这样
r = []
print([r.append(item) for item in string if item not in r])
#由于 append()方法无返回值，所以打印出的是none
print(r)
```

    ['A', 'B', 'C', 'D']
    ['A', 'A', 'B', 'C', 'A', 'A', 'A', 'D', 'A']
    [None, None, None, None]
    ['A', 'B', 'C', 'D']



```python
#方法二
string = 'AABCAAADA'
k = 3
for part in zip(*[iter(string)] * k):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
    print(d)
```

    AB
    {'A': 'A', 'B': 'B'}
    CA
    {'C': 'C', 'A': 'A'}
    AD
    {'A': 'A', 'D': 'D'}


<h2> dict.setdefault(key, default=None)</h2>

Python 字典 setdefault() 方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。

参数
key -- 查找的键值。
default -- 键不存在时，设置的默认键值。

返回值
如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。

<h2> dict.get(key, default=None)</h2>

Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值。

参数
key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值值。

返回值
返回指定键的值，如果值不在字典中返回默认值 None。


```python
a = {'A': 'A', 'B': 'B'}

print(a.get('A','NA'))
print(a.get('C','NA'))
print(a)
print(a.setdefault('A','NA'))
print(a.setdefault('C','NA'))
print(a)
```

    A
    NA
    {'A': 'A', 'B': 'B'}
    A
    NA
    {'A': 'A', 'B': 'B', 'C': 'NA'}


<h2>iter()函数</h2>

凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数



<h2>iterator 对象 迭代器</h2>

可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。


<h2>zip(*iterables)函数</h2>
https://docs.python.org/3/library/functions.html#zip

Python3中的zip函数可以把两个或者两个以上的迭代器封装成生成器，这种zip生成器会从每个迭代器中获取该迭代器的下一个值，然后把这些值组装成元组（tuple）。这样，zip函数就实现了平行地遍历多个迭代器。

如果输入的迭代器长度不同，那么，只要有一个迭代器遍历完，zip就不再产生元组了，zip会提前终止，这可能导致意外的结果，不可不察。

zip(*[iter(s)]*n)将数据序列聚类为n长度组的习语成为可能。这重复了相同的迭代器n次，以使每个输出元组具有对迭代器的n次调用的结果。这具有将输入划分为n个长块的效果。

zip() 与 * 操作符一起可以用来 unzip 一个列表


```python
#很简洁地实现了同时遍历两个列表
list1 = ['a','b','c','d']
list2 = ['apple','boy','cat','dog']
for x,y in zip(list1,list2):
    print(x,'is',y)
```

    a is apple
    b is boy
    c is cat
    d is dog



```python
s = 'AABCAAADA'
i = iter(s)
print(list(zip(i,i,i))) 
#其中3个i都是指向同一个iterator对象，它的内容只能被消费一次，每next()调用一次，就到下一个数据
```

    [('A', 'A', 'B'), ('C', 'A', 'A'), ('A', 'D', 'A')]



```python
l = [1,2,3]
n = l*3
m = [l]*3
print(n)
print(m)
m[0][0]=9
print(m)
```

    [1, 2, 3, 1, 2, 3, 1, 2, 3]
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    [[9, 2, 3], [9, 2, 3], [9, 2, 3]]


<h2>list.sort() 方法 与 sorted() 函数</h2>

sorted(iterable,key=None,reverse=False)，返回新的列表，对所有可迭代的对象均有效

list.sort(key=None,reverse=False) 就地改变列表reverse：True反序；False 正序

sorted 和list.sort 都接受key, reverse定制。但是区别是。list.sort()是列表中的方法，只能用于列表。而sorted可以用于任何可迭代的对象。list.sort()是在原序列上进行修改，不会产生新的序列。所以如果你不需要旧的序列，可以选择list.sort()。 sorted() 会返回一个新的序列。旧的对象依然存在。

# Symmetric Difference
https://www.hackerrank.com/challenges/symmetric-difference/problem


```python
M = '2 4 5 9'
N = '2 4 11 12'
M = set(map(int,M.split(' ')))
N = set(map(int,N.split(' ')))
for i in sorted(M^N):
    print(i)
```

    5
    9
    11
    12



```python
M = '2 4 5 9'
N = '2 4 11 12'
M = set(M.split(' '))
N = set(N.split(' '))
sym_dif = list(M^N)
print(sym_dif)
print(sorted(sym_dif))
print(sorted(sym_dif,key=int))
print('\n'.join(sorted(sym_dif,key=int)))
```

    ['11', '5', '9', '12']
    ['11', '12', '5', '9']
    ['5', '9', '11', '12']
    5
    9
    11
    12



```python
#方法一
m,M,n,N =[input() for i in range(4)]
M = set(map(int,M.split(' ')))
N = set(map(int,N.split(' ')))

for i in sorted(M^N):
    print(i)
    
#上面的for循环等同于下面的代码块
print(*sorted(M^N),sep='\n')
```

    4
    2 4 5 9
    4
    2 4 11 12
    5
    9
    11
    12
    5 9 11 12



```python
#方法二 简化
a,b = [set(input().split()) for i in range(4)][1::2]
print(*sorted(a^b, key=int), sep='\n')
```

    4 
    2 4 5 9 
    4
    2 4 11 12
    5
    9
    11
    12



```python
#方法三
a,b = [set(input().split()) for i in range(4)][1::2]
print ('\n'.join(sorted(a^b, key=int)))
```

    4  
    2 4 5 9  
    4 
    2 4 11 12
    5
    9
    11
    12


<h2> 'sep'.join(seq)</h2>
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组，里面的元素必须是字符串类型
如果是整数类型，
可以先把它转化为字符串类型  print('\n'.join(map(str,a)))
或者用 print(*a,sep='\n')


```python
a = ['5', '9', '11', '12']
print('\n'.join(a))
print(*a,sep='\n')

a = [5, 9, 11, 12]
print(*a,sep='\n')
#print('\n'.join(a)) 报错，因为a里面的元素是整数型
print('\n'.join(map(str,a))) #先把元素转化为字符串类型
```

    5
    9
    11
    12
    5
    9
    11
    12
    5
    9
    11
    12
    5
    9
    11
    12



```python
# 按照数字的大小，从小到大换行打印每一个元素
a = ['11', '12', '5', '9'] 

print('\n'.join(sorted(a,key = int)))

print(*(sorted(a,key=int)),sep='\n')
```

    5
    9
    11
    12
    5
    9
    11
    12


# No Idea!
https://www.hackerrank.com/challenges/no-idea/problem


```python
#方法一  如果序列太大了，太耗时了
n = 3
m = 2
arry = [1,5,3]
A = {3,1}
B = {5,7}
happiness = 0

for i in arry:
    if i in A:
        happiness += arry.count(i)
    elif i in B:
        happiness -= arry.count(i)
print(happiness)
```

    1



```python
#方法二 简化
n = 3
m = 2
arry = [1,5,3]
A = {3,1}
B = {5,7}
happiness = 0
count = []
for i in arry:
    if i in A:
        count.append(1)
    elif i in B:
        count.append(-1)
    else:
        count.append(0)
print(sum(count))
```

    1



```python
#方法三
n = 3
m = 2
arry = [1,5,3]
A = {3,1}
B = {5,7}
happiness = 0
count = []
for i in arry:
    count.append((i in A) - (i in B))
print(count)
```

    [1, -1, 1]



```python
print(int(True))
print(int(False))
```

    1
    0



```python
n,m = list(map(int,input().split(' ')))
arry = list(map(int,input().split(' ')))
A = set(map(int,input().split(' ')))
B = set(map(int,input().split(' ')))
print(n,m,arry,A,B)
```

    3 2
    1 5 3
    3 1
    5 7
    3 2 [1, 5, 3] {1, 3} {5, 7}



```python
n,m = input().split(' ')
arry = input().split(' ')
A = set(input().split(' '))
B = set(input().split(' '))
print(n,m,arry,A,B)
```

    3 2
    1 5 3
    3 1
    5 7
    3 2 ['1', '5', '3'] {'3', '1'} {'5', '7'}



```python
n = int(input())
country = set(input().strip() for i in range(n))
print(country,len(country))
```

    7
    UK  
    China 
    USA 
    France
    New Zealand
     UK 
    France
    {'France', 'China', 'USA', 'UK', 'New Zealand'} 5



```python
n = int(input())
s = set(map(int,input().split(' ')))
print(s)
```

    9
    1 2 3 4 5 6 7 8 9
    {1, 2, 3, 4, 5, 6, 7, 8, 9}



```python
Eng,Fre = (set(input().split(' ')) for i in range(2))
print(Eng,Fre)

print(Eng - Fre)
```

    1 2 3 4 5 6 7 8 9
    10 1 2 3 11 21 55 6 8
    {'6', '2', '5', '8', '3', ' ', '7', '9', '4', '1'} {'6', '2', '5', '0', '8', '3', ' ', '1'}
    {'4', '7', '9'}


# Set Mutations
https://www.hackerrank.com/challenges/py-set-mutations/problem

<span class="girk">方法一</span> if


```python
num_ele = input()
set_A = set(map(int,input().split(' ')))
num = int(input())
for i in range(num):
    command = input().split(' ')[0]
    set_a = set(map(int,input().split(' ')))
    if command == 'intersection_update':
        set_A &= set_a
    if command == 'update':
        set_A |= set_a
    if command == 'symmetric_difference_update':
        set_A ^= set_a
    if command == 'difference_update':
        set_A -= set_a
print(sum(set_A))
```

    16
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
    {'10', '2', '12', '7', '11', '4', '13', '6', '3', '8', '1', '14', '52', '24', '5', '9'}
    1
    intersection_update 10
    2 3 5 6 8 9 1 4 7 11
    {'2', '7', '11', '4', '8', '6', '3', '1', '5', '9'}
    10


<span class="girk">方法二</span> getattr()


```python
num_ele = input()
set_A = set(input().split(' '))
num = int(input())
for i in range(num):
    command = input().split(' ')[0]
    set_a = set(input().split(' '))
    getattr(set_A,command)(set_a)
print(sum(map(int,set_A)))
```

<h2>getattr()</h2>

getattr(object, name[,default])
获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
可以在后面添加一对括号。


```python
class test():
    name = 'hackerrank'
    def run(self):
        return 'Hello Hackerrank'

t = test()
print(getattr(t,'name')) #获取name属性，存在就打印出来
print(getattr(t,'run')) #获取run方法，存在就打印出方法的内存地址
getattr(t, 'run')()  #获取run方法，后面加括号可以将这个方法运行
print(getattr(t, "age","18"))  #若属性不存在，返回一个默认值。
print(getattr(t, 'age'))  #获取一个不存在的属性
```

    hackerrank
    <bound method test.run of <__main__.test object at 0x000001C07C87F390>>
    18



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-11-7e96e4c12be7> in <module>()
          9 getattr(t, 'run')()  #获取run方法，后面加括号可以将这个方法运行
         10 print(getattr(t, "age","18"))  #若属性不存在，返回一个默认值。
    ---> 11 print(getattr(t, 'age'))  #获取一个不存在的属性
    

    AttributeError: 'test' object has no attribute 'age'


<h2>dir()</h2>

dir()函数可以查看对像内所有属于及方法，在python中任何东西都是对像，一种数据类型，一个模块等，都有自己的属性和方法，除了常用方法外，其它的你不需要全部记住它，交给dir()函数就好了。


```python
a = {1,2,3,4}
dir(a)
```




    ['__and__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__iand__',
     '__init__',
     '__init_subclass__',
     '__ior__',
     '__isub__',
     '__iter__',
     '__ixor__',
     '__le__',
     '__len__',
     '__lt__',
     '__ne__',
     '__new__',
     '__or__',
     '__rand__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__ror__',
     '__rsub__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__xor__',
     'add',
     'clear',
     'copy',
     'difference',
     'difference_update',
     'discard',
     'intersection',
     'intersection_update',
     'isdisjoint',
     'issubset',
     'issuperset',
     'pop',
     'remove',
     'symmetric_difference',
     'symmetric_difference_update',
     'union',
     'update']



# The Captain's Room
https://www.hackerrank.com/challenges/py-the-captains-room/problem

<span class="girk">思路一：正常思路，找到出现频率为1次的项</span>


```python
#方法一 循环
k = int(input())
num_list = input().split()
num_times = {}
for i in num_list:
    if i not in num_times:
        num_times[i] = 0
    num_times[i] +=  1

for i in num_times.keys():
    if num_times[i] == 1:
        print(i)
```

    5
    1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
    {'1': 5, '2': 5, '3': 5, '6': 5, '5': 5, '4': 5, '8': 1}
    8



```python
#方法二 fromkeys() 
k = int(input())
num_list = input().split()
num_times = dict.fromkeys(set(num_list),0)
for i in num_list:
    if i in num_times:
        num_times[i] +=  1
print(num_times)

for i in num_times.keys():
    if num_times[i] == 1:
        print(i)
```


```python
#方法三 collections.Counter
from collections import Counter
k = int(input())
num_list = input().split()
num_times = Counter(num_list)
print(num_times.most_common()[-1][0])
```

    5
    1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
    8



```python

l = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6]
d = dict.fromkeys(set(l),0)
print(d)
for i in l:
    if i in d:
        d[i] += 1
print(d)

from collections import Counter
c = Counter(d)
print(c)
m = c.most_common()
print(m[-1])
print(m[-1][0])


l = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6]
s = set(l)
print(s)
n = int((len(l)-1)/5)
print(n)
c = (sum(s)*n - sum(l))/(n-1)
print(int(c))
```

    {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    {1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1}
    Counter({1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1})
    (6, 1)
    6
    {1, 2, 3, 4, 5, 6}
    3
    6


<span class="girk">思路二：数学思路</span>

L = \[1,2,3,4,1,2,3,4,1,2,3,4,5\]    S = (1,2,3,4,5)

C 是L中只出现一次的5   K 是 \[1,2,3,4\]在L中出现的次数 

L = S \* K - (K-1) \* C 

C = (S * K - L)/(K-1)


```python
k = int(input())
num_list = list(map(int,input().split()))
s = set(num_list)
Captin = (sum(s)*k - sum(num_list))/(k-1)
print(int(Captin))
```

    5
    1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
    8


<span class="girk">思路三：集合差</span>

创建一个包括所有元素的集合，再创建一个包括出现频率超过一次的集合，两个集合求差

A 与 B 的差集是所有属于 A 且不属于 B 的元素构成的集合


```python
k = int(input())
num_list = list(map(int,input().split()))
s1 = set()
s2 = set()
for i in num_list:
    if i not in s1:
        s1.add(i)
    else:
        s2.add(i)
print((s1-s2).pop())
```

    5
    1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
    8


<span class="girk">思路四：集合对称差 完全想不到</span> 

将列表进行排序后，交错分成2个列表，一个奇数列表，一个偶数列表，将这两个列表变成集合后，求对称差

两个集合的对称差是只属于其中一个集合，而不属于另一个集合的元素组成的集合。


```python
k = int(input())
rooms = input().split()
rooms.sort()
capt_room = (set(rooms[0::2]) ^ set(rooms[1::2]))
print(capt_room.pop())
```

    5
    1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
    8


# Check Subset
https://www.hackerrank.com/challenges/py-check-subset/problem

s.issubset(t)  
 s <= t  # 测试是否 s 中的每一个元素都在 t 中 

s.issuperset(t)  
 s >= t  # 测试是否 t 中的每一个元素都在 s 中 


```python
# 正常思路求A和B的交集数量是否是还是A的数量

T = int(input())
for i in range(T):
    A_len = int(input())
    A = set(input().split())
    B_len = int(input())
    B = set(input().split())
    print(len(A&B)==A_len)
```

    1
    5
    1 2 3 5 6
    9
    9 8 5 6 3 2 1 4 7
    True



```python
# s.issubset(t)

T = int(input())
for i in range(T):
    A_len = int(input())
    A = set(input().split())
    B_len = int(input())
    B = set(input().split())
    print(A<=B)
```

    1
    5
    1 2 3 5 6
    9
    9 8 5 6 3 2 1 4 7
    True


# Check Strict Superset
https://www.hackerrank.com/challenges/py-check-strict-superset/problem


```python
# 正常思路

A = set(input().split())
N = int(input())
result = 0
for i in range(N):
    B = set(input().split())
    if A>B:
        result += 1
    else:
        result -= 1
if result=N:
    print('True')
else:
    print('False')

```

    True
    True
    True
    True
    False
    False



```python
# 用all() 函数

A = set(input().split())
print(all([A>set(input().split()) for i in range(int(input()))]))
```

    1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
    2
    1 2 3 4 5
    100 11 12
    False


<h2>all() 函数</h2>

all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False。

<span class="mark">注意：</span>空元组、空列表返回值为True，这里要特别注意。

all函数等价于下列代码段：


```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```


```python
print(all(['a', 'b', 'c', 'd']) ) # 列表list，元素都不为空或0
print(all(['a', 'b', '', 'd']) )  # 列表list，存在一个为空的元素
print(all([0, 1,2, 3]) )  # 列表list，存在一个为0的元素
print(all([]))  # 空列表
print(all(())) # 空元组
```

    True
    False
    False
    True
    True

