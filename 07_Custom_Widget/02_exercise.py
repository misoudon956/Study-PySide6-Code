# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt

class CustomFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 100)
        # 枠線の色を保持するインスタンス変数
        self._border_color = QColor("skyblue")

    def paintEvent(self, event):
        painter = QPainter(self)
        # 枠線の色をインスタンス変数から取得
        pen = QPen(self._border_color, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.setBrush(QColor("#353535"))
        painter.drawRect(self.rect().adjusted(1, 1, -1, -1))

    # --- 課題1 --- #
    # 枠線の色を変更するためのメソッド `setBorderColor` を作成しましょう。
    # このメソッドは、新しい色(QColor)を引数として受け取ります。
    def setBorderColor(self, color):
        self._border_color = color
        # update()を呼び出して、paintEventを再実行させ、画面を更新します。
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Widget Exercise")
        self.resize(400, 300)

        self.frame = CustomFrame()
        button_blue = QPushButton("Change to Blue")
        button_red = QPushButton("Change to Red")

        # --- 課題2 --- #
        # 各ボタンの `clicked` シグナルを接続し、クリックされたら
        # `self.frame` の `setBorderColor` メソッドを呼び出して
        # 枠線の色が変わるようにしましょう。
        # ヒント: ラムダ式を使うと、引数を渡すのが簡単になります。
        button_blue.clicked.connect(lambda: self.frame.setBorderColor(QColor("blue")))
        button_red.clicked.connect(lambda: self.frame.setBorderColor(QColor("red")))

        # --- レイアウト --- #
        layout = QVBoxLayout()
        layout.addWidget(self.frame)
        layout.addWidget(button_blue)
        layout.addWidget(button_red)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
