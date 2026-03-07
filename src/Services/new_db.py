from desktop_automation.controls.setup_wizard import SetupWizard
from desktop_automation.controls.currency_dialog import CurrencyDialog

class NewDatabase:
    def __init__(self, window):
        self.window = window
        self.setup_wizard = SetupWizard(self.window)
        self.currency_dialog = CurrencyDialog(self.window)
        

    def complete_setup(self, username, currency="USD", accountname="Conta Principal"):
        self.setup_wizard.click_next()
        self.setup_wizard.set_username(username)
        self.setup_wizard.open_currency_dialog()
        self.currency_dialog.select_and_confirm_currency(currency)
        self.setup_wizard.click_finish()
        self.setup_wizard.click_next()
        self.setup_wizard.click_next()
        self.setup_wizard.set_account_name(accountname)
        self.setup_wizard.click_finish()
        self.setup_wizard.click_ok()

        