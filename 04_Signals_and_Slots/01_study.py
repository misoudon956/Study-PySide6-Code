# study.py - シグナルとスロット

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout

# 「スロット」とは、シグナルによって呼び出されるメソッド（関数）のことです。

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signals and Slots")

        self.label = QLabel("Press the button.")
        self.button = QPushButton("Press Me")

        # --- シグナルとスロットの接続 --- #
        # buttonの "clicked" シグナルを、"self.button_clicked" スロットに接続します。
        # これにより、ボタンがクリックされると self.button_clicked メソッドが自動的に呼び出されます。
        self.button.clicked.connect(self.button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # --- スロットの定義 --- #
    def button_clicked(self):
        # ボタンがクリックされたときに実行したい処理をここに書きます。
        print("Button was clicked!")
        self.label.setText("Button has been clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
