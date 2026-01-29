from abc import ABC, abstractmethod
import pandas as pd
from pathlib import Path

class AbstractSearchPath(ABC):
    """パス検索抽象クラス
    """
    #
    # インストラクタ/デストラクタ
    #
    def __init__(self) -> None:
        pass

    def __del__(self) -> None:
        pass

    #
    # publicメソッド
    #
    @abstractmethod    
    def search_folder_list(self, search_path: Path, noexist_postfix: str = None)  -> pd.DataFrame:
        """指定されたフォルダ内のフォルダリストを作成

        Args:
            search_path (Path): 検索対象フォルダパス
            noexist_postfix (str): 検索対象フォルダがない場合に付与するPostFix（指定がなければ出力しない）
        
        Returns:
            pd.DataFrame: フォルダリスト(DataFrame形式)
        """
        pass

    @abstractmethod
    def search_file_list(self, search_path: Path = None, extensions: list[str] = None)  -> pd.DataFrame:
        """指定されたフォルダ内のファイルリストを作成

        Args:   
            search_path (Path): 検索対象フォルダパス
            extensions (list[str]): 拡張子フィルタリングリスト（指定しない場合は全てのファイルを対象とする）
        
        Returns:
            pd.DataFrame: ファイルリスト(DataFrame形式)
        """
        pass
