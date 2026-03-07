from pywinauto import Desktop

class CurrencyDialog:

    def __init__(self, window):
        self.window = window

    def wait(self):
        self.window.wait("visible", timeout=20)

    def select_and_confirm_currency(self, currency):

        self.wait()

        edits = self.window.descendants(control_type="Edit")

        search_box = edits[0]

        search_box.set_edit_text(currency)

        currency_list = self.window.child_window(control_type="List")

        currency_list.child_window(title_re=currency).click_input()

        self.window.child_window(title="Selecionar", control_type="Button").click_input()