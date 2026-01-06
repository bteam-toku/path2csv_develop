from path2csv.base_path2csv import BasePath2Csv
import argparse
import os
from datetime import datetime

class Path2Csv(BasePath2Csv):
    """Path2Csvの具象化クラス
    """
    #
    # コンストラクタ/デストラクタ
    #
    def __init__(self):
        """コンストラクタ
        """
        super().__init__()
    
    def __del__(self):
        """デストラクタ
        """
        super().__del__()
    
    #
    # publicメソッドのオーバーライド
    #
    def define_arguments(self, parser: argparse.ArgumentParser) -> None:
        """引数定義の拡張

        Args:
            parser (ArgumentParser): 引数パーサーオブジェクト
        """
        super().define_arguments(parser)
    
    def parse_arguments(self, args: argparse.Namespace) -> None:
        """引数解析の拡張

        Args:
            args (Namespace): 引数オブジェクト
        """
        super().parse_arguments(args)

    #
    # protectedメソッドのオーバーライド
    #
    def _get_base_path(self) -> str:
        """基準フォルダパスの取得

        Returns:
            str: 基準フォルダパス
        """
        return super()._get_base_path()
    
    def _get_search_folder(self) -> str:
        """検索フォルダ名の取得

        Returns:
            str: 検索フォルダ名
        """
        return super()._get_search_folder()
    
    def _get_output_filename(self, list_type: str) -> str:
        """出力ファイル名の取得

        Args:
            list_type (str): リスト種別(folder/file)

        Returns:
            str: 出力ファイル名
        """
        return super()._get_output_filename(list_type)
    
