# バッチ実行関数
function Invoke-Batch {
    param (
        [string]$search_path,
        [string]$subfolder_name = ""
    )
    
    $fullCurrentPath = Get-Location
    $fullCustomizePath = Join-Path $fullCurrentPath "customizes"

    # Dockerコンテナの実行
    docker run -it --rm `
        -v "$($fullCurrentPath):/data" `
        -v "$($fullCustomizePath):/app/src/path2csv/customizes" `
        ghcr.io/bteam-toku/path2csv:latest --search_path $search_path --subfolder_name $subfolder_name
}

# 一つ上の親ディレクトリをカレントフォルダリに設定（環境に合わせて変更してください）
Set-Location -Path (Join-Path $PSScriptRoot "..")

# # path2csvの実行
# Invoke-Batch -search_path your-basepath -subfolder_name your-subfolder