# 01_Basic_Window まとめ

このセクションでは、PySide6で最も基本的なウィンドウを表示する方法を学びました。

## 重要ないくつかのクラス

- **`QApplication`**: 
  - すべてのPySide6アプリケーションに**必ず1つだけ**必要なオブジェクトです。
  - GUIの制御やイベント処理など、アプリケーション全体を管理します。

- **`QMainWindow`**: 
  - メインウィンドウを作成するためのクラスです。
  - メニューバー、ツールバー、ステータスバーなどを最初から持っている高機能なウィンドウです。
  - `QWidget`を基底クラスとして使うこともできますが、最初は`QMainWindow`に慣れるのがおすすめです。

## 基本的なコードの構造

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# 1. メインウィンドウのクラスを定義
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ここにウィンドウの設定（タイトル、サイズなど）を書く

# 2. アプリケーションを実行するための定型文
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplicationを作成
    window = MainWindow()         # MainWindowインスタンスを作成
    window.show()                 # ウィンドウを表示
    sys.exit(app.exec())          # イベントループを開始
```

## ポイント

- `app.exec()` は、アプリケーションの**イベントループ**を開始します。これにより、ウィンドウが表示され続け、ユーザーの操作（クリックやキー入力など）を待ち受ける状態になります。
- `sys.exit()` でラップすることで、プログラムが綺麗に終了することを保証します。
