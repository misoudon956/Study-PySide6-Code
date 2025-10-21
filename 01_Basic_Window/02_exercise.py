# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- 課題1 --- #
        # ウィンドウのタイトルを "My First Qt App" に変更してみましょう。

        # --- 課題2 --- #
        # ウィンドウのサイズを幅800、高さ600に変更してみましょう。

        # ここから下にコードを書いてください







        # --- 構文のヒント ---
        # # ウィンドウのタイトルを設定
        # self.setWindowTitle("タイトル")
        #
        # # ウィンドウのサイズを設定
        # self.resize(幅, 高さ)










        # --- 解答 --- #
        # (課題が完成したら、以下のコメントを外して動作確認)
        # self.setWindowTitle("My First Qt App")
        # self.resize(800, 600)

        # --- 解答のヒント ---
        # self.setWindowTitle("My First Qt App")
        # self.resize(800, 600)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())