def fizzbizz(num):
     s=[]
     for i in range(1,num+1):
            if i%15==0:
                         s.append("fizzBizz")
            elif i%3==0:
                         s.append("fizz")
            elif i%5==0:
                         s.append("bizz")
            else:
                         s.append(i)
     return s
