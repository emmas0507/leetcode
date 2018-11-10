def compare_versions(v1, v2):
    min_len = min(len(v1), len(v2))
    for i in range(min_len):
       if v1[i] != '.':
           if int(v1[i]) < int(v2[i]):
               return -1
           elif int(v1[i]) > int(v2[i]):
               return 1
           else:
               continue
    if len(v1) > min_len:
        return 1
    elif len(v2) > min_len:
        return -1
    else:
        return 0

v1 = '1.1.0'
v2 = '1.1'

print(compare_versions(v1, v2))
