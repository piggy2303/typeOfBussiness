# f= open("data.txt","w+")
# for i in range(100):
#      f.write("set key%d value%d\n" % (i+1,i+1))
# f.close()

f= open("data.txt","w+")
for i in range(437):
     c = raw_input()
     s = raw_input()
     f.write("{ key:%s, label: \"%s - %s\",value:\"%s\" },\n" % (c,c,s,s))
f.close()