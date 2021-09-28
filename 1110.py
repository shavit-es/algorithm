i=0
num = input()
i_num=-1
while str(i_num)!=num:
    sum=0
    if i_num==-1:
        i_num = num
    if int(i_num)<10:
        i_num=str(i_num)+str(i_num)
    else:
        i_num=str(i_num)
        for char in i_num:
            sum = int(sum)
            sum = sum + int(char)
            sum = str(sum)
        i_num=i_num[-1]+sum[-1]
    i=i+1
    i_num=int(i_num)
print(i)
