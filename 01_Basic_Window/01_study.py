# study.py - 基本的なウィンドウの表示

import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# QMainWindowを継承してメインウィンドウのクラスを作成します
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ウィンドウのタイトルを設定
        self.setWindowTitle("My Qt Application")

        # ウィンドウの初期サイズを設定 (幅, 高さ)
        self.resize(400, 300)


# このスクリプトが直接実行されたときにのみ以下のコードを実行
if __name__ == "__main__":
    # QApplicationインスタンスを作成
    # sys.argvはコマンドライン引数をアプリケーションに渡すために必要です
    app = QApplication(sys.argv)

    # MainWindowのインスタンスを作成
    window = MainWindow()
    
    # ウィンドウを表示
    window.show()

    # アプリケーションのイベントループを開始
    # ウィンドウが閉じられるまでプログラムはここで待機します
    sys.exit(app.exec())
