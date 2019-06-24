from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class MainController(QObject):
    task_bar_message = pyqtSignal(str, str)

    def __init__(self, model):
        super().__init__()
        self._model = model

    @pyqtSlot(str)
    def file_name_changed(self, name):
        # update model
        self._model.file_name = name
