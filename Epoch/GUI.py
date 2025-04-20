from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from Epoch import Generator

class Epoch(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Epoch")
        self.resize(600, 400)
        self.generator = Generator()

        self.value = QLabel()
        self.value.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.gen_button = QPushButton()
        self.gen_button.setText("Generate ID")
        self.gen_button.clicked.connect(self.generate_value)

        self.single_layout = QVBoxLayout()
        self.single_layout.addWidget(self.value)
        self.single_layout.addWidget(self.gen_button)
        self.single = QWidget()
        self.single.setLayout(self.single_layout)

        self.setCentralWidget(self.single)

    def generate_value(self):
        self.value.setText(self.generator.generate()[0])
# app = QApplication(sys.argv)

# window = QMainWindow()
# window.show()

# app.exec()