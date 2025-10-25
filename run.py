import os
import subprocess

print("""
ファイルを番号で実行するプログラム
例）directory number: 01 file number: 01
""" )

dir_num = input("directory number: ")
file_num = input("file number: ")

# Find the directory
target_dir = None
try:
    # List directories and filter for those that start with the given number
    dirs = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith(dir_num + '_')]
    if dirs:
        target_dir = sorted(dirs)[0]
except FileNotFoundError:
    print("エラー: カレントディレクトリの読み込みに失敗しました。")
    exit()

if not target_dir:
    print(f"エラー: ディレクトリ番号 '{dir_num}' が見つかりません。")
else:
    # Find the file
    target_file = None
    try:
        # List files in the target directory and filter for python or markdown files that start with the given number
        files = [f for f in os.listdir(target_dir) if f.startswith(file_num + '_') and (f.endswith('.py') or f.endswith('.md'))]
        if files:
            target_file = os.path.join(target_dir, sorted(files)[0])
    except FileNotFoundError:
        print(f"エラー: ディレクトリ '{target_dir}' が見つかりません。")
        target_file = None

    if not target_file:
        print(f"エラー: ディレクトリ '{target_dir}' 内にファイル番号 '{file_num}' の .py ファイルが見つかりません。")
    else:
        if target_file.endswith('.py'):
            print(f"実行中: {target_file}")
            try:
                # Use python from .venv
                venv_python = os.path.join('.venv', 'Scripts', 'python.exe')
                subprocess.run([venv_python, target_file], check=True)
            except subprocess.CalledProcessError as e:
                print(f"エラー: {target_file} の実行中にエラーが発生しました。")
                print(e)
            except FileNotFoundError:
                print(f"エラー: 仮想環境のPythonが見つかりません。'{venv_python}'が存在することを確認してください。")
        elif target_file.endswith('.md'):
            print(f"エディターで開いています: {target_file}")
            try:
                # Use 'start' command on Windows to open with default application
                subprocess.run(['start', target_file], shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"エラー: {target_file} の開中にエラーが発生しました。")
                print(e)
            except FileNotFoundError:
                print("エラー: ファイルを開くコマンドが見つかりません。")
        else:
            print(f"エラー: サポートされていないファイル形式です: {target_file}")