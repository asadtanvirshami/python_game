#Playing with the list

items = ["Roger", "Syd"] #items list

items[0]="Clark" #adding the element into the listin specific index
items.append("Marks") #adding the element into the list
items.extend(["Lara"]) #adding the element into the list
items += (["unais"]) #adding the element into the list
items.remove("unais")
items[1:1] = ["NewName1", "NewName2"] #adding the element into the list with slice order

print(sorted(items, key=str.lower)) #sorting the list

 
