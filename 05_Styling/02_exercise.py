# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styling Exercise")

        # --- 課題 --- #
        # 1. `info_label` の文字色を緑(green)に、フォントサイズを20pxにしてください。
        # 2. `action_button` の背景色をオレンジ(orange)に、文字サイズを14pxにしてください。
        # 3. `action_button` にマウスカーソルが乗った(`hover`)ときに、背景色を `darkorange` に変更してください。
        #
        # ヒント: 特定のウィジェットにスタイルを適用するには、`setObjectName`で名前を付け、
        #        セレクタに `#名前` を使います。

        info_label = QLabel("Information Label")
        info_label.setObjectName("info_label") # スタイル適用のため名前を設定

        action_button = QPushButton("Action Button")
        action_button.setObjectName("action_button") # スタイル適用のため名前を設定

        # --- ここにスタイルシートを記述 --- #
        style = """
            #info_label {
                color: green;
                font-size: 20px;
            }
            #action_button {
                background-color: orange;
                font-size: 14px;
                color: white;
                padding: 5px;
                border-radius: 5px;
            }
            #action_button:hover {
                background-color: darkorange;
            }
        """
        self.setStyleSheet(style)

        # --- レイアウト --- #
        layout = QVBoxLayout()
        layout.addWidget(info_label)
        layout.addWidget(action_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
