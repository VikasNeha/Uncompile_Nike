import uncompyle2

with open("zipfile.py", "wb") as fileobj:
    uncompyle2.uncompyle_file("C:\\temp\\zipfile.pyo", fileobj)