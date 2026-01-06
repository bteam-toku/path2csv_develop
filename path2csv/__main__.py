
from custom.path2csv import Path2Csv
import os
import argparse

def main():
    """メイン処理
    """
    # Path2Csvオブジェクト生成
    path2csv = Path2Csv()

    # argument取得
    parser = argparse.ArgumentParser()
    path2csv.define_arguments(parser) # 引数定義の拡張
    parser.add_argument('--outputpath', type=str, default='./output', help='出力フォルダ名(デフォルト: ./output)')
    parser.add_argument('--basepath', type=str, default=os.getcwd(), help='基準パス(デフォルト: カレントディレクトリ)')
    parser.add_argument('--searchfolder', type=str, default=None, help='検索フォルダ名(デフォルト: 自動取得)')
    args = parser.parse_args()
    # argument解析
    path2csv.parse_arguments(args) # 引数解析の拡張
    basepath = args.basepath
    searchfolder = args.searchfolder
    outputpath = args.outputpath

    # パラメータ設定
    path2csv.set_parameters(output_path=outputpath, base_path=basepath, search_folder=searchfolder)
    # リスト出力
    path2csv.export_folder_list()
    path2csv.export_file_list()

if __name__ == '__main__':
    main()