# Import Modules
import Controller as ct

controller = ct.Controller()

controller.start()
while(controller.isRunning()):

    controller.displaySplash()
    controller.readMap()
    controller.readAlgorithm()
    controller.solve()
    controller.menu()