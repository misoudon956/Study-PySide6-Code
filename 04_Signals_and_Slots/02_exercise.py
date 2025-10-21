# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter Exercise")

        # --- 課題 --- #
        # ボタンをクリックするたびに、ラベルの数字が1ずつ増えるカウンターを作成しましょう。

        # 1. カウント数を保存するインスタンス変数を用意する
        # 2. ラベルとボタンを作成する
        # 3. ボタンのclickedシグナルを、新しく作る `count_up` メソッドに接続する

        # ここから下にコードを書いてください







        # --- レイアウト設定 --- #
        layout = QVBoxLayout()
        # ここにラベルとボタンを追加するコードを書く
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # 4. `count_up` メソッドを定義する
    def count_up(self):
        # ここに、クリックされたときの処理を書きます
        # - self.count を 1 増やす
        # - ラベルのテキストを更新して、新しいカウント数を表示する
        pass # ユーザーがコードを書くためのプレースホルダー


        # --- 構文のヒント ---
        # # インスタンス変数の初期化
        # self.variable_name = 初期値
        #
        # # ウィジェットの作成
        # self.widget_name = QLabel("テキスト") # または QPushButton("テキスト")
        #
        # # シグナルとスロットの接続
        # self.widget_name.signal_name.connect(self.slot_method_name)
        #
        # # ラベルのテキスト更新
        # self.label_name.setText("新しいテキスト")
        #
        # # メソッドの定義
        # def method_name(self):
        #     # 処理










        # --- 解答 --- #
        # (課題が完成したら、以下のコメントを外して動作確認)
        # self.count = 0
        # self.label = QLabel(f"Count: {self.count}")
        # self.button = QPushButton("Add +1")
        # self.button.clicked.connect(self.count_up)
        #
        # # レイアウト設定の解答
        # layout.addWidget(self.label)
        # layout.addWidget(self.button)
        #
        # # count_up メソッドの解答
        # # def count_up(self): # メソッド定義は既に存在するためコメントアウト
        # #     self.count += 1
        # #     self.label.setText(f"Count: {self.count}")

        # --- 解答のヒント ---
        # self.count = 0
        # self.label = QLabel(f"Count: {self.count}")
        # self.button = QPushButton("Add +1")
        # self.button.clicked.connect(self.count_up)
        #
        # # レイアウト設定のヒント
        # layout.addWidget(self.label)
        # layout.addWidget(self.button)
        #
        # # count_up メソッドのヒント
        # # def count_up(self): # メソッド定義は既に存在するためコメントアウト
        # #     self.count += 1
        # #     self.label.setText(f"Count: {self.count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())