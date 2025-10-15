# ==========================================
# sync_class_to_student.ps1
# ==========================================
# First-run capable student script.
# Handles empty folders by cloning both repos.
# Then performs:
#   1. Commit & push student_repo
#   2. Pull class_repo
#   3. Copy new/modified files from class_repo → student_repo
# ------------------------------------------

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# --- Setup folder paths ---
$Dest = Get-Location           # student_repo (current folder)
$Root = Split-Path $Dest -Parent
$Source = Join-Path $Root "class_repo"
$ConfigFile = Join-Path $Dest ".sync_config.txt"

Write-Host "=========================================="
Write-Host "    PythonClass Student Sync Utility"
Write-Host "==========================================`n"

# --- STEP 0: Clone repos if missing ---

# Ask for student GitHub URL (store it)
if (-not (Test-Path $ConfigFile)) {
    $GitStudentURL = Read-Host "Enter your GitHub student repo URL (example: https://github.com/babson-org/python-yourname.git)"
    Set-Content -Path $ConfigFile -Value $GitStudentURL
} else {
    $GitStudentURL = Get-Content -Path $ConfigFile -Raw
}

# Define instructor (class) repo
$GitClassURL = "https://github.com/babson-org/classroom-python-python_repo.git"

# Clone student repo if missing
if (-not (Test-Path (Join-Path $Dest ".git"))) {
    Write-Host "[Setup] Cloning your student repository..."
    Set-Location $Root
    Remove-Item -Recurse -Force $Dest -ErrorAction SilentlyContinue | Out-Null
    git clone $GitStudentURL "student_repo"
    Write-Host "✅ Student repo cloned successfully.`n"
}

# Clone class repo if missing
if (-not (Test-Path (Join-Path $Source ".git"))) {
    Write-Host "[Setup] Cloning instructor class repository..."
    Set-Location $Root
    Remove-Item -Recurse -Force $Source -ErrorAction SilentlyContinue | Out-Null
    git clone $GitClassURL "class_repo"
    Write-Host "✅ Class repo cloned successfully.`n"
}

# --- STEP 1: Commit & push student repo ---
Set-Location (Join-Path $Root "student_repo")
Write-Host "[1/3] Committing and pushing student repo..."
git add -A
$pending = git status --porcelain
if ($pending) {
    git commit -m "Auto-sync commit from PowerShell script"
    git push origin main
    Write-Host "✅ Student repo committed and pushed to GitHub.`n"
} else {
    Write-Host "No local changes to commit.`n"
}

# --- STEP 2: Pull class repo ---
Set-Location (Join-Path $Root "class_repo")
Write-Host "[2/3] Pulling latest updates from class repo..."
git pull
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Class repo updated successfully.`n"
} else {
    Write-Host "⚠️  Warning: Could not update class repo.`n"
}

# --- STEP 3: Compare & Copy ---
Set-Location (Join-Path $Root "student_repo")
Write-Host "[3/3] Comparing and syncing files..."
Write-Host "   SOURCE: $Source"
Write-Host "   DEST:   $Dest"
Write-Host ""

$Exclude = @(".git", ".ipynb_checkpoints", "__pycache__", ".venv", "venv")
$CopyAll = $false
$NewFilesCopied = 0
$ModifiedOverwritten = 0
$SkippedFiles = 0

$sourceFiles = Get-ChildItem -Path $Source -Recurse -File -ErrorAction SilentlyContinue | Where-Object {
    $excludeMatch = $false
    foreach ($pattern in $Exclude) {
        if ($_.FullName -match [regex]::Escape($pattern)) { $excludeMatch = $true; break }
    }
    return -not $excludeMatch
}

Write-Host "Found $($sourceFiles.Count) source files to evaluate.`n"

foreach ($srcFile in $sourceFiles) {
    $relativePath = $srcFile.FullName.Substring($Source.Length + 1)
    $destFile = Join-Path $Dest $relativePath
    $destDir = Split-Path $destFile

    if (-not (Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }

    if (-not (Test-Path $destFile)) {
        Copy-Item $srcFile.FullName $destFile -Force
        Write-Host "Auto-copied new file: $relativePath"
        $NewFilesCopied++
        continue
    }

    $srcHash = (Get-FileHash $srcFile.FullName).Hash
    $destHash = (Get-FileHash $destFile).Hash

    if ($srcHash -ne $destHash) {
        Write-Host "Modified file: $relativePath"
        if (-not $CopyAll) {
            $choice = Read-Host "Overwrite this file? (Y/N/A=Yes to All)"
            if ($choice -match '^[Aa]$') { $CopyAll = $true }
        }

        if ($CopyAll -or $choice -match '^[Yy]$') {
            Copy-Item $srcFile.FullName $destFile -Force
            Write-Host "Overwrote $relativePath"
            $ModifiedOverwritten++
        } else {
            $SkippedFiles++
        }
    }
}

Write-Host "`n=========================================="
Write-Host "Sync complete."
Write-Host "----------------------------------"
Write-Host "New files copied:      $NewFilesCopied"
Write-Host "Files overwritten:     $ModifiedOverwritten"
Write-Host "Files skipped:         $SkippedFiles"
Write-Host "----------------------------------"
Write-Host "✅ Student repo committed & pushed. (Step 1)"
Write-Host "✅ Class repo updated.             (Step 2)"
Write-Host "✅ Files synced.                   (Step 3)"
Write-Host "=========================================="

# Return to student repo
Set-Location $Dest



