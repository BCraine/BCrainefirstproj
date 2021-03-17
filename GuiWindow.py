from PySide6 import QtWidgets
from typing import List, Dict


class BCraineGuiWindow(QtWidgets.QWidget):
    def __init__(self, data_to_show, more_data_to_show):
        super().__init__()
        self.data = data_to_show
        self.data1 = more_data_to_show
        self.list_control = None
        self.list_control1 = None
        self.setup_window_2()

    def setup_window(self):
        self.setWindowTitle("Sprint 4 Gui College Data")
        display_list = QtWidgets.QListWidget(self)
        self.list_control = display_list
        self.put_data_in_list_one(self.data)
        display_list.resize(700, 350)
        self.setGeometry(200, 200, 700, 600)
        quit_button = QtWidgets.QPushButton("Quit Now", self)
        quit_button.clicked.connect(QtWidgets.QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(400, 350)
        change_table_button = QtWidgets.QPushButton("Change Table/Update data", self)
        change_table_button.clicked.connect(self.setup_window_2)
        change_table_button.resize(change_table_button.sizeHint())
        change_table_button.move(30, 350)
        map_button = QtWidgets.QPushButton("Show Map", self)
        # map_button.clicked.connect(self.setup_window_2)
        map_button.resize(map_button.sizeHint())
        map_button.move(30, 425)
        color_buttona = QtWidgets.QPushButton("Show Color Coded Data (Ascending)", self)
        # map_button.clicked.connect(self.setup_window_2)
        color_buttona.resize(color_buttona.sizeHint())
        color_buttona.move(400, 425)
        color_buttonb = QtWidgets.QPushButton("Show Color Coded Data (Descending)", self)
        # map_button.clicked.connect(self.setup_window_2)
        color_buttonb.resize(color_buttonb.sizeHint())
        color_buttonb.move(30, 500)
        reload_data_button = QtWidgets.QPushButton("Reload Data", self)
        reload_data_button.resize(reload_data_button.sizeHint())
        reload_data_button.move(400, 500)

        self.show()

    def setup_window_2(self):
        self.setWindowTitle("Sprint 4 Gui Wage data")
        display_list1 = QtWidgets.QListWidget(self)
        self.list_control1 = display_list1
        self.put_data_in_list_two(self.data1)
        display_list1.resize(700, 350)
        self.setGeometry(200, 200, 700, 600)
        quit_button = QtWidgets.QPushButton("Quit Now", self)
        quit_button.clicked.connect(QtWidgets.QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(400, 350)
        change_table_button = QtWidgets.QPushButton("Change Table/Update data", self)
        change_table_button.clicked.connect(display_list1.clear)
        change_table_button.clicked.connect(self.setup_window)
        change_table_button.resize(change_table_button.sizeHint())
        change_table_button.move(30, 350)
        map_button = QtWidgets.QPushButton("Show Map", self)
        # map_button.clicked.connect(self.setup_window_2)
        map_button.resize(map_button.sizeHint())
        map_button.move(30, 425)
        color_buttonA = QtWidgets.QPushButton("Show Color Coded Data (Ascending)", self)

        color_buttonA.resize(color_buttonA.sizeHint())
        color_buttonA.move(400, 425)
        color_buttonb = QtWidgets.QPushButton("Show Color Coded Data (Descending)", self)

        color_buttonb.resize(color_buttonb.sizeHint())
        color_buttonb.move(30, 500)
        reload_data_button = QtWidgets.QPushButton("Reload Data", self)
        reload_data_button.clicked.connect(display_list1.clear)
        reload_data_button.resize(reload_data_button.sizeHint())
        reload_data_button.move(400, 500)
        self.show()

    def put_data_in_list_one(self, data: List[Dict]):
        for item in data:
            display_text = f"{item['name']}\t\t{item['city']}\t\t{item['cstate']}\t\t{item['size_2018']}" \
                           f"\t\t{item['size_2017']}\t\t{item['poverty_2017']}\t\t{item['repayment_2016']}" \
                           f"\t\t{item['repayment_cohort_2016']}"
            list_item = QtWidgets.QListWidgetItem(display_text, listview=self.list_control)
            list_item

    def put_data_in_list_two(self, data1: List[Dict]):

        for item in data1:
            display_text1 = f"\t\t{item['state']}\t\t{item['occ_group']}" \
                           f"\t\t{item['major_title']}" \
                           f"\t\t{item['total_employment']}\t\t{item['percentile_25_salary']}" \
                           f"\t\t{item['occupation_code']}"
            list_item1 = QtWidgets.QListWidgetItem(display_text1, listview=self.list_control1)
            list_item1
