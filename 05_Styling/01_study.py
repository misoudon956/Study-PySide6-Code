# study.py - スタイリング

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styling App")

        # --- スタイルシート (Stylesheet) --- #
        # CSSによく似た記法で、ウィジェットの見た目をカスタマイズできます。
        # セレクタ { プロパティ: 値; }
        style = """
            /* QWidget全体に適用 */
            QWidget {
                background-color: #f0f0f0; /* 背景色 */
            }

            /* QLabelに適用 */
            QLabel {
                color: navy; /* 文字色 */
                font-size: 16px; /* フォントサイズ */
            }

            /* QPushButtonに適用 */
            QPushButton {
                background-color: steelblue;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px; /* 角を丸くする */
            }

            /* QPushButtonが押された(pressed)状態のとき */
            QPushButton:pressed {
                background-color: crimson;
            }
        """
        self.setStyleSheet(style)

        # --- ウィジェットとレイアウト --- #
        label = QLabel("This is a styled label.")
        button = QPushButton("This is a styled button")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
