# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Exercise")
        self.resize(400, 200)

        # --- 課題 --- #
        # 以下の仕様でレイアウトを組んでみましょう。
        # 1. 全体をまとめる垂直レイアウト(main_layout)を作成する。
        # 2. 上部に "Top Label" というテキストを持つQLabelを配置する。
        # 3. 下部に水平レイアウト(bottom_layout)を配置する。
        # 4. bottom_layoutの中に、"Left Button" と "Right Button" の2つのQPushButtonを配置する。

        # 1. 全体をまとめる垂直レイアウト
        main_layout = QVBoxLayout()

        # 2. 上部のラベル
        # (ここにQLabelを作成し、main_layoutに追加するコードを書く)
        top_label = QLabel("Top Label")
        main_layout.addWidget(top_label)

        # 3. 下部の水平レイアウト
        bottom_layout = QHBoxLayout()

        # 4. 水平レイアウト内のボタン
        # (ここに2つのQPushButtonを作成し、bottom_layoutに追加するコードを書く)
        left_button = QPushButton("Left Button")
        right_button = QPushButton("Right Button")
        bottom_layout.addWidget(left_button)
        bottom_layout.addWidget(right_button)

        # 3. main_layoutにbottom_layoutを追加
        main_layout.addLayout(bottom_layout)

        # --- 解答 --- #
        # (上記が完成したら、以下のコメントを外して動作確認)
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
