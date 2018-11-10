def simplify_path(path):
    path_list = path.split('/')
    result = []
    for i in range(len(path_list)):
        p = path_list[i]
        if p == '..':
            if len(result) > 0:
                result = result[:(-1)]
        elif p.isalpha():
            result = result + [p]
        else:
            continue
    print(result)
    result = '/' + '/'.join(result)
    return result

path = "/a//b////c/d//././/.."
print(simplify_path(path))
