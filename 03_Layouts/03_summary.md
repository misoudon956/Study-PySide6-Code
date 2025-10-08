# 03_Layouts まとめ

このセクションでは、ウィジェットを整然と並べるための「レイアウトマネージャー」について学びました。

## レイアウトとは？

レイアウトは、ウィンドウサイズが変更されたときなどに、ウィジェットのサイズや位置を自動的に調整してくれる仕組みです。`.move()` で位置を固定するよりも、はるかに柔軟なUIが作成できます。

## 主なレイアウトクラス

- **`QVBoxLayout`**: ウィジェットを**垂直（Vertical）**に、上から下に並べます。
- **`QHBoxLayout`**: ウィジェットを**水平（Horizontal）**に、左から右に並べます。
- **`QGridLayout`**: ウィジェットを格子状（グリッド）に配置します。（今回は扱いませんでしたが、電卓のようなUIで役立ちます）

## レイアウトの使い方

1. **レイアウトオブジェクトを作成する。**
   ```python
   layout = QVBoxLayout()
   ```

2. **`.addWidget()` でウィジェットをレイアウトに追加する。**
   追加した順に並びます。
   ```python
   button1 = QPushButton("Button 1")
   button2 = QPushButton("Button 2")
   layout.addWidget(button1)
   layout.addWidget(button2)
   ```

3. **`.addLayout()` でレイアウトを入れ子にする。**
   レイアウトの中に、さらに別のレイアウトを配置できます。これにより、複雑なUI構造も作成可能です。
   ```python
   main_layout = QHBoxLayout()
   left_layout = QVBoxLayout()
   main_layout.addLayout(left_layout) # レイアウトにレイアウトを追加
   ```

4. **最後に、土台となるウィジェットに `.setLayout()` でレイアウトを適用する。**
   ```python
   container = QWidget()
   container.setLayout(main_layout)
   self.setCentralWidget(container)
   ```
