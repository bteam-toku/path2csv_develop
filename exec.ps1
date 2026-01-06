# バッチ実行関数
function Invoke-Batch {
    param (
        [string]$basepath,
        [string]$searchfolder
    )
    
    Set-Location -Path $PSScriptRoot
    Write-Host "$project Start"

    # 空きドライブレターを検索
    try {
        # PSDriveの作成
        $letter = $null
        # 絶対パスの取得
        $absPath = (Resolve-Path $basepath -ErrorAction Stop).Path
        # ネットワークドライブの場合の対応
        if ($abspath.StartsWith("\\") ) {
            # 空きドライブレターを検索
            foreach ($l in [char[]]([int][char]'Z'..[int][char]'D')) {
                if (-not (Get-PSDrive -Name $l -ErrorAction SilentlyContinue)) {
                    $letter = "$($l)"
                    break
                }
            }
            # ドライブが見つからなかった場合のエラーハンドリング
            if (-not $letter) {
                Write-Error "No available drive letters."
                return
            }
            # PSDriveの作成
            New-PSDrive -Name $letter -PSProvider FileSystem -Root $absPath -Persist | Out-Null
            $drivePath = "$letter`:"
            # ドライブがマウントされるまで待機
            $retryCount = 0
            while (-not (Test-Path "$drivePath") -and $retryCount -lt 5) {
                Start-Sleep -Seconds 1
                $retryCount++
            }
        }
        # ローカルパスの場合はそのまま使用
        else {
            $drivePath = $absPath
        }
        # Dockerコンテナの実行
        $current = (Get-Location).Path.Replace('\', '/')
        $drivePath = $drivePath.Replace('\', '/')
        docker run -it --rm `
            -v "${current}/output:/app/output" `
            -v "${current}/custom:/app/custom" `
            -v "${drivePath}:/app/data" `
            path2csv path2csv --basepath /app/data --searchfolder $searchfolder

    } 
    catch {
        Write-Error "Failed to create PSDrive: $_"
        return
    }
    finally {
        # ネットワークドライブの場合の解除
        if ($abspath.StartsWith("\\")) {
            Remove-PSDrive -Name $letter -Force
        }
    }

    Write-Host "$project Completed"
}
function Invoke-Setup-Batch {
    Set-Location -Path $PSScriptRoot
    Write-Host "path2csv_setup Start"
    # Dockerコンテナの実行
    $current = (Get-Location).Path.Replace('\', '/')
    docker run -it --rm `
        -v "${current}/custom:/app/custom" `
        path2csv path2csv_setup

    Write-Host "path2csv_setup Completed"
}

# # path2csv_setupの実行
# Invoke-Setup-Batch

# # path2csvの実行
# Invoke-Batch -basepath your-basepath -searchfolder your-searchfolder
