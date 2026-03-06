from pywinauto import Application
import time

# GnuCashApp é uma classe que encapsula a automação do aplicativo GnuCash usando a biblioteca pywinauto.
class GnuCashApp:
    def __init__(self, app_path):
        self.app_path = app_path
        self.app = None
        self.window = None

    # O método start_app inicia o aplicativo GnuCash e aguarda até que a janela principal esteja visível.
    def start_app(self):
        self.app = Application(backend="uia").start(self.app_path)
        time.sleep(5)  # Wait for the application to start
        self.window = self.app.window(title_re=".*GnuCash.*")
        self.window.wait('visible')

        print("GnuCash foi iniciado com sucesso.")
