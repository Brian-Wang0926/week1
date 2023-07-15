#Find out whose middle name is unique among all the names, and print it.
#You can assume every input is a Chinese name with 2 ~ 3 words.
#If there are only 2 words in a name, the middle name is defined as the second word.
# your code here

def func(*data):
    list=[]
    a=len(data)
    for i in range(a):
        list.append(data[i][1])
    not_repeat=[] 
    for j in list:
        a=''.join(list).count(j,0,len(list))
        if a == 1 and j not in not_repeat:
            not_repeat.append(j)

    for q in data:
        for k in not_repeat:
            if k in q:
                print(q)
    if len(not_repeat)==0:
        print("沒有")

func("彭大牆", "王明雅", "吳明")# print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

