# study.py - レイアウト管理

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Layout App")
        self.resize(400, 300)

        # --- レイアウトの準備 --- #
        # QVBoxLayout: ウィジェットを垂直（縦）に並べる
        # QHBoxLayout: ウィジェットを水平（横）に並べる
        main_layout = QHBoxLayout() # 全体をまとめる水平レイアウト
        left_layout = QVBoxLayout() # 左側の垂直レイアウト

        # --- 左側のウィジェット --- #
        left_layout.addWidget(QLabel("Left Side"))
        left_layout.addWidget(QPushButton("Button 1"))
        left_layout.addWidget(QPushButton("Button 2"))

        # --- 右側のウィジェット --- #
        right_widget = QLabel("Right Side - This area can hold another widget")
        right_widget.setStyleSheet("background-color: lightgray;") # 見た目を分かりやすく

        # --- レイアウトの組み立て --- #
        # main_layout に左側のレイアウトと右側のウィジェットを追加
        main_layout.addLayout(left_layout)
        main_layout.addWidget(right_widget)

        # --- セントラルウィジェットの設定 --- #
        container = QWidget()
        container.setLayout(main_layout) # containerにレイアウトを適用
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
