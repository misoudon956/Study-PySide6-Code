# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget Exercise")
        self.resize(400, 300)

        container = QWidget()
        self.setCentralWidget(container)

        # --- 課題1 --- #
        # "Hello World" と表示されているラベルのテキストを "My Widgets" に変更してみましょう。
        self.label = QLabel("Hello World", parent=container)
        self.label.move(50, 50)

        # 既存のボタン
        self.button = QPushButton("Click Me!", parent=container)
        self.button.move(50, 80)

        # --- 課題2 --- #
        # ここに新しいQPushButtonを追加してみましょう。
        # ボタンのテキストは "New Button" としてください。
        # (ヒント: self.new_button = QPushButton("テキスト", parent=container))
        

        # --- 課題3 --- #
        # 課題2で作成した新しいボタンを、(150, 80) の位置に表示してみましょう。
        # (ヒント: self.new_button.move(x, y))
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
