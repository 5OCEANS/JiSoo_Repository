def min_integer(x):
    result = ""
    for i in x:
        if i == "6":
            result += "5"
        else:
            result += i
    return result


def max_integer(x):
    result = ""
    for i in x:
        if i == "5":
            result += "6"
        else:
            result += i
    return result


A, B = input().split()

mn = int(min_integer(A)) + int(min_integer(B))
mm = int(max_integer(A)) + int(max_integer(B))

print(mn, mm)
