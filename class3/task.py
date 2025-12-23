# print numbers from 1 to 100
# for every 3rd number add foo
# for every 5th number add bar
# for every 10th number add buzz

for i in range(101):
    output = str(i)
    if i % 3 == 0:
        output += " foo"
    if i % 5 == 0:
        output += " bar"
    if i % 10 == 0:
        output += " buzz"
    print(output)