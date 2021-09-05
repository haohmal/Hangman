in_string = input()
left = in_string.find("old")
right = in_string.rfind("old")
if left > right:
    print(str(left))
else:
    print(str(right))