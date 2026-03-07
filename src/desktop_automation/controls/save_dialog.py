from pywinauto import Desktop


class SaveDialog:

    def __init__(self):
        self.dialog = None

    def wait_dialog(self):

        print("Aguardando janela de salvar...")

        self.dialog = Desktop(backend="uia").window(class_name="wxWindowNR")

        self.dialog.wait("visible", timeout=20)

        print("Janela encontrada.")

    def set_file_name(self, file_name):

        print(f"Digitando nome do arquivo: {file_name}")

        file_name_edit = self.dialog.child_window(
            auto_id="1001",
            control_type="Edit"
        )

        #file_name_edit.wait("visible")

        file_name_edit.type_keys(file_name)

    def click_save(self):

        print("Clicando em salvar...")

        save_button = self.dialog.child_window(
            title="Salvar",
            control_type="Button"
        )

        save_button.click_input()

    def save(self, file_name):

        self.wait_dialog()

        self.set_file_name(file_name)

        self.click_save()

        print("Arquivo salvo com sucesso.")