f = open(r"C:\Users\Admin\Desktop\Pracrice_6\File_Handling\demofile.txt", "r")
content = f.read()
print(content)
f.close()

f = open(r"C:\Users\Admin\Desktop\Pracrice_6\File_Handling\demofile.txt", "r")
print(f.readline())
f.close()

with open(r"C:\Users\Admin\Desktop\Pracrice_6\File_Handling\demofile.txt", "r") as f:
  print(f.read(5))

