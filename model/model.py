from PyQt5.QtCore import QObject, pyqtSignal

class Model(QObject):
    file_name_changed = pyqtSignal(str, str)


    def __init__(self):
        super().__init__()


