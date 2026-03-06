from automation.gnucash_app import GnuCashApp

def main():
    app_path = r"C:\Program Files (x86)\gnucash\bin\gnucash.exe"

    gnucash_app = GnuCashApp(app_path)

    gnucash_app.start_app()

    input("Pressione ENTER para finalizar...")

if __name__ == "__main__":
    main()