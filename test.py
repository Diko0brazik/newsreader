di = {1:11, 2:22, 3:33}

#for i in di:
#    print(i, "  ")
li = [(i,di[i]) for i in di ]
print(li)