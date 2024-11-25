a={'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}
# Output : Jaguar
b=max({i:a.get(i,0) for i in a.values()})
print({i:a.get(i,0) for i,j in a.items() if j == b})
out=max(a, key =lambda x:a[x])
print({out:a[out]})