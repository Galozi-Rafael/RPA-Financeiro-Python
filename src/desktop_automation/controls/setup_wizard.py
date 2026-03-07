from desktop_automation.controls.currency_dialog import CurrencyDialog

class SetupWizard:

    def __init__(self, window):
        self.window = window
        self.currency_dialog = CurrencyDialog(window)

    def click_next(self):
        self.window.child_window(title_re="Next|Próximo").click_input()

    def open_currency_dialog(self):
        self.window.child_window(title_re="Choose Currency|Selecionar Moeda").click_input()

    def set_username(self, name):
        self.window.child_window(control_type="Edit").set_edit_text(name)

    def set_account_name(self, name):
        self.window.child_window(control_type="Edit").set_edit_text(name)

    def click_finish(self):
        self.window.child_window(title_re="Finish|Concluir").click_input()

    def click_ok(self):
        self.window.child_window(title_re="OK|Concluir").click_input()
        