# 05_Styling まとめ

このセクションでは、`setStyleSheet` を使ってアプリケーションの見た目をカスタマイズする方法を学びました。

## スタイルシート (Stylesheet)

PySide6のスタイルシートは、Web開発で使われるCSS（カスケーディング・スタイル・シート）のサブセットです。基本的な構文はCSSとほぼ同じです。

```css
セレクタ {
    プロパティ1: 値1;
    プロパティ2: 値2;
}
```

## セレクタ

スタイルをどのウィジェットに適用するかを指定します。

- **タイプセレクタ**: ウィジェットのクラス名を指定します。そのタイプのすべてのウィジェットに適用されます。
  ```css
  QPushButton { color: red; }
  ```

- **IDセレクタ**: 特定のウィジェットにのみ適用したい場合に使います。`setObjectName()`でウィジェットに名前を付け、`#名前`で指定します。
  ```python
  my_button.setObjectName("special_button")
  ```
  ```css
  #special_button { background-color: blue; }
  ```

## 疑似状態 (Pseudo-States)

ウィジェットの特定の状態（マウスが乗っている、クリックされているなど）に応じてスタイルを変更できます。セレクタに`:状態名`を付けます。

- **`:hover`**: マウスカーソルがウィジェットの上に乗っている状態。
- **`:pressed`**: ウィジェットがクリックされている（マウスボタンが押されている）状態。
- **`:disabled`**: ウィジェットが無効化されている状態。

```css
QPushButton:hover {
    background-color: lightblue;
}
```

## 主なプロパティ

- `color`: 文字色
- `background-color`: 背景色
- `font-size`: フォントサイズ (例: `16px`)
- `font-weight`: フォントの太さ (例: `bold`)
- `border`: 枠線 (例: `2px solid black`)
- `border-radius`: 角の丸み
- `padding`: 内側の余白
