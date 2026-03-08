from apps.MoneyManagerEx.money_manager_app import MoneyManagerApp
from Services.new_db import NewDatabase

def main():
    app_path = r"C:\Program Files\Money Manager EX\bin\mmex.exe"

    money_manager_app = MoneyManagerApp(app_path)

    money_manager_app.start_money_manager()

    money_manager_app.create_database("MinhaNovaBase")

    new_database = NewDatabase(money_manager_app.window)

    new_database.complete_setup("Ze das couves", "USD", "Conta Principal")

    input("Pressione ENTER para finalizar...")

if __name__ == "__main__":
    main()