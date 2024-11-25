import re
i='abcd11gdf15hnnn678hh4'
txt = re.findall('\d',i)
print(txt)

num= "1299888833"
print(" ".join((list((set(i for i in num))))))

