# Import Modules
import Controller as ct

controller = ct.Controller()

controller.start()
while(controller.isRunning()):
    
    controller.readMap()
    controller.readAlgorithm()
    controller.solve()
    
    if True:
        controller.stop()