from desktop_automation.core.app_manager import AppManager
from desktop_automation.controls.save_dialog import SaveDialog

# MoneyManagerApp é uma classe que encapsula a automação do aplicativo Money Manager Ex usando a biblioteca pywinauto.
class MoneyManagerApp:
    def __init__(self, app_path):
        self.app_path = app_path
        self.app_manager = AppManager()
        self.app = None
        self.window = None

    # O método start_app inicia o aplicativo GnuCash e aguarda até que a janela principal esteja visível.
    def start_money_manager(self):
        self.app = self.app_manager.start_app(self.app_path)
        self.window = self.app.window(title_re=".*Money Manager Ex.*")
        self.window.wait('visible')

        print("Money Manager Ex foi iniciado com sucesso.")

    def map_interface(self):
        print("Mapeando a interface do Money Manager Ex...")

        self.window.print_control_identifiers()

    def click_new_file(self):
        self.window.child_window(
            auto_id="5002",
            control_type="Button").click_input()
        
    def create_database(self, db_name):

        self.click_new_file()

        print("Criando nova base de dados...")

        save_dialog = SaveDialog()
        save_dialog.save(db_name)
