# 04_Signals_and_Slots まとめ

このセクションでは、PySide6の最も重要な概念である「シグナルとスロット」を学びました。

## シグナルとスロットとは？

- **シグナル (Signal)**: あるウィジェットで特定のイベント（例: ボタンがクリックされた、テキストが変更された）が発生したことを知らせる**通知**です。

- **スロット (Slot)**: シグナルを受け取って、特定の処理を実行する**メソッド（関数）**です。

この仕組みにより、「イベントの発生」と「処理の実行」を分離してコードを書くことができ、見通しが良くなります。

## 使い方

1. **スロットとなるメソッドを定義する。**
   ```python
   class MainWindow(QMainWindow):
       # ...
       def my_slot_method(self):
           print("Signal received!")
           # ここに実行したい処理を書く
   ```

2. **ウィジェットのシグナルと、定義したスロットを `.connect()` で接続する。**
   ```python
   class MainWindow(QMainWindow):
       def __init__(self):
           # ...
           my_button = QPushButton("Click")
           # "my_button" の "clicked" シグナルを "self.my_slot_method" に接続
           my_button.clicked.connect(self.my_slot_method)
   ```

## よく使われるシグナル

- `QPushButton`: `clicked()` (ボタンがクリックされたとき)
- `QLineEdit`: `textChanged(str)` (テキストが変更されたとき、新しいテキストが引数で渡される)
- `QCheckBox`: `toggled(bool)` (チェック状態が変わったとき、新しい状態が引数で渡される)

シグナルとスロットを使いこなすことが、インタラクティブなアプリケーションを作成する鍵となります。
