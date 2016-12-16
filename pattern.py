def array(k):
     s=[]
     k=k+1
     for i in range (1,k):
           for j in range(1,k):
                 s.append('{:2}'.format(i*j)),
           s.append("\n")
                 
     return s

