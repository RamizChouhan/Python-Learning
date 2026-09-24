import os

# ================= Create file =================
try:
    if not os.path.exists("data.txt"):
        file = open("data.txt", "x+")
        print("File Successfully created")
    else:
        file = open("data.txt", "w+")

except:
    print("Error!")

print(os.path.abspath("data.txt"))


# ================= READ BEFORE WRITE =================
print(file.tell())

data2 = file.read(2)
print("data 2:", data2)

print("Position after read:", file.tell())


# ================= WRITE =================
file.write("This is data file \n")
file.write("AI cannot replace you if you are always up skill your skills \n")

AiName = ["chatgpt\n", "claude\n", "cursor\n", "blackBox\n", "anti\n", "gemini"]
file.writelines(AiName)

print("Ending:", file.tell())


# ================= READ =================
file.seek(0)

data = file.read()
print(data)

# ================= READ signle lines =================
file.seek(0)
oneline = file.readline()
print("one line :",oneline)

# ================= READ lines as list =================

file.seek(0)
lst = file.readlines()
print("read as a list :",lst)

# ================= file object properties =================
print("file name :",file.name)
print("file mode :",file.mode)
print("file is closed :",file.closed)

# ================= CLOSE =================
file.close()

# ================= RENAME =================
#os.rename("data.txt", "detail.txt")

print("file size :",os.path.getsize("detail.txt"))
print("File renamed successfully")

