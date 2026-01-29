from path2csv.interfaces import AbstractSearchPath
import os
from pathlib import Path
import pandas as pd

class BaseSearchPath(AbstractSearchPath):
    """パス検索基底クラス
    """
    #
    # コンストラクタ/デストラクタ
    #
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

    #
    # publicメソッド
    #
    def search_folder_list(self, search_path: Path, noexist_postfix: str = '_(NONE)'):
        """指定されたフォルダ内のフォルダリストを作成

        Args:
            search_path (Path): 検索対象フォルダパス
            noexist_postfix (str): 検索対象フォルダがない場合に付与するPostFix（指定がなければ出力しない）

        Returns:
            pd.DataFrame: フォルダリスト(DataFrame形式)
        """        
        #　初期化
        base_path = search_path.parent if search_path.parent is not None else Path.cwd()
        search_folder = search_path.name if search_path.name is not None else ''
        rows = []
        #　フォルダリストを取得
        if(search_path.is_dir()):
            # フォルダリストに先頭フォルダを追加
            rows.append({'Current':'', 'Sub':search_folder})
            # フォルダ内を走査してフォルダリストを取得
            for current_path, sub_dirs, _ in os.walk(search_path):
                # 基準パスからの相対パスを取得してPathオブジェクトに変換
                rel_path = Path(current_path).relative_to(base_path).as_posix()
                current_dir = '' if rel_path == "." else rel_path
                # サブフォルダをリストに追加
                for sub_dir in sub_dirs:
                    rows.append({'Current':current_dir, 'Sub':sub_dir})
        else:
            if noexist_postfix is not None:
                # フォルダが存在しない場合、先頭フォルダにタグを付与して出力
                rows.append({'Current':'', 'Sub':search_folder + noexist_postfix})
        # DataDrameに変換して返却
        return pd.DataFrame(rows, columns=['Current','Sub'])

    def search_file_list(self, search_path: Path = None, extensions: list[str] = None):
        """指定されたフォルダ内のファイルリストを作成

        Args:   
            search_path (Path): 検索対象フォルダパス
            extensions (list[str]): 拡張子フィルタリングリスト（指定しない場合は全てのファイルを対象とする）

        Returns:
            pd.DataFrame: ファイルリスト(DataFrame形式)
        """
        # 初期化
        base_path = search_path.parent if search_path.parent is not None else Path.cwd()
        extlist = [ext.lower() for ext in extensions if ext] if extensions is not None else []
        rows = []

        # フォルダ存在チェック
        if search_path.is_dir():
            # フォルダ内を走査してファイルリストを取得
            for file_path in search_path.rglob('*'):
                if file_path.is_file() and self._is_target_file(file_path.name, extlist):
                    # 基準パスからの相対パスを取得してPathオブジェクトに変換
                    rel_path = file_path.parent.relative_to(base_path).as_posix()
                    current_dir = '' if rel_path == "." else rel_path
                    rows.append({'Current':current_dir, 'file':file_path.name})
        # DataFrameに変換して返却
        return pd.DataFrame(rows, columns=['Current','file'])    

    #
    # protectedメソッド
    #
    def _is_target_file(self, filename: str, extensions: list[str]) -> bool:
        """指定されたファイルが対象の拡張子か判定する

        Args:
            filename (str): ファイル名
            extensions (list[str]): 拡張子リスト

        Returns:
            bool: 対象の拡張子の場合True、そうでない場合False
        """
        # 拡張子リストが空の場合はTrueを返す
        if not extensions:
            return True
        # 拡張子の判定結果を返す
        lower_filename = filename.lower()
        return any(lower_filename.endswith(ext) for ext in extensions)
