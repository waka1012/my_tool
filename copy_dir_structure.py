import os

inputDirPath = "C:\\Users\\***"
outputDirPath = "C:\\Users\\***"

#フォルダ構成を再帰的に取得
for dpath, dnames, fnames in os.walk(inputDirPath):
    for dname in dnames:
        #基準のフォルダからの相対パスを取得
        relPath = os.path.relpath(dpath, inputDirPath)
        #カレントディレクトリを出力ディレクトリに戻してから相対パスへ移動
        os.chdir(outputDirPath)
        os.chdir(relPath)
        os.mkdir(dname)
