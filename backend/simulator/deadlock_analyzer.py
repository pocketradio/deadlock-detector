from simulator.resource_manager import ResourceManager
from simulator.tarjan import TarjanSCC, checkdeadlock
import kafka.producer as prod

rm = ResourceManager(10,2)

import time
while True:
    time.sleep(1)
    rm.tick()
    waitforgraph = rm.build_wfg()
    prod.produce('graph-updates', waitforgraph)
    
    
    tarjan = TarjanSCC(waitforgraph)
    sccs = tarjan.run()
    
    
    deadlocks = checkdeadlock(sccs,waitforgraph)
    if len(deadlocks) > 0:
        prod.produce('deadlock-alerts', f'DEADLOCK DETECTED : {deadlocks}')
        break