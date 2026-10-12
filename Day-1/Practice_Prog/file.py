
l=["elevate","CSE"]
with open("Microsoft-Elevate.txt","r") as f:
    content = f.read()
    for i in l:
        if i in content:
            print(content.count(i))