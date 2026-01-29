# バッチ実行関数
function Invoke-Batch {
    param (
        [string]$search_path,
        [string]$subfolder_name = ""
    )
    uv run execute --search_path $search_path --subfolder_name $subfolder_name
}

# 一つ上の親ディレクトリをカレントフォルダリに設定（環境に合わせて変更してください）
Set-Location -Path (Join-Path $PSScriptRoot "..")
# 仮想環境の有効化
.\scripts\env.ps1

# # path2csvの実行
# Invoke-Batch -search_path your-basepath -subfolder_name your-subfolder
