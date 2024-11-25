s="inet 10.187.84.9 netmask 0xfffff800 broadcast 10.187.87.255"
import re
pattern = re.compile(("inet\s+\d+\.\d+\.\d+\.\d"))
match = re.findall(pattern,s)
print(match)

pattern = re.compile(("netmask\s+\d+\w*"))
match = re.findall(pattern,s)
print(match)

pattern = re.compile(("broadcast\s+\d+\.\d+\.\d+\.\d+"))
match = re.findall(pattern,s)
print(match)