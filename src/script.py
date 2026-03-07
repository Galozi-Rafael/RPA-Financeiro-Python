from pywinauto import Desktop

desktop = Desktop(backend="uia")

for w in desktop.windows():
    print("TITLE:", w.window_text())
    print("CLASS:", w.class_name())
    print("HANDLE:", w.handle)
    print("-----")