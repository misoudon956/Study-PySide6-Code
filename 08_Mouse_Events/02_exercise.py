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
    # ここから下にコードを書いてください







    # --- 課題2 --- #
    # マウスボタンが離されたら、ドラッグを終了します。
    # ここから下にコードを書いてください







    # --- 課題3 --- #
    # ドラッグ中(`_is_dragging`がTrue)にマウスが動いたら、
    # `movable_label` をマウスカーソルの位置に追従させて動かします。
    # ここから下にコードを書いてください







        # --- 構文のヒント ---
        # # マウスイベントハンドラのオーバーライド
        # def mousePressEvent(self, event):
        #     # マウスボタンが押されたときの処理
        #     pass
        #
        # def mouseReleaseEvent(self, event):
        #     # マウスボタンが離されたときの処理
        #     pass
        #
        # def mouseMoveEvent(self, event):
        #     # マウスが移動したときの処理
        #     pass
        #
        # # イベントオブジェクトから情報を取得
        # # event.position() # 現在のマウスカーソル位置 (QPointF)
        # # event.button()   # 押されたマウスボタン (Qt.MouseButton)
        # # widget.geometry().contains(point) # ウィジェットが点を含むか
        # # widget.move(QPoint) # ウィジェットを移動










        # --- 解答 --- #
        # (課題が完成したら、以下のコメントを外して動作確認)
        # def mousePressEvent(self, event):
        #     if self.movable_label.geometry().contains(event.position().toPoint()):
        #         self._is_dragging = True
        #         self.offset = event.position() - self.movable_label.pos()
        #
        # def mouseReleaseEvent(self, event):
        #     self._is_dragging = False
        #
        # def mouseMoveEvent(self, event):
        #     if self._is_dragging:
        #         new_pos = event.position() - self.offset
        #         self.movable_label.move(new_pos.toPoint())

        # --- 解答のヒント ---
        # def mousePressEvent(self, event):
        #     if self.movable_label.geometry().contains(event.position().toPoint()):
        #         self._is_dragging = True
        #         self.offset = event.position() - self.movable_label.pos()
        #
        # def mouseReleaseEvent(self, event):
        #     self._is_dragging = False
        #
        # def mouseMoveEvent(self, event):
        #     if self._is_dragging:
        #         new_pos = event.position() - self.offset
        #         self.movable_label.move(new_pos.toPoint())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())