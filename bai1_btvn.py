# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 00:51:26 2023

@author: OS
"""
# phần 1 kiểu dữ liệu tuples 
"""t=(1,2, "skip a few", 99, 100)

print(type(t)) #in ra kiểu dữ liệu của t 
print(t)       #in ra t 
print(t[4])    # in ra giá trị của phần tử thứ 4  ở vị trí thứ 5 """

#kiểu dữ liệu list 
"""L=[1,2,3,4,5,6,100]

print(" the fisrt item is ", L[0])
print(" the second item is ", L[1])
print(" the last item is ", L[-1]) #giá trị tiếp theo của giá trị đầu sẽ đẩy về cuối list 
print(" the second to last item is ", L[-2])#giá trị tiếp theo của giá trị đầu sẽ đẩy về kế cuối list
 
    # bạn cũng có thể ghi đè trong kiểu list 
L[2]="huy"
L[3]=99
L[4]="erro" 

print(" the item is ", L[2])
print(" the item is ", L[3])
print(" the item is ", L[4])"""

# kiểu dữ liệu dict
"""d=dict()

d[5]="five"
d["ten"]= "huy"
d[2]="two"

print(d)
print(d["ten"])
    # trường hợp lỗi nếu ta cố tình ghi gọi sai 
my_dict={"a":"one", "b":"two"}
print(my_dict["c"])"""
#kiểu dữ liệu set 

s={2,1}
print(type(s))
#print(s[1]) # không thể in 1 phần tử trong set  

s.add(5)
print(s)
s.add(3)
s.add(3)
s.add(2)
print(s)