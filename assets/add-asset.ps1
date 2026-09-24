# ============================================
# SCRIPT D'AJOUT AUTOMATIQUE D'ASSETS
# Afrique Boussole Creatives
# ============================================

param(
    [Parameter(Mandatory=$true)]
    [string]$SourceFile,
    
    [Parameter(Mandatory=$true)]
    [ValidateSet("brand", "team", "visuals", "projects", "templates", "references")]
    [string]$Category,
    
    [string]$NewName,
    [string]$Description
)

# Couleurs pour output
$colors = @{
    Success = "Green"
    Warning = "Yellow"
    Error = "Red"
    Info = "Cyan"
}

function Write-ColorOutput($Message, $Color) {
    Write-Host $Message -ForegroundColor $colors[$Color]
}

# ============================================
# VALIDATION
# ============================================

Write-ColorOutput "`n🚀 AJOUT D'ASSET AUTOMATIQUE" "Info"
Write-ColorOutput "================================`n" "Info"

# Vérifier si le fichier source existe
if (-not (Test-Path $SourceFile)) {
    Write-ColorOutput "❌ Erreur : Fichier source introuvable : $SourceFile" "Error"
    exit 1
}

$file = Get-Item $SourceFile
$extension = $file.Extension.ToLower()

# Extensions autorisées
$allowedExtensions = @(".jpg", ".jpeg", ".png", ".svg", ".gif", ".webp", ".ico", ".pdf")

if ($extension -notin $allowedExtensions) {
    Write-ColorOutput "❌ Format non supporté : $extension" "Error"
    Write-ColorOutput "Formats autorisés : $($allowedExtensions -join ', ')" "Warning"
    exit 1
}

# ============================================
# DÉTERMINATION DU DOSSIER DESTINATION
# ============================================

$baseDir = Split-Path -Parent $PSScriptRoot
$assetsDir = "$baseDir\assets"

$destinationMap = @{
    "brand" = "$assetsDir\brand\logos"
    "team" = "$assetsDir\team"
    "visuals" = "$assetsDir\visuals"
    "projects" = "$assetsDir\projects"
    "templates" = "$assetsDir\templates"
    "references" = "$assetsDir\references"
}

$destDir = $destinationMap[$Category]

if (-not (Test-Path $destDir)) {
    Write-ColorOutput "📁 Création du dossier : $destDir" "Info"
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
}

# ============================================
# NAMING
# ============================================

if ([string]::IsNullOrEmpty($NewName)) {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
    $cleanName = $baseName -replace '[^a-zA-Z0-9_-]', '_'
    $NewName = "${Category}_${cleanName}_${timestamp}${extension}"
} else {
    # Ajouter l'extension si manquante
    if (-not $NewName.EndsWith($extension)) {
        $NewName += $extension
    }
}

$destPath = Join-Path $destDir $NewName

# ============================================
# COPIE & OPTIMISATION
# ============================================

Write-ColorOutput "📋 Résumé :" "Info"
Write-ColorOutput "  Source      : $($file.FullName)" "Info"
Write-ColorOutput "  Destination : $destPath" "Info"
Write-ColorOutput "  Catégorie   : $Category" "Info"
Write-ColorOutput "  Taille      : $([math]::Round($file.Length / 1KB, 2)) KB`n" "Info"

# Confirmation
$confirm = Read-Host "Procéder à la copie ? (O/N)"
if ($confirm -ne "O" -and $confirm -ne "o") {
    Write-ColorOutput "❌ Opération annulée" "Warning"
    exit 0
}

try {
    Copy-Item $file.FullName $destPath -Force
    Write-ColorOutput "✅ Asset copié avec succès !" "Success"
    
    # ============================================
    # MISE À JOUR CSV
    # ============================================
    
    $csvPath = "$assetsDir\assets-database.csv"
    
    $newRow = @{
        Categorie = $Category
        Fichier = $NewName
        Type = if ($extension -in @(".jpg", ".jpeg", ".png")) { "Photo" } elseif ($extension -eq ".svg") { "Vectoriel" } else { "Document" }
        Format = $extension.TrimStart('.')
        Dimensions = "À définir"
        Taille_Ko = [math]::Round($file.Length / 1KB, 0)
        Usage = if ($Description) { $Description } else { "À définir" }
        Date_Ajout = Get-Date -Format "yyyy-MM-dd"
        Status = "Actif"
        Notes = "Ajouté automatiquement"
    }
    
    $csv = Import-Csv $csvPath
    $csv += [PSCustomObject]$newRow
    $csv | Export-Csv $csvPath -NoTypeInformation -Encoding UTF8
    
    Write-ColorOutput "✅ Base de données mise à jour" "Success"
    
    # ============================================
    # INSTRUCTIONS FINALES
    # ============================================
    
    Write-ColorOutput "`n📝 PROCHAINES ÉTAPES :" "Info"
    Write-ColorOutput "  1. Vérifier le fichier : $destPath" "Info"
    Write-ColorOutput "  2. Optimiser si nécessaire (TinyPNG, SVGO...)" "Info"
    Write-ColorOutput "  3. Mettre à jour ASSETS-INVENTORY.md" "Info"
    Write-ColorOutput "  4. Commit Git avec message descriptif`n" "Info"
    
    Write-ColorOutput "🎉 Asset ajouté avec succès !" "Success"
    
} catch {
    Write-ColorOutput "❌ Erreur lors de la copie : $_" "Error"
    exit 1
}

# ============================================
# USAGE
# ============================================
<#
.SYNOPSIS
    Ajoute automatiquement un asset dans la structure organisée

.EXAMPLE
    .\add-asset.ps1 -SourceFile "C:\Downloads\logo.svg" -Category "brand"
    
.EXAMPLE
    .\add-asset.ps1 -SourceFile "photo.jpg" -Category "team" -NewName "team_ceo_2024.jpg" -Description "Photo CEO officielle"
#>
