#This is a dfs function that requires user input.

def createDictionary():
    def dfs(graph, start, visited):
        visited.add(start)
        if start in graph:
            for neighbor in graph[start]:
                if neighbor not in graph:
                    dfs(graph, neighbor, visited)
                    
    graph = {}
    num_items = int(input("Enter the number of items: "))
    
    for _ in range(num_items):
        keys = input("Enter number of key: ")
        values = input ("Enter values splited by comma: ").split(",")
        
        values= [value.strip() for value in values]
        
        graph[keys] = values
        
    visited =set()
    dfs(graph, '0', visited)
    
    return graph, visited
    
myDict, visitedNodes = createDictionary()

print(myDict)
print(visitedNodes)
    
        