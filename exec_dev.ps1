.\env.ps1

# バッチ実行関数
function Invoke-Batch {
    param (
        [string]$basepath,
        [string]$searchfolder
    )
    
    Set-Location -Path $PSScriptRoot
    Write-Host "$project Start"
    py -m path2csv --basepath $basepath --searchfolder $searchfolder
    Write-Host "$project Completed"
}
function Invoke-Setup-Batch {
    Set-Location -Path $PSScriptRoot
    Write-Host "path2csv_setup Start"
    py -m path2csv_setup
    Write-Host "path2csv_setup Completed"
}

# # path2csv_setupの実行
# Invoke-Setup-Batch

# # path2csvの実行
# Invoke-Batch -basepath your-basepath -searchfolder your-searchfolder
