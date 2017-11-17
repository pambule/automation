@echo off
set LOG="C:\Users\pranil_ambule\Documents\wsman-simulator-dev\automation\bios-update\PE2600.log"
set PKG="C:\Users\pranil_ambule\Documents\wsman-simulator-dev\automation\bios-update\Latitude E5470\Latitude_E5x70_Precision_3510_1.17.3.exe"
    echo Executing %PKG% >>%LOG%
    %PKG% /s /l=%LOG%
    set ExitCode=%ErrorLevel%
    if %ExitCode% EQU 0 echo Result: SUCCESSFUL >>%LOG%
    if %ExitCode% EQU 1 echo Result: UNSUCCESSFUL >>%LOG%
    if %ExitCode% EQU 2 echo Result: REBOOT_REQUIRED >>%LOG%
    if %ExitCode% EQU 3 echo Result: DEP_SOFT_ERROR >>%LOG%
    if %ExitCode% EQU 4 echo Result: DEP_HARD_ERROR >>%LOG%
    if %ExitCode% EQU 5 echo Result: QUAL_HARD_ERROR >>%LOG%
    if %ExitCode% EQU 6 echo Result: REBOOTING_SYSTEM >>%LOG%