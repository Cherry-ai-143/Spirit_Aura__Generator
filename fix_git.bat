@echo off
cd /d "c:\Users\91734\Downloads\SPIRIT CODE-20260209T030538Z-1-001"
echo Aborting merge...
git merge --abort
echo Checking status...
git status
echo.
echo Pulling latest changes...
git pull origin main --no-edit
echo.
echo Pushing changes...
git push origin main
echo Done!
pause
