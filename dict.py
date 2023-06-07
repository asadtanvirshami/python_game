#playing with the dictionaries

agent = {"name":"Jack", "age":8, "designation":"employee"}
agent["designation"] = "roger"

# accessing the elements in this dict
# print(agent["designation"]) #accessing the specific element.
# print(agent.get("name","yusha"))#get the specific element.

# deleting the element form the dict
# print(agent.pop("name")) #remove the specific element.
# print(agent.popitem()) #poping the last element.

# mapping over here
# print(list(agent.keys()))#mapping the keys only.
# print(list(agent.values()))#mapping the values only.
# print(list(agent.items()))#mapping the whole dictionary.

# adding & deleting the element in the dict
agent["depart"] = "I.T" #adding the depart and its value in the dict. 
del agent["age"] #removing the age from the dict.

print(agent)