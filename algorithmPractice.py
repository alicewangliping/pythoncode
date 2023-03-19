import sys;
import array as arraylist;
import os
import time
import calendar

def rotateLeft(d, arr):
    # Write your code here
    for i in range(0,d):
        t=arr[0]
        arr= arr[1:]
        arr.append(t)
    return arr


if __name__ == '__main__':
        # fptr = open(os.environ['OUTPUT_PATH'], 'w')

        # first_multiple_input = input().rstrip().split()
        #
        # n = int(first_multiple_input[0])
        #
        d = int(input())
        arr=[1,2,3,4,5]
        #
        # arr = list(map(int, input("dfd").rstrip().split()))
        result = rotateLeft(d, arr)
        print(str,result)
        print("tup1[0]: ", result)
        print("tup2[1:5]: ", result[1:5])

        # learn how to use tuple
        tuple1=(50,30)
        print("tup1[1]: ",tuple1[0] )
        del tuple1

        # learn how to use list

        list1=["ddd",2,2,2,2]
        list2 = ["ttt", 2, 2, 2, 2]
        list3 = list1 + list2
        print('list3',list3[2:])

        # learn how to use complex number
        v=1-2j

        print('complex',v)

        # learn how to use string

        str = 'Hello World!'

        print(str) # 输出完整字符串
        print(str[0])  # 输出字符串中的第一个字符
        print(str[2:5])  # 输出字符串中第三个至第六个之间的字符串
        print(str[2:])  # 输出从第三个字符开始的字符串
        print(str * 2)

        # dictionary
        dict={}
        dict["name"] = "robert"
        dict["gender"] = "male"
        dict2={"name": "richard",'code' :16, 'gender': 'male' }

        print(dict['name'])
        print(dict2.keys(),dict2.values())




        # 幂函数

        a = 2
        b = 3
        c = a**b
        print('a mi b is ',c)
        #//= 取整等
        b=b//a
        print('a//b',b)
        c = a << 2;       # 240 = 1111 0000向左移动
        if(not (a<b)):
                print("test not")
        # is 与 == 区别： is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。

        # while 可以用ELSE

        print('a,b', a,b)

        while a<=b:
                a+=b
        else:
                a=b

        print(r'a\n', a)
#         r/R mean dont transfer不转义
        errHTML = '''
        <HTML><HEAD><TITLE>
        Friends CGI Demo</TITLE></HEAD>
        <BODY><H3>ERROR</H3>
        <B>%s</B><P>
        <FORM><INPUT TYPE=button VALUE=Back
        ONCLICK="window.history.back()"></FORM>
        </BODY></HTML>
        '''
        cursor= '''
        CREATE TABLE users (  
        login VARCHAR(8), 
        uid INTEGER,
        prid INTEGER)
        '''
        print(errHTML)

        # learn time fun time.time() is a timestamp means how long is from 1970
        ticks = time.time()
        localtime = time.localtime(time.time())# is a struct
        localtime = time.asctime(time.localtime(time.time()))#Is a normal time
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))#means formattime string
        print( "当前time struct:", localtime)

        # calendar need to be imported
        cal = calendar.month(2016, 1)


        # 可写函数说明
        def printme(str):
                "打印任何传入的字符串"
                print(str)

                return

        # 调用printme函数
        printme(str="My string")

        # 可写函数说明
        sum = lambda arg1, arg2: arg1 + arg2

        # 调用sum函数 learn how to use try exception
        print("相加后的值为 : ", sum(10, 20))

        try:
                fh = open("testfile", "w")
                fh.write("这是一个测试文件，用于测试异常!!")
        except IOError:
                print("Error: 没有找到文件或读取文件失败")
        else:
                print("内容写入文件成功")
                fh.close()


        # define decorator，define a function that parameter is a fun too, return is a function.
        def use_logging(func):
                def wrapper():
                        print("%s is running" % func.__name__)#__name__每个函数都可以取出相应的name
                        return func()
                return wrapper
        @use_logging #语法糖
        def foo():
                print("i am foo")
        foo()

        #赋值y=x
        y = [x for x in range(10)]
        #    y = [value for key, value in d.items()]


