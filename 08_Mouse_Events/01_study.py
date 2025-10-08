# study.py - マウスイベント

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Events")
        self.resize(400, 300)

        self.label = QLabel("Click or drag anywhere in this window.", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

    # --- マウスイベントのオーバーライド --- #

    # マウスボタンが押されたときに呼び出される
    def mousePressEvent(self, event):
        pos = event.position()
        self.label.setText(f"Mouse Pressed at: ({pos.x()}, {pos.y()})")

    # マウスボタンが離されたときに呼び出される
    def mouseReleaseEvent(self, event):
        pos = event.position()
        self.label.setText(f"Mouse Released at: ({pos.x()}, {pos.y()})")

    # マウスが動いたときに呼び出される
    # デフォルトではマウスボタンが押された状態でないと発生しない
    # 常時発生させるには self.setMouseTracking(True) を呼び出す
    def mouseMoveEvent(self, event):
        pos = event.position()
        self.label.setText(f"Mouse Moving at: ({pos.x()}, {pos.y()})")

    # マウスがダブルクリックされたときに呼び出される
    def mouseDoubleClickEvent(self, event):
        self.label.setText("Mouse Double Clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
