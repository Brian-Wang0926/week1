#There is a number sequence: 
# 0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, ...
# 偶數區：0,3,6,9,12,15 (0,2,4,6,8,10)
# 奇數區：4,7,10,13 (1,3,5,7)
# 先判斷是在奇數還是偶數區，分別都是依序+3，判斷是第幾個
#Find out the nth term in this sequence.

def get_number(index):
    if index%2==0:   #判斷是偶數區
        num_even=0
        for i in range(0,index,2):
            num_even+=3
        print(num_even)
    else:            #判斷是奇數區
        num_odd=4
        for j in range(1,index,2):
            num_odd+=3
        print(num_odd)

get_number(1) # print 4 
print(" ")
get_number(5) # print 10 
print(" ")
get_number(10) # print 15 
print(" ")