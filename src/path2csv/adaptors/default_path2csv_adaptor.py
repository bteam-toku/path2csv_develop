from path2csv.interfaces import AbstractPath2Csv
from path2csv.search_path import DefaultSearchPath
from pathlib import Path
import pandas as pd

class DefaultPath2CsvAdaptor(AbstractPath2Csv):
    """パス情報CSV出力デフォルトアダプタクラス    
    """
    #
    # コンストラクタ/デストラクタ
    #
    def __init__(self) -> None:
        super().__init__()

    def __del__(self) -> None:
        super().__del__()

    #
    # publicメソッド
    #
    def export(self, search_path: Path, folder_output: Path, file_output: Path) -> None:
        """指定されたパスの情報をCSVに出力する

        Args:
            search_path (Path): 検索対象パス
            folder_output (Path): 出力フォルダCSVファイルパス
            file_output (Path): 出力ファイルCSVファイルパス
        """
        #  パス検索クラスを生成
        search_engine = DefaultSearchPath()
        # フォルダを検索してCSVに出力
        folder_list = search_engine.search_folder_list(search_path)
        folder_list.to_csv(folder_output, index=False, encoding='utf-8-sig')
        # ファイルを検索してCSVに出力
        file_list = search_engine.search_file_list(search_path)
        file_list.to_csv(file_output, index=False, encoding='utf-8-sig')