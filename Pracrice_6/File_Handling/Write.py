with open(r"C:\Users\Admin\Desktop\Pracrice_6\File_Handling\demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open(r"C:\Users\Admin\Desktop\Pracrice_6\File_Handling\demofile.txt", "r") as f:
  print(f.read())