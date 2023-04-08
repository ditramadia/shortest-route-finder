# Import Modules
import Controller as ct

controller = ct.Controller()

controller.start()
while(controller.isRunning()):
    controller.displaySplash()
    controller.mode()
    controller.readMap()
    controller.readAlgorithm()
    controller.solve()
    if controller.wCoordinate():
        controller.plotter()
    controller.menu()
