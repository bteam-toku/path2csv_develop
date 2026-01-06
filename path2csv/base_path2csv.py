import os
import pandas as pd
import argparse

class BasePath2Csv:
    """Path2Csvの基底クラス
    """
    # protectedメンバ変数
    _basepath: str = None
    _searchfolder: str = None
    _outputpath: str = None
    # protected定数
    _noexist_tag = '_(NONE)'

    #
    # コンストラクタ/デストラクタ
    #
    def __init__(self):
        pass

    def __del__(self):
        pass

    #
    # publicメソッド
    #
    def export_folder_list(self, output_path: str = None, base_path: str = None, search_folder: str = None, noexist_tag: str = None)  -> None:
        """指定されたフォルダ内のフォルダリストを出力
        Args:
            output_path (str): 出力CSVファイルパス
            base_path (str): 基準フォルダパス
            search_folder (str): 検索フォルダ名
            noexist_tag (str): フォルダが存在しない場合に付与するタグ
        """
        # 初期化
        base_path = base_path if base_path is not None else self._get_base_path()
        search_folder = search_folder if search_folder is not None else self._get_search_folder()
        noexist_tag = noexist_tag if noexist_tag is not None else self._noexist_tag
        target_path =  os.path.join(base_path, search_folder)

        rows = []

        # フォルダ存在チェック
        if(os.path.isdir(target_path)):
            # フォルダリストに先頭フォルダを追加
            rows.append({'Current':'', 'Sub':search_folder})
            # フォルダ内を走査してフォルダリストを取得
            for current_path, sub_dirs, _ in os.walk(target_path):
                # 区切り文字をOS依存から統一に変更
                rel_path = os.path.relpath(current_path, base_path)
                current_dir = '' if rel_path == "." else rel_path.replace(os.sep, '/')
                # サブフォルダをリストに追加
                for sub_dir in sub_dirs:
                    rows.append({'Current':current_dir, 'Sub':sub_dir})
        else:
            # フォルダが存在しない場合、先頭フォルダにタグを付与して出力
            rows.append({'Current':'', 'Sub':search_folder + noexist_tag})
        
        # DataFrame作成・CSV出力
        output_filename = os.path.abspath(os.path.join(output_path, 'folder_list.csv')) if output_path is not None else self._get_output_filename('folder')
        pd.DataFrame(rows, columns=['Current','Sub']).to_csv(output_filename, encoding='utf-8-sig', index=False)

    def export_file_list(self, output_path: str = None, base_path: str = None, search_folder: str = None, extensions: list[str] = None)  -> None:
        """指定されたフォルダ内のファイルリストを出力
        Args:   
            output_path (str): 出力CSVファイルパス
            base_path (str): 基準フォルダパス
            search_folder (str): 検索フォルダ名
            extensions (list[str]): 拡張子フィルタリングリスト. 指定しない場合は全てのファイルを対象とする. Defaults to None.
        """
        # 初期化
        base_path = base_path if base_path is not None else self._get_base_path()
        search_folder = search_folder if search_folder is not None else self._get_search_folder()
        target_path =  os.path.join(base_path, search_folder)
        rows = []
        if extensions is None:
            extlist = []
        else:
            extlist = [ext.lower() for ext in extensions if ext]

        # フォルダ存在チェック
        if os.path.isdir(target_path):
            # フォルダ内を走査してファイルリストを取得
            for current_path, _, files in os.walk(target_path):
                # 区切り文字をOS依存から統一に変更
                rel_path = os.path.relpath(current_path, base_path)
                current_dir = '' if rel_path == "." else rel_path.replace(os.sep, '/')
                # ファイルをリストに追加
                for file in files:
                    if self._is_target_file(file, extlist):
                        rows.append({'Current':current_dir, 'file':file})

        # DataFrame作成・CSV出力
        output_filename = os.path.abspath(os.path.join(output_path, 'file_list.csv')) if output_path is not None else self._get_output_filename('file')
        pd.DataFrame(rows, columns=['Current','file']).to_csv(output_filename, encoding='utf-8-sig', index=False)

    def define_arguments(self, parser: argparse.ArgumentParser) -> None:
        """引数定義の拡張

        Args:
            parser (ArgumentParser): 引数パーサーオブジェクト
        """
        pass
    
    def parse_arguments(self, args: argparse.Namespace) -> None:
        """引数解析の拡張

        Args:
            args (Namespace): 引数オブジェクト
        """
        pass

    def set_parameters(self, output_path: str = None, base_path: str = None, search_folder: str = None) -> None:
        """パラメータ設定

        Args:
            output_path (str): 出力フォルダパス
            base_path (str): 基準フォルダパス
            search_folder (str): 検索フォルダ名
        """
        self._basepath = base_path
        self._searchfolder = search_folder
        self._outputpath = output_path

    #
    # protectedメソッド
    #
    def _get_base_path(self) -> str:
        """基準パスを取得する

        Returns:
            str: 基準フォルダパス
        """
        return_path = self._basepath if self._basepath is not None else os.getcwd()
        return os.path.abspath(return_path)
    
    def _get_search_folder(self) -> str:
        """検索フォルダ名を取得する

        Returns:
            str: 検索フォルダ名
        """
        folder_name = self._searchfolder if self._searchfolder is not None else ''
        return folder_name


    def _get_output_filename(self, list_type: str) -> str:
        """出力ファイル名を取得する

        Args:
            list_type (str): リスト種別(folder/file)

        Returns:
            str: 出力ファイル名
        """
        # 出力フォルダ作成
        base_output_path = os.path.abspath(self._outputpath)
        if not os.path.exists(base_output_path):
            os.makedirs(base_output_path, exist_ok=True)

        match list_type:
            case 'folder':
                return os.path.join(base_output_path, 'folder_list.csv')
            case 'file':
                return os.path.join(base_output_path, 'file_list.csv')
            case _:
                raise ValueError(f"Unsupported list_type: {list_type}")
    
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
        # 拡張子が対象の場合はTrueを返す
        lower_filename = filename.lower()
        if any(lower_filename.endswith(ext) for ext in extensions):
            return True
        # 条件に該当しない場合はFalseを返す
        return False