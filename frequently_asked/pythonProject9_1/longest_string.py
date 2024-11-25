def find_length(s):
    maxlen = 1
    if len(s) == 0:
        return 0
    result_string=''
    for i in range(len(s)):
        substring = s[i]
        for j in range(i+1,len(s)):
            if s[j] not in substring:
                substring = substring + s[j]
                maxlen = max(maxlen, len(substring))
                # print(substring, maxlen)
                if (len(substring) >= maxlen):
                    result_string = substring
            else:
                break
    if maxlen == 1:
        result_string = s[i]
    return result_string, maxlen


print(find_length("ABDEFGABEF"))





