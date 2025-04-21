from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt6.QtCore import Qt
from Epoch import Generator

class Epoch(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Epoch")
        self.resize(600, 400)
        self.generator = Generator()
        
        # self.setCentralWidget(Generate_Single(self.generator))
        self.setCentralWidget(Check_Single(self.generator))

class Generate_Single(QWidget):

    def __init__(self, generator: Generator):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.generator = generator

        self.id_field = QLabel()
        self.id_field.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.layout.addWidget(self.id_field)

        self.generate_button = QPushButton()
        self.generate_button.setText("Generate ID")
        self.generate_button.clicked.connect(self.generate_value)
        self.layout.addWidget(self.generate_button)

    def generate_value(self):
        self.id_field.setText(self.generator.generate()[0])

class Check_Single(QWidget):
    
    class Check_Field(QWidget):
        def __init__(self):
            super().__init__()
            self.layout = QHBoxLayout()
            self.setLayout(self.layout)

            self.check_field = QLineEdit()
            self.layout.addWidget(self.check_field)

            self.check_status = QLabel()
            self.layout.addWidget(self.check_status)


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
        status = self.generator.check(self.check_field.check_field.text())
        self.check_field.check_status.setText("Passed \u2705" if status else u"Failed \u274c")
        
