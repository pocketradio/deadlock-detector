import random

class ResourceManager:
    
    def __init__(self, N, M):
        
        self.processes = []
        self.resources = []
        
        for i in range(N):
            self.processes.append('P'+ str(i))
        for i in range(M):
            self.resources.append('R' + str(i))

        
        self.resource_owner = {r : None for r in self.resources}
        self.resource_requests = {p : [] for p in self.processes}
        
        self.resource_owner[self.resources[0]] = self.processes[0]

    
    def build_wfg(self):
        
        graph = {p : [] for p in self.processes}
        
        for process, resource in self.resource_requests.items():
            if len(resource) == 0:
                continue
            
            for r in resource:
                owner = self.resource_owner[r] # gives the process to which the resource is allocated.
                if owner is not None: # means there is a process that has resource r
                    graph[process].append(owner)
        
        return graph
    
    
    def tick(self):
        
        choice = random.randint(1,10)
        resource = random.choice(self.resources)
        process = random.choice(self.processes)
        
        if choice < 3: # release a process' resource
            for res,proc in self.resource_owner.items():
                if proc == process:
                    self.resource_owner[res] = None
                    
                    if res in self.resource_requests[process]:
                        self.resource_requests[process].remove(res)
                    print(f'\n\n released resource {res}')
                    break
                
        elif choice >= 3: # process requests a resource
            if self.resource_owner[resource] is None:
                
                if len(self.resource_requests[process]) == 0:
                    self.resource_owner[resource] = process   
            
            
            if resource not in self.resource_requests[process]:
                self.resource_requests[process].append(resource)
            print(f'\n\n process {process} requested resource {resource}')