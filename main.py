display = {
  "0":("###","# #","# #","# #","###"),
  "1":("  #","  #","  #","  #","  #"),
  "2":("###","  #","###","#  ","###"),
  "3":("###","  #","###","  #","###"),
  "4":("# #","# #","###","  #","  #"),
  "5":("###","#  ","###","  #","###"),
  "6":("###","#  ","###","# #","###"),
  "7":("###","  #","  #","  #","  #"),
  "8":("###","# #","###","# #","###"),
  "9":("###","# #","###","  #","###")
}

num = input("Enter ")

string = ""
for row in range(len(display["0"])):
  line = []
  for item in num:
    line.append(display[item][row])      
  print(" ".join(line))  
  for item in line:
    string+=item

print(len(string.replace(" ","")))
