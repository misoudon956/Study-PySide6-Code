# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Exercise")
        self.resize(500, 400)

        # このラベルをマウスで動かします
        self.movable_label = QLabel("Drag Me!", self)
        self.movable_label.resize(100, 30)
        self.movable_label.setStyleSheet("background-color: lightblue; border: 1px solid black;")
        self.movable_label.setAlignment(Qt.AlignCenter)

        # ドラッグ中かどうかを判定するフラグ
        self._is_dragging = False

    # --- 課題1 --- #
    # `movable_label` の上でマウスボタンが押されたら、ドラッグを開始する準備をします。
    def mousePressEvent(self, event):
        # `event.position()` で得た座標が `movable_label` の範囲内にあるかチェック
        if self.movable_label.geometry().contains(event.position().toPoint()):
            self._is_dragging = True
            # ラベルを動かす際に、クリックした位置とラベルの左上の差分を保持
            self.offset = event.position() - self.movable_label.pos()

    # --- 課題2 --- #
    # マウスボタンが離されたら、ドラッグを終了します。
    def mouseReleaseEvent(self, event):
        self._is_dragging = False

    # --- 課題3 --- #
    # ドラッグ中(`_is_dragging`がTrue)にマウスが動いたら、
    # `movable_label` をマウスカーソルの位置に追従させて動かします。
    def mouseMoveEvent(self, event):
        if self._is_dragging:
            # マウスの現在位置から、クリック時の差分を引くことで、
            # ラベルがスムーズに動くようになります。
            new_pos = event.position() - self.offset
            self.movable_label.move(new_pos.toPoint())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
