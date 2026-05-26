Write-Host ""
Write-Host "STARTING ABSALOM COMMAND CENTER..." -ForegroundColor Cyan
Write-Host ""

Start-Process powershell -ArgumentList '-NoExit', '-Command', '
cd "$env:USERPROFILE\Desktop\absalom-command-center"
docker compose up
'

Start-Sleep -Seconds 8

Start-Process powershell -ArgumentList '-NoExit', '-Command', '
cd "$env:USERPROFILE\Desktop\absalom-command-center\apps\web"
npm run dev
'

Write-Host ""
Write-Host "ABSALOM COMMAND CENTER STARTED" -ForegroundColor Green
Write-Host ""
