str = 'Ashish Yadav Abhishek Rajput Sunil Pundir'
print([i[::-1] for i in str.split(" ") if len(i)%2 ==0 ][::-1])
new=[]
for i in str.split():
    if len(i)%2 == 0 :
        new.append(i[::-1])
print(', '.join(new[::-1]))
