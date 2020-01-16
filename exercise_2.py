# {'name':[xxx,xxxxx]}
# person = {}
#
# f = open('talk.txt','r')
#
# for each_line in f:
#     # 不是空行的情况下
#     if each_line != '\n':
#         role,line_spoken = each_line.split('：',1)
#         if role not in person:
#             person[role] = [each_line]
#         else:
#             person[role].append(each_line)
#
# f.close()
#
# for name in person:
#     with open(name+'.txt','w') as fw:
#         fw.writelines(person[name])
person = {}
f = open("talk.txt","r")
for line in f:
    if line != "\n":
        name,spoken = line.split("：",1)
        if name not in person:
            person[name] = [spoken]
        else:
            person[name].append(spoken)

f.close()
for name in person:
    fd = open(name + ".txt","w")
    fd.writelines(person[name])




