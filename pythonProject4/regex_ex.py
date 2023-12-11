import re

def match_text(s):
    pattern ='a,b{4,8}'
    if re.match(pattern,s):
        return True


print(match_text("aabbbbbc"))