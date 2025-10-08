# study.py - CodeSmith風レイアウト

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CodeSmith Layout Style")
        self.resize(800, 600)
        self.setStyleSheet("background-color: #333; color: white;")

        # --- 全体をまとめる水平レイアウト --- #
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0) # ウィンドウの端の余白をなくす
        main_layout.setSpacing(0) # ウィジェット間のスペースをなくす

        # --- 左側のサイドバー --- #
        sidebar = QWidget()
        sidebar.setStyleSheet("background-color: #444;")
        sidebar.setFixedWidth(150) # 幅を固定
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(QPushButton("File"))
        sidebar_layout.addWidget(QPushButton("Block"))
        sidebar_layout.addStretch() # ウィジェットを上に詰める
        sidebar.setLayout(sidebar_layout)

        # --- 右側のメインエリア --- #
        main_area = QWidget()
        main_area.setStyleSheet("background-color: #282828;")
        main_area_layout = QVBoxLayout()
        main_area_layout.addWidget(QLabel("Main Content Area"))
        main_area.setLayout(main_area_layout)

        # --- レイアウトの組み立て --- #
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
