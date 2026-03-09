from apps.MoneyManagerEx.money_manager_app import MoneyManagerApp
from Services.new_db import NewDatabase
from desktop_automation.controls.import_csv import importcsv

def main():
    app_path = r"C:\Program Files\Money Manager EX\bin\mmex.exe"

    money_manager_app = MoneyManagerApp(app_path)

    money_manager_app.start_money_manager()

    money_manager_app.create_database("MinhaNovaBase")

    new_database = NewDatabase(money_manager_app.window)

    new_database.complete_setup("Ze das couves", "USD", "Conta Principal", "01/01/2024")

    import_csv = importcsv(money_manager_app.window)
    import_csv.click_import_csv(r'"D:\7-GitHub\RPA-Financeiro-Python\src\data\extrato_money_manager_ex_250_linhas.csv"')

    input("Pressione ENTER para finalizar...")

if __name__ == "__main__":
    main()