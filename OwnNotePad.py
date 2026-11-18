import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QGridLayout,
                             QTextEdit, QComboBox, QMenu, QAction, QFileDialog)

import themes

class NotePad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(150, 200, 700, 500)
        self.setWindowTitle("OwnNotePad")

        self.font_size = "0"
        self.file_directory = ""
        self.theme_change_toggle = False

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        self.central_widget.setLayout(vbox)
        self.writing_pad = QTextEdit()

        self.theme_button = QPushButton()

        self.edit_button = QPushButton("Text")

        self.file_button = QPushButton("File")

        self.file_menu = QMenu(self)
        self.file_menu.setFixedWidth(120)

        self.action_new = QAction("New")
        self.action_open = QAction("Open")
        self.action_save = QAction("Save")

        self.action_new.triggered.connect(self.action_new_triggered)
        self.action_open.triggered.connect(self.action_open_triggered)
        self.action_save.triggered.connect(self.action_save_triggered)
        
        self.file_menu.addAction(self.action_new)
        self.file_menu.addAction(self.action_open)
        self.file_menu.addAction(self.action_save)

        self.file_button.setMenu(self.file_menu)


        self.edit_button.clicked.connect(self.edit_click)
        self.theme_button.clicked.connect(self.theme_change)

        hbox.addWidget(self.file_button)
        hbox.addWidget(self.edit_button)
        hbox.addWidget(self.theme_button)

        hbox.setAlignment(Qt.AlignLeft)

        vbox.addLayout(hbox)
        vbox.addWidget(self.writing_pad)

        self.theme_change()

    def theme_change(self):
        if self.theme_change_toggle == False:
            self.setStyleSheet(themes.dark_mode)
            self.theme_change_toggle = True
            self.theme_button.setText("🌑")
        else:
            self.setStyleSheet(themes.light_mode)
            self.theme_change_toggle = False
            self.theme_button.setText("🌕")
    
    def edit_click(self):
        self.edit_window = on_edit(self, self.writing_pad, self.font_size)
        self.edit_window.show()

    def f_size_value_change(self, size):
        self.font_size = size

    def action_new_triggered(self):
        self.writing_pad.clear()

    def action_open_triggered(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            self.file_directory,
            "Text Files (*.txt);;All Files (*)"
        )

        if not filename:
            return

        with open(filename, "r") as file:
            self.writing_pad.clear()
            content = file.read()
            self.writing_pad.insertPlainText(content)

        self.file_directory = os.path.dirname(filename)
        print("#######################################################")
        print(f"Opened: {self.file_directory}")

    def action_save_triggered(self):
        text = self.writing_pad.toPlainText()
        print("#######################################################")
        print(text)
        filename = QFileDialog.getSaveFileName(self, "Save File", "", "Text files (*.txt)")
        try:
            with open(filename[0], "w", encoding="utf-8") as file:
                file.write(self.writing_pad.toPlainText())
                print("File created!", text)
        except Exception:
            print("error")

        self.file_directory = os.path.dirname(filename[0])
        print("#######################################################")
        print(f"Saved: {self.file_directory}")

class on_edit(QWidget):
    counter1 = 0
    f_list = ["Arial", "Calibri", "Segoe Print", "Ink Free", "Gabriola"]
    def __init__(self, notepad, writingpad, font_size):
        super().__init__()

        self.notepad = notepad
        self.writing_pad = writingpad
        self.font_size = font_size

        #buttons

        self.size_edit = QLineEdit()
        self.size_edit.setPlaceholderText("Enter size")

        #vbox

        self.local_vbox = QVBoxLayout()

        self.local_vbox.addWidget(self.size_edit)

        #vbox2

        self.bigvbox = QVBoxLayout()

        self.bigvbox.addLayout(self.local_vbox)

        #font list

        self.font_list = QComboBox()

        self.font_list.addItems(self.f_list)

        #add font list to vbox2

        self.bigvbox.addWidget(self.font_list)

        # cancel and done

        self.cahbox = QHBoxLayout()

        self.cancel = QPushButton("Cancel")
        self.done = QPushButton("Done")

        self.cahbox.addWidget(self.cancel)
        self.cahbox.addWidget(self.done)

        self.bigvbox.addLayout(self.cahbox)

        # cancel and done connect
        # self.cancel.clicked.connect()
        self.done.clicked.connect(self.done_click)
        self.cancel.clicked.connect(self.close)

        self.setLayout(self.bigvbox)

    def font_change(self):
        text = self.font_list.currentText()
        self.writing_pad.setStyleSheet(f"font-family: {text};"
                                       f"font-size: {self.font_size}px;")

        print("#######################################################")
        print(text)
        print("#######################################################")
        print(f"Old font list: {self.f_list}")

        index = self.f_list.index(text)
        self.f_list.pop(index)
        self.f_list.insert(0,text)

        print(f"New font list: {self.f_list}")
        print(f"{self.font_size}")

    def text_size_and_font_change(self, size):
        text = self.font_list.currentText()

        print("#######################################################")
        print(text)
        print("#######################################################")
        print(f"Old font list: {self.f_list}")

        index = self.f_list.index(text)
        self.f_list.pop(index)
        self.f_list.insert(0, text)

        print("#######################################################")
        print(f"New font list: {self.f_list}")

        self.font_size = size

        self.writing_pad.setStyleSheet(f"font-size: {self.font_size}px;"
                                       f"font-family: {text}")

        print("#######################################################")
        print(f"{self.font_size}")

        self.notepad.f_size_value_change(size)

    def done_click(self):
        self.size = self.size_edit.text()
        self.size = self.size.replace(" ", "")

        if self.size.isdigit():
            self.text_size_and_font_change(self.size)
            self.close()

        elif self.size == "":
            self.font_change()
            self.close()

        else:
            if self.counter1 == 0:
                self.error = QLabel("Invalid!")
                self.error.setStyleSheet("color: red")

                self.local_vbox.addWidget(self.error)

                self.counter1 += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NotePad()
    window.show()
    sys.exit(app.exec_())