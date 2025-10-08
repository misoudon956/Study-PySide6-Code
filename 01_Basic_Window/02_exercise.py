# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- 課題1 --- #
        # ウィンドウのタイトルを "My First Qt App" に変更してみましょう。
        self.setWindowTitle("My Qt Application")

        # --- 課題2 --- #
        # ウィンドウのサイズを幅800、高さ600に変更してみましょう。
        self.resize(400, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
