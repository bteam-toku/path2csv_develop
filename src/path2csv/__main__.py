
from path2csv.factories import Factory
from path2csv import Config
from pathlib import Path
import argparse

def main():
    """メイン処理
    """
    # argument取得
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_path', type=str, default='', help='出力フォルダ名(デフォルトは設定ファイルのoutput_path)')
    parser.add_argument('--search_path', type=str, default='', help='検索フォルダ名(デフォルトは設定ファイルのsearch_path)')
    parser.add_argument('--subfolder_name', type=str, default='', help='サブフォルダ名(設定ファイルのsearch_path/subfolder_nameを検索対象とする)')
    args = parser.parse_args()
    # argument解析
    config = Config()
    search_path = Path(args.search_path) if args.search_path else Path(config.search_path())
    if args.subfolder_name:
        search_path = search_path / args.subfolder_name
    output_path = Path(args.output_path) if args.output_path else Path(config.output_path())

    # サービスオブジェクト生成
    path2csv = Factory.create(config.adaptor_type_name())
    # パラメータ設定
    path2csv.export(
        search_path=search_path, 
        folder_output=output_path / 'folder_list.csv', 
        file_output=output_path / 'file_list.csv')

if __name__ == '__main__':
    main()