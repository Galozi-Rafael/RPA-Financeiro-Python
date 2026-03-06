from desktop_automation.core.app_manager import AppManager

# GnuCashApp é uma classe que encapsula a automação do aplicativo GnuCash usando a biblioteca pywinauto.
class GnuCashApp:
    def __init__(self, app_path):
        self.app_path = app_path
        self.app_manager = AppManager()
        self.app = None
        self.window = None

    # O método start_app inicia o aplicativo GnuCash e aguarda até que a janela principal esteja visível.
    def start_gnucash(self):
        self.app = self.app_manager.start_app(self.app_path)
        self.window = self.app.window(title_re=".*GnuCash.*")
        self.window.wait('visible')

        print("GnuCash foi iniciado com sucesso.")

    def map_interface(self):
        print("Mapeando a interface do GnuCash...")

        self.window.print_control_identifiers()
