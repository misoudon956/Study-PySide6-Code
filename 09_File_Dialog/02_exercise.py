# exercise.py - 問題

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialog Exercise")

        self.open_label = QLabel("Opened file path...")
        self.save_label = QLabel("Saved file path...")
        open_button = QPushButton("Choose File to Open")
        save_button = QPushButton("Choose File to Save")

        # --- 課題 --- #
        # 1. `open_button` をクリックしたら `open_file` メソッドを呼び出すように接続してください。
        # 2. `save_button` をクリックしたら `save_file` メソッドを呼び出すように接続してください。
        open_button.clicked.connect(self.open_file)
        save_button.clicked.connect(self.save_file)

        # --- レイアウト --- #
        layout = QVBoxLayout()
        layout.addWidget(open_button)
        layout.addWidget(self.open_label)
        layout.addWidget(save_button)
        layout.addWidget(self.save_label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file(self):
        # 3. ファイルを開くダイアログを表示し、選択されたパスを `self.open_label` に表示してください。
        #    JSONファイルとAll Filesをフィルタに設定してみましょう。
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)"
        )
        if file_path:
            self.open_label.setText(file_path)

    def save_file(self):
        # 4. ファイルを保存するダイアログを表示し、選択されたパスを `self.save_label` に表示してください。
        #    PythonファイルとAll Filesをフィルタに設定してみましょう。
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Python File", "", "Python Files (*.py);;All Files (*)"
        )
        if file_path:
            self.save_label.setText(file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
