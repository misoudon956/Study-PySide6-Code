# study.py - ウィジェットの追加

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Widget App")
        self.resize(400, 300)

        # QMainWindowにウィジェットを配置するには、中央に表示するための
        # "セントラルウィジェット" としてQWidgetを一つ設定するのが一般的です。
        container = QWidget()
        self.setCentralWidget(container)

        # --- QLabel (テキストラベル) --- #
        # QLabelを作成します。引数で表示するテキストを渡せます。
        # 親ウィジェットとして container を指定します。
        self.label = QLabel("Hello World", parent=container)
        # .move(x, y) で親ウィジェット内の表示位置を決めます。
        self.label.move(50, 50)

        # --- QPushButton (ボタン) --- #
        # QPushButtonを作成します。
        self.button = QPushButton("Click Me!", parent=container)
        self.button.move(50, 80)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
