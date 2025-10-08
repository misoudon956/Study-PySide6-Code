# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Exercise")
        self.resize(800, 600)
        self.setStyleSheet("background-color: #333; color: white;")

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # --- サイドバー --- #
        sidebar = QWidget()
        sidebar.setStyleSheet("background-color: #444;")
        sidebar.setFixedWidth(200) # 少し幅を広げます
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(QPushButton("File"))
        sidebar_layout.addWidget(QPushButton("Block"))

        # --- 課題1 --- #
        # サイドバーに "Add Frame" というテキストの QPushButton を追加してみましょう。
        sidebar_layout.addWidget(QPushButton("Add Frame"))

        sidebar_layout.addStretch()
        sidebar.setLayout(sidebar_layout)

        # --- メインエリア --- #
        main_area = QWidget()
        main_area.setStyleSheet("background-color: #282828;")
        main_area_layout = QVBoxLayout()
        
        # --- 課題2 --- #
        # メインエリアに "Frame 1" というテキストの QLabel を追加してみましょう。
        main_area_layout.addWidget(QLabel("Frame 1"))

        main_area.setLayout(main_area_layout)

        # --- 組み立て --- #
        main_layout.addWidget(sidebar)
        main_layout.addWidget(main_area)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
