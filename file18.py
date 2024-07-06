f=open("f18ile.py","+a")
content=f.read()
print(content)


f=open("f18ile.py")
print(f.name)
print(f.mode)
print(f.closed)
f.close()
print(f.closed)

























f=open("f18ile.py","rb")
content=f.read(12)
print(content)
content=f.read()
print(content)