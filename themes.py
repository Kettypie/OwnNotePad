light_mode = """
/* ===== GLOBAL ===== */
QWidget {
    background-color: #eff1f5;
    color: #4c4f69;
    border: none;
}

/* ===== MAIN WINDOW ===== */
QMainWindow {
    background-color: #e6e9ef;
}

/* ===== LABELS ===== */
QLabel {
    background-color: transparent;
    color: #4c4f69;
}

/* ===== PUSH BUTTONS ===== */
QPushButton {
    background-color: #dce0e8;
    color: #4c4f69;
    border: 1px solid #bcc0cc;
    border-radius: 5px;
    padding: 5px;
}

QPushButton:hover {
    background-color: #ccd0da;
    border: 1px solid #1e66f5;
}

QPushButton:pressed {
    background-color: #bcc0cc;
}

QPushButton:disabled {
    background-color: #e6e9ef;
    color: #9ca0b0;
    border: 1px solid #dce0e8;
}

/* ===== LINE EDIT ===== */
QLineEdit {
    background-color: #ffffff;
    color: #4c4f69;
    border: 1px solid #bcc0cc;
    border-radius: 5px;
    padding: 5px;
    selection-background-color: #7287fd;
    selection-color: #ffffff;
}

QLineEdit:focus {
    border: 1px solid #1e66f5;
}

/* ===== TEXT EDIT ===== */
QTextEdit {
    background-color: #ffffff;
    color: #4c4f69;
    border: 1px solid #bcc0cc;
    border-radius: 5px;
    padding: 5px;
    selection-background-color: #7287fd;
    selection-color: #ffffff;
}

QTextEdit:focus {
    border: 1px solid #1e66f5;
}

/* ===== COMBO BOX ===== */
QComboBox {
    background-color: #dce0e8;
    color: #4c4f69;
    border: 1px solid #bcc0cc;
    border-radius: 5px;
    padding: 5px;
}

QComboBox:hover {
    border: 1px solid #1e66f5;
}

QComboBox::drop-down {
    background-color: #dce0e8;
    border: none;
    width: 20px;
}

QComboBox QAbstractItemView {
    background-color: #ffffff;
    color: #4c4f69;
    selection-background-color: #ccd0da;
    selection-color: #1e66f5;
    border: 1px solid #bcc0cc;
    outline: none;
}

/* ===== MENU ===== */
QMenu {
    background-color: #eff1f5;
    color: #4c4f69;
    border: 1px solid #bcc0cc;
    padding: 4px;
}

QMenu::item {
    background-color: transparent;
    padding: 6px 25px 6px 10px;
}

QMenu::item:selected {
    background-color: #dce0e8;
    color: #1e66f5;
}

QMenu::item:disabled {
    color: #9ca0b0;
}

QMenu::separator {
    height: 1px;
    background-color: #bcc0cc;
    margin: 4px 6px;
}

/* ===== MENU BAR ===== */
QMenuBar {
    background-color: #e6e9ef;
    color: #4c4f69;
}

QMenuBar::item {
    background-color: transparent;
    padding: 5px 10px;
}

QMenuBar::item:selected {
    background-color: #dce0e8;
    color: #1e66f5;
}

QMenuBar::item:pressed {
    background-color: #ccd0da;
}

/* ===== FILE DIALOG ===== */
QFileDialog {
    background-color: #eff1f5;
    color: #4c4f69;
}

QFileDialog QLabel {
    color: #4c4f69;
}

QFileDialog QLineEdit {
    background-color: #ffffff;
    color: #4c4f69;
}

QFileDialog QPushButton {
    background-color: #dce0e8;
    color: #4c4f69;
}

/* ===== YOUR CUSTOM BUTTON SETTINGS ===== */
QPushButton {
    min-width: 50px;
    max-width: 50px;
    min-height: 20px;
    max-height: 20px;
    font-size: 12px;
    font-weight: bold;
}
"""

##############################################################

dark_mode = """
/* ===== GLOBAL ===== */
QWidget {
    background-color: #1e1e2e;
    color: #cdd6f4;
    border: none;
}

QMainWindow {
    background-color: #181825;
}

/* ===== LABELS ===== */
QLabel {
    background-color: transparent;
    color: #cdd6f4;
}

/* ===== PUSH BUTTONS ===== */
QPushButton {
    background-color: #313244;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 5px;
    padding: 5px;
}

QPushButton:hover {
    background-color: #45475a;
    border: 1px solid #89b4fa;
}

QPushButton:pressed {
    background-color: #585b70;
}

QPushButton:disabled {
    background-color: #252536;
    color: #6c7086;
    border: 1px solid #313244;
}

/* ===== LINE EDIT ===== */
QLineEdit {
    background-color: #181825;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 5px;
    padding: 5px;
    selection-background-color: #45475a;
    selection-color: #ffffff;
}

QLineEdit:focus {
    border: 1px solid #89b4fa;
}

/* ===== TEXT EDIT ===== */
QTextEdit {
    background-color: #181825;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 5px;
    padding: 5px;
    selection-background-color: #45475a;
    selection-color: #ffffff;
}

QTextEdit:focus {
    border: 1px solid #89b4fa;
}

/* ===== COMBO BOX ===== */
QComboBox {
    background-color: #313244;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 5px;
    padding: 5px;
}

QComboBox:hover {
    border: 1px solid #89b4fa;
}

QComboBox::drop-down {
    background-color: #313244;
    border: none;
    width: 20px;
}

QComboBox QAbstractItemView {
    background-color: #313244;
    color: #cdd6f4;
    selection-background-color: #45475a;
    selection-color: #ffffff;
    border: 1px solid #45475a;
    outline: none;
}

/* ===== MENU ===== */
QMenu {
    background-color: #1e1e2e;
    color: #cdd6f4;
    border: 1px solid #45475a;
    padding: 4px;
}

QMenu::item {
    background-color: transparent;
    padding: 6px 25px 6px 10px;
}

QMenu::item:selected {
    background-color: #45475a;
    color: #89b4fa;
}

QMenu::separator {
    height: 1px;
    background-color: #45475a;
    margin: 4px 6px;
}

/* ===== MENU BAR ===== */
QMenuBar {
    background-color: #181825;
    color: #cdd6f4;
}

QMenuBar::item {
    background-color: transparent;
    padding: 5px 10px;
}

QMenuBar::item:selected {
    background-color: #313244;
    color: #89b4fa;
}

/* ===== FILE DIALOG ===== */
QFileDialog {
    background-color: #1e1e2e;
    color: #cdd6f4;
}

/* ===== YOUR CUSTOM BUTTON SETTINGS ===== */
QPushButton {
    min-width: 50px;
    max-width: 50px;
    min-height: 20px;
    max-height: 20px;
    font-size: 12px;
    font-weight: bold;
}
"""