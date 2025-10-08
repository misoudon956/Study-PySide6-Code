# study.py - カスタムウィジェット

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt

# QWidgetを継承して、独自のウィジェットを作成します。
# これがCodeSmithにおけるFrameやBlockの基礎となります。
class CustomFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # ウィジェットの最小サイズを設定
        self.setMinimumSize(200, 100)

    # paintEventは、ウィジェットを描画する必要があるときに自動的に呼び出されます。
    def paintEvent(self, event):
        # QPainterを使ってウィジェット上に描画します
        painter = QPainter(self)

        # 枠線の設定 (色、太さ、スタイル)
        pen = QPen(QColor("skyblue"), 2, Qt.SolidLine)
        painter.setPen(pen)

        # 背景色の設定
        painter.setBrush(QColor("#353535"))

        # 長方形を描画 (x, y, width, height)
        # self.rect() はウィジェット自身の矩形領域を返します。
        painter.drawRect(self.rect().adjusted(1, 1, -1, -1)) # 枠線が内側になるよう調整


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Widget")
        self.resize(400, 300)

        # 作成したカスタムウィジェットをセントラルウィジェットとして設定
        my_frame = CustomFrame()
        self.setCentralWidget(my_frame)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
