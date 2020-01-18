import re
file1=open("readfile8.txt","r")
content1=file1.readlines()
file2=open("readfile9.txt","r")
content2=file2.readlines()
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
dict1={}
dict2={}
dict3={}
print("-----------------------nonmatching IP Addresses dictionary---------------------")

for i in content1:
    m1=re.search(r'(\d\d+.\d\d+.\d\d+.\d\d+.)',i)
    if m1:
        result1=m1.group(1)
        list1.append(result1)
#print(list1)
        
for j in content2:
    m2=re.search(r'(\d\d+.\d\d+.\d\d+.\d\d+.)',j)
    if m2:
        result2=m2.group(1)
        list2.append(result2)
#print(list2)

a1=(list(set(list1) - set(list2))) 
#print(a)

dict1={'ip':a1}
print(dict1)

print("-----------------------nonmatching Vlan Addresses dictionary---------------------")
for i in content1:
    m3=re.search(r'Vlan(\d+)',i)
    if m3:
        result3=m3.group(1)
        list3.append(result3)
#print(list3)
        
for j in content2:
    m4=re.search(r'Vlan(\d+)',j)
    if m4:
        result4=m4.group(1)
        list4.append(result4)
#print(list4)
        
a2=(list(set(list3) - set(list4)))
#print(a2)
dict2={'Vlan':a2}
print(dict2)

print("-----------------------nonmatching Hardware Addresses dictionary---------------------")
for i in content1:
    m5=re.search(r'(\d+.\d+.\d+.\d+)(\s+\S+\s)',i)
    if m5:
        result5=m5.group(2)
        list5.append(result5)
#print(list5)
        
for j in content2:
    m6=re.search(r'(\d+.\d+.\d+.\d+)(\s+\S+\s)',j)
    if m6:
        result6=m6.group(2)
        list6.append(result6)
#print(list6)
        
a3=(list(set(list5) - set(list6)))
#print(a3)
dict3={'Hardware Addresses':a3}
print(dict3)

