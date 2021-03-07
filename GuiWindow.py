from PySide6 import QtWidgets
from typing import List, Dict


class BCraineGuiWindow(QtWidgets.QWidget):
    def __init__(self, data_to_show):
        super().__init__()
        self.data = data_to_show
        self.list_control = None
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Sprint 4 Gui")
        display_list = QtWidgets.QListWidget(self)
        self.list_control = display_list
        self.put_data_in_list(self.data)
        display_list.resize(400, 350)
        self.setGeometry(100, 100, 400, 500)
        quit_button = QtWidgets.QPushButton("Quit Now", self)
        quit_button.clicked.connect(QtWidgets.QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(150, 400)
        self.show()

    def put_data_in_list(self, data: List[Dict]):
        for item in data:
            display_text = f"{item['state']}\t\t{item['occ_group']}\t\t{item['major_title']}" \
                           f"\t\t{item['total_employment']}\t\t{item['percentile_25_salary']}" \
                           f"\t\t{item['occupation_code']}"
            list_item = QtWidgets.QListWidgetItem(display_text, listview=self.list_control)
            list_item
