class TarjanSCC:
    
    def __init__(self, graph):
        
        self.graph = graph
        self.index = 0
        self.indices = {}
        self.stack = []
        self.on_stack = set()
        self.lowlink = {}
        self.sccs= []
    
    def run(self):
        
        for node in self.graph:
            if node not in self.indices:
                self.dfs(node)
        
        return self.sccs

    def dfs(self, node):
        
        self.indices[node] = self.index
        self.lowlink[node] = self.index
        self.index += 1
        self.stack.append(node)
        self.on_stack.add(node)
        
        for neighbor in self.graph[node]:
            
            # check if child is visited:
            if neighbor not in self.indices:
                self.dfs(neighbor)
                self.lowlink[node] = min(self.lowlink[neighbor], self.lowlink[node])
                
            elif neighbor in self.on_stack:
                self.lowlink[node] = min(self.lowlink[neighbor], self.indices[node])
            
        if self.lowlink[node] == self.indices[node]:
            # scc root 
            
            scc = []
            while True:
                w = self.stack.pop()
                self.on_stack.remove(w)
                scc.append(w)
                if w == node:
                    break
            
            self.sccs.append(scc)



def checkdeadlock(scc, wfg):
    deadlocks = []
    
    for component in scc:
        if len(component) > 1:
            deadlocks.append(component)
        elif len(component) == 1 and component[0] in wfg[component[0]]: # self loop
            deadlocks.append(component)
    return deadlocks