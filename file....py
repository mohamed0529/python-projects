f=open("filehandling.txt") #default read mode
content=f.read()
print (content)

f=open("filehandling.txt","w")
content=f.write("alhamdhulillah we have married")

print(f.name)
print(f.mode)

f=open("filehandling.txt","a")
content=f.write("\nmasha allah!! what a couples!!\n")
print(content)


f=open("filehandling.txt","b")
print(f.read())