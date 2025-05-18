from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt6.QtWidgets import QTabWidget, QSpinBox, QListWidget, QApplication, QFileDialog
from PyQt6.QtGui import QClipboard
from PyQt6.QtCore import Qt
from Epoch import Generator
import csv

class Epoch(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Epoch")
        self.resize(600, 400)
        self.generator = Generator()
        
        self.tab_layout = QTabWidget()
        self.setCentralWidget(self.tab_layout)

        self.tab_layout.addTab(Generate_Single(self.generator), "Generate")
        self.tab_layout.addTab(Check_Single(self.generator), "Check")
        self.tab_layout.addTab(Generate_Multi(self.generator), "Generate Multi")


class Generate_Multi(QWidget):

    class button_layout(QWidget):
        def __init__(self, parent: object):
            super().__init__()
            self.layout = QHBoxLayout()
            self.setLayout(self.layout)
            self.parent = parent

            self.num_ids = QSpinBox()
            self.num_ids.setMinimum(1)
            self.num_ids.setMaximum(1000000)
            self.num_ids.setSingleStep(1)
            self.num_ids.textChanged.connect(self.update_warning)
            self.layout.addWidget(self.num_ids)

            self.button = QPushButton()
            self.button.setText("Generate")
            self.button.clicked.connect(self.generate_value)
            self.layout.addWidget(self.button)

        def update_warning(self):
            self.parent.warning_label.setText(f"""WARNING: Large batch requests may take some time. \nTime to process current request: {self.num_ids.value()/10} seconds.""")
        
        def generate_value(self):
            self.parent.list_view.clear()
            ID = self.parent.generator.generate(int(self.num_ids.value()))
            for i in ID:
                self.parent.list_view.addItem(str(i))

    def __init__(self, generator: Generator):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.generator = generator

        list_group = QWidget()
        list_layout = QHBoxLayout()
        list_group.setLayout(list_layout)
        
        self.list_view = QListWidget()
        self.list_view.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        list_layout.addWidget(self.list_view)

        button_stack = QVBoxLayout()

        self.copy_button = QPushButton()
        self.copy_button.setText("Copy")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        button_stack.addWidget(self.copy_button)

        self.export_button = QPushButton()
        self.export_button.setText("Export")
        self.export_button.clicked.connect(self.export)
        button_stack.addWidget(self.export_button)

        list_layout.addLayout(button_stack)

        self.warning_label = QLabel()
        self.warning_label.setText(f"""WARNING: Large batch requests may take some time. \nTime to process current request: 0.1 Seconds""")

        self.layout.addWidget(list_group)
        self.layout.addWidget(self.warning_label)
        self.layout.addWidget(self.button_layout(self))

    def export(self) -> None:
        file_name, _ = QFileDialog.getSaveFileName(self, "Export", "", "Comma Seperated Values (*.csv);;All Files (*)")
        if file_name:
            writer = csv.writer(open(file_name, 'w', newline=''))
            for i in range(self.list_view.count()):
                writer.writerow([self.list_view.item(i).text()])

    def copy_to_clipboard(self):
        numbers = []
        for i in range(self.list_view.count()):
            numbers.append(self.list_view.item(i).text())
        clipboard = QApplication.clipboard()
        clipboard.setText(','.join(numbers))


class Generate_Single(QWidget):

    def __init__(self, generator: Generator):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.generator = generator

        self.field = QWidget()
        layout = QHBoxLayout()
        self.field.setLayout(layout)

        self.id_field = QLabel()
        self.id_field.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        layout.addWidget(self.id_field)

        self.copy_button = QPushButton()
        self.copy_button.setText("Copy")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        layout.addWidget(self.copy_button)

        self.layout.addWidget(self.field)

        self.generate_button = QPushButton()
        self.generate_button.setText("Generate ID")
        self.generate_button.clicked.connect(self.generate_value)
        self.layout.addWidget(self.generate_button)

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.id_field.text(), QClipboard.Mode.Clipboard)

    def generate_value(self):
        self.id_field.setText(self.generator.generate()[0])


class Check_Single(QWidget):
    
    class Check_Field(QWidget):
        def __init__(self):
            super().__init__()
            self.layout = QHBoxLayout()
            self.setLayout(self.layout)
            
            self.paste_button = QPushButton()
            self.paste_button.setText("Paste")
            self.layout.addWidget(self.paste_button)

            self.field = QLineEdit()
            self.layout.addWidget(self.field)

            self.check_status = QLabel()
            self.layout.addWidget(self.check_status)

            self.paste_button.clicked.connect(self.paste_clipboard)
        
        def paste_clipboard(self):
            clipboard = QApplication.clipboard()
            self.field.setText(clipboard.text(QClipboard.Mode.Clipboard))

    def __init__(self, generator: Generator):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.generator = generator

        self.check_field = self.Check_Field()
        self.layout.addWidget(self.check_field)

        self.check_button = QPushButton()
        self.check_button.setText("Check")
        self.check_button.clicked.connect(self.checkButton)
        self.layout.addWidget(self.check_button)

    def checkButton(self):
        status = self.generator.check(self.check_field.field.text())
        self.check_field.check_status.setText("Passed \u2705" if status else u"Failed \u274c")
        
