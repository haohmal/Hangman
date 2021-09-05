numbers = input().split()
answers = input().split()
left = set()
left.update(numbers)
result = True
for answer in answers:
    if answer not in numbers:
        result = False
    elif answer in left:
        left.discard(answer)

if len(left) > 0:
    result = False
print(result)
