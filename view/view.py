from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot
from os import path
from view.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()
        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        ####################################################################
        #   connect widgets to controllers
        ####################################################################
        # open file buttons
        self._ui.pushButton.clicked.connect(self.open_file_name_dialog)

        ####################################################################
        #   listen for model event signals
        ####################################################################
        # file name is updated
        self._model.file_name_changed.connect(self.on_file_name_changed)

    def on_file_name_changed(self, name):
        # label color based on file_name
        # if the file name is empty them it means file is reseted
        name = path.basename(name)
        file_label_color = "green"
        self.on_task_bar_message(file_label_color, "Successfully loaded {} file".format(name))

    @pyqtSlot(str, str)
    def on_task_bar_message(self, color, message):
        self._ui.statusbar.show()
        self._ui.statusbar.showMessage(message)
        self._ui.statusbar.setStyleSheet('color: {}'.format(color))

    # Set one file
    def open_file_name_dialog(self):
        # open window to select file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                       "All Files (*)", options=options)

        if file_name:
            self._main_controller.file_name_changed(file_name)
