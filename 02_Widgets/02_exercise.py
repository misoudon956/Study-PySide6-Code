# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget Exercise")
        self.resize(400, 300)

        container = QWidget()
        self.setCentralWidget(container)

        # --- 課題1 --- #
        # "Hello World" と表示されているラベルのテキストを "My Widgets" に変更してみましょう。

        # --- 課題2 --- #
        # ここに新しいQPushButtonを追加してみましょう。
        # ボタンのテキストは "New Button" としてください。
        # (ヒント: self.new_button = QPushButton("テキスト", parent=container))
        
        # --- 課題3 --- #
        # 課題2で作成した新しいボタンを、(150, 80) の位置に表示してみましょう。
        # (ヒント: self.new_button.move(x, y))

        # ここから下にコードを書いてください







        # --- 構文のヒント ---
        # # ラベルの作成
        # self.label_name = QLabel("テキスト", parent=親ウィジェット)
        #
        # # ボタンの作成
        # self.button_name = QPushButton("テキスト", parent=親ウィジェット)
        #
        # # ウィジェットの位置を設定
        # self.widget_name.move(x, y)
        #
        # # ラベルのテキストを変更
        # self.label_name.setText("新しいテキスト")










        # --- 解答 --- #
        # (課題が完成したら、以下のコメントを外して動作確認)
        # self.label = QLabel("My Widgets", parent=container)
        # self.label.move(50, 50)
        #
        # self.button = QPushButton("Click Me!", parent=container)
        # self.button.move(50, 80)
        #
        # self.new_button = QPushButton("New Button", parent=container)
        # self.new_button.move(150, 80)

        # --- 解答のヒント ---
        # self.label = QLabel("My Widgets", parent=container)
        # self.label.move(50, 50)
        #
        # self.button = QPushButton("Click Me!", parent=container)
        # self.button.move(50, 80)
        #
        # self.new_button = QPushButton("New Button", parent=container)
        # self.new_button.move(150, 80)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())