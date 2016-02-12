import os

inputDirPass = "C:\\Users\\***"
outputDirPass = "C:\\Users\\***"

#フォルダ構成を再帰的に取得
for dpath, dnames, fnames in os.walk(inputDirPass):
    for dname in dnames:
        #基準のフォルダからの相対パスを取得
        relPath = os.path.relpath(dpath, inputDirPass)
        #カレントディレクトリを出力ディレクトリに戻してから相対パスへ移動
        os.chdir(outputDirPass)
        os.chdir(relPath)
        os.mkdir(dname)
