from pywinauto import Application
import time

class AppManager:

    def __init__(self, backend="uia"):
        self.backend = backend
        self.app = None
        

    def start_app(self, app_path):
        self.app = Application(backend=self.backend).start(app_path)

        time.sleep(2)  

        return self.app