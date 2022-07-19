<#
    .SYNOPSIS
        Script to mount, parse, and store file paths in an ISO.
    .Description
        This script will mount an ISO, enumerate the file system, parse the string outputs, and store the output in a DB.
    .Example
        .\iso.ps1 -i "Ubuntu.iso" -os "u2004" -type "unix"
    .Example
        .\iso.ps1 -iso "Windows10.iso" -OSName "w10" -OSType "Windows"
    .Notes
        Created by Drew Bikowicz, 2022.
#>
param(

    [Alias("i")]
    [Parameter(Mandatory=$true)]
    [string]$iso,

    [Alias("os")]
    [Parameter(Mandatory=$true)]
    [string]$OSName,

    [Alias("type")]
    [Parameter(Mandatory=$false)]
    [string]$OSType

)

# Storyline: Mount an ISO file and list file paths. Filter for executable files and list. Format and export to JSON. 

# Mount the ISO via the file
$mountResult = Mount-DiskImage -PassThru "$iso"

# Get the drive/volume and set a variable for it's path
$drive = Get-DiskImage $mountResult.ImagePath | Get-Volume
$letter = $drive.DriveLetter + ":\"

# Define the array of file paths
$paths = @()

# If this is a Windows OS, format like Windows file paths
if ($OSType -imatch "windows") {
    # List contents and put it in an array
    foreach ($filePath in (Get-ChildItem $letter -Include "*.exe","*.dll" -Recurse -File | % { $_.FullName })) {
        # Replace the drive letter assigned to the mounted drive with C:\
        $windowsPath = (($filePath -replace ($drive.DriveLetter+":\\"), "C:\"))

        # Add filepath string to array of paths array under the OS name
        $paths += ($windowsPath)
    }
}
# If this is anything other than Windows, format like Unix file paths
else {
    # List contents and put it in an array
    foreach ($filePath in (Get-ChildItem $letter -Recurse -File | % { $_.FullName })) {
        # Replace Windows file path formatting with Unix file path formatting
        $unixPath = (($filePath -replace "\\","/") -replace ":","").Trim("/").TrimStart($drive.DriveLetter).ToLower()

        # Add filepath string to array of paths array under the OS name
        $paths += ($unixPath)
    }
}

$pathsFile = ".\file_paths_iso.txt"

$paths | Out-File -Append $pathsFile -Encoding ascii

# Dismount the ISO
Dismount-DiskImage -ImagePath "$iso" | Out-Null