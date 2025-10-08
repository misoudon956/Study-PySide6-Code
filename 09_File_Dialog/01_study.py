# study.py - ファイルダイアログ

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialog")

        self.label = QLabel("Selected file path will appear here.")
        open_button = QPushButton("Open File")
        save_button = QPushButton("Save File")

        open_button.clicked.connect(self.open_file_dialog)
        save_button.clicked.connect(self.save_file_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(open_button)
        layout.addWidget(save_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file_dialog(self):
        # ファイルを開くダイアログを表示します。
        # QFileDialog.getOpenFileName() はタプル (ファイルパス, フィルタ) を返します。
        # ユーザーがキャンセルした場合は、ファイルパスは空文字列になります。
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File", # ダイアログのタイトル
            "", # 初期ディレクトリ
            "Text Files (*.txt);;All Files (*)" # ファイルフィルタ
        )

        if file_path:
            self.label.setText(f"Opened: {file_path}")
            print(f"Selected file to open: {file_path}")

    def save_file_dialog(self):
        # ファイルを保存するダイアログを表示します。
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "Text Files (*.txt);;All Files (*)"
        )

        if file_path:
            self.label.setText(f"Saved: {file_path}")
            print(f"Selected file to save: {file_path}")
            # ここで実際にファイルを書き込む処理などを行う


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
