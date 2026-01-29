from abc import ABC, abstractmethod
from pathlib import Path

class AbstractPath2Csv(ABC):
    """パス情報CSV出力抽象クラス    
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
    def export(self, search_path: Path, folder_output: Path, file_output: Path) -> None:
        """指定されたパスの情報をCSVに出力する

        Args:
            search_path (Path): 検索対象パス
            folder_output (Path): 出力フォルダCSVファイルパス
            file_output (Path): 出力ファイルCSVファイルパス
        """
        pass