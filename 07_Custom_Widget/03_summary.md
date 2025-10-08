# 07_Custom_Widget まとめ

このセクションでは、`QWidget`を継承して独自のウィジェットを作成する方法を学びました。これは、CodeSmithのフレームやブロックのように、アプリケーション独自の見た目や振る舞いを持つUI部品を作るための基本です。

## カスタムウィジェットの作り方

1. **`QWidget` を継承したクラスを作成する。**
   ```python
   from PySide6.QtWidgets import QWidget

   class MyCustomWidget(QWidget):
       def __init__(self, parent=None):
           super().__init__(parent)
           # ここで初期設定などを行う
   ```

2. **`paintEvent()` メソッドをオーバーライド（再定義）する。**
   - `paintEvent` は、そのウィジェットの外観を描画するためのメソッドです。
   - ウィンドウサイズが変わったり、他のウィンドウに隠れてから再表示されたり、`update()`が呼ばれたりしたときに、自動的に実行されます。
   - このメソッドの中で、`QPainter`を使って線、図形、テキストなどを描画します。

## `QPainter` による描画

`QPainter`は、ウィジェット上に描画を行うための強力なツールです。

- **`QPainter(self)`**: 描画対象のウィジェット(`self`)を指定して、`QPainter`オブジェクトを作成します。
- **`painter.setPen()`**: 描画する**線**の色、太さ、スタイル（実線、点線など）を設定します。`QPen`オブジェクトを使います。
- **`painter.setBrush()`**: 図形の**塗りつぶし**の色やパターンを設定します。`QColor`や`QBrush`オブジェクトを使います。
- **`painter.drawRect()`**: 長方形を描画します。
- **`painter.drawText()`**: テキストを描画します。
- **`painter.drawLine()`**: 線を描画します。

```python
from PySide6.QtGui import QPainter, QColor, QPen

def paintEvent(self, event):
    painter = QPainter(self)
    pen = QPen(QColor("red"), 3) # 赤い、3pxの太さのペン
    painter.setPen(pen)
    painter.setBrush(QColor("blue")) # 青い塗りつぶし
    painter.drawRect(10, 10, 100, 50) # (10,10)の位置に100x50の長方形を描画
```

## `update()` による再描画

ウィジェットの状態が変わったときに見た目を更新するには、`self.update()`メソッドを呼び出します。これにより、PySide6は適切なタイミングで`paintEvent`を再度実行し、画面を再描画してくれます。
