

class importcsv:
    def __init__(self, window):
        self.window = window

    def click_import_csv(self, file_path, account_name="Conta Principal", preset="preset"):
        self.window.child_window(title_re="File").click_input()
        self.window.child_window(title_re="Import from").click_input()
        self.window.child_window(auto_id="6043").click_input()

        self.window.child_window(auto_id="10100").click_input()
        self.window.child_window(auto_id="1148", control_type="Edit").type_keys(file_path)
        self.window.child_window(auto_id="1", control_type="Button").click_input()

        self.window.child_window(auto_id="10103", control_type="ComboBox").select(account_name)
        self.window.child_window(auto_id="5102", control_type="ComboBox").select(preset)

        self.window.child_window(auto_id="10094", control_type="Button").click_input()

        self.window.child_window(auto_id="CommandButton_1", control_type="Button").click_input()

        self.window.child_window(auto_id="5101", control_type="Button").click_input()