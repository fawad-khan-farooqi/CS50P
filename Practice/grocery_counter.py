#Input items until EOF.
# Output counts.
grocery = {}
while True:
    try:
        item = input("Enter Grocery Item: ")
        if not item:
            continue
        item = item.strip().title()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        break
    
for k, v in grocery.items():
    print(f"{k} = {v}")

    