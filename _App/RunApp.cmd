:: RunApp.cmd
:: Batch file for runing of app
:: Author: Milos Petrasinovic <mpetrasinovic@pr-dc.com>
:: PR-DC, Republic of Serbia
:: info@pr-dc.com
:: --- INPUTS ---
::  appFileName - name of python app file
::  pythonPath - path to python used for app
::  appCommands - aditional commands to execute
:: --------------------
::
:: Copyright (C) 2021 PR-DC <info@pr-dc.com>
:: 
:: This program is free software: you can redistribute it and/or modify
:: it under the terms of the GNU Lesser General Public License as 
:: published by the Free Software Foundation, either version 3 of the 
:: License, or (at your option) any later version.
::  
:: This program is distributed in the hope that it will be useful,
:: but WITHOUT ANY WARRANTY; without even the implied warranty of
:: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
:: GNU Lesser General Public License for more details.
::  
:: You should have received a copy of the GNU Lesser General Public License
:: along with this program.  If not, see <https://www.gnu.org/licenses/>.
::
:: --------------------
@echo off
set appFileName="PRDC_QRCodeGenerator.py"

:: --------------------
:: Set directory
setlocal
set realPath=%~dp0
cd /d %realPath%

:: Get admin rights
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"  
if '%errorlevel%' NEQ '0' ( echo Requesting administrative privileges... ) else ( goto gotAdmin )
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"  
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"  
    "%temp%\getadmin.vbs"  
    exit /B
:gotAdmin

:: Execute commands
cmd /k "cd ../ & Scripts\activate & cd %realPath% & python %appFileName%"
:: --------------------