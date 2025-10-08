# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter Exercise")

        # --- 課題 --- #
        # ボタンをクリックするたびに、ラベルの数字が1ずつ増えるカウンターを作成しましょう。

        # 1. カウント数を保存するインスタンス変数を用意する
        self.count = 0

        # 2. ラベルとボタンを作成する
        self.label = QLabel(f"Count: {self.count}") # f-stringで初期値を表示
        self.button = QPushButton("Add +1")

        # 3. ボタンのclickedシグナルを、新しく作る `count_up` メソッドに接続する
        self.button.clicked.connect(self.count_up)

        # --- レイアウト設定 --- #
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # 4. `count_up` メソッドを定義する
    def count_up(self):
        # ここに、クリックされたときの処理を書きます
        # - self.count を 1 増やす
        # - ラベルのテキストを更新して、新しいカウント数を表示する
        self.count += 1
        self.label.setText(f"Count: {self.count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
