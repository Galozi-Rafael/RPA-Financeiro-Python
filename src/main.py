from apps.MoneyManagerEx.money_manager_app import MoneyManagerApp
from desktop_automation.controls.save_dialog import SaveDialog
from desktop_automation.controls.setup import SetupWizard
from desktop_automation.controls.currency_dialog import CurrencyDialog

def main():
    app_path = r"C:\Program Files\Money Manager EX\bin\mmex.exe"

    money_manager_app = MoneyManagerApp(app_path)

    money_manager_app.start_money_manager()

    #money_manager_app.map_interface()

    #money_manager_app.click_new_file()

    money_manager_app.create_database("Teste_MMEX.mmex")

    setup_wizard = SetupWizard(money_manager_app.window)

    setup_wizard.complete_setup("Teste")

    currency_dialog = CurrencyDialog(money_manager_app.window)

    currency_dialog.select_and_confirm("USD")

    setup_wizard.click_finish()

    setup_wizard.click_next()

    setup_wizard.click_next()

    setup_wizard.set_username("Teste")

    setup_wizard.click_finish()

    setup_wizard.click_ok()

    input("Pressione ENTER para finalizar...")

if __name__ == "__main__":
    main()