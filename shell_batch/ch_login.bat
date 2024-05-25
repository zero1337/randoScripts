@if (@CodeSection == @Batch) @then
@echo off

set webpage="https://accounts.google.com"
set username="username"
set password="password"

REM Open webpage in Chrome
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" -incognito %webpage%

REM Wait for webpage to load
timeout /t 3

    set SendKeys=CScript //nologo //E:JScript "%~F0"
    cls
    color 0a
        %SendKeys% %username%
        timeout /t 1 /nobreak >nul
		%SendKeys% "{ENTER}"
		timeout /t 3 /nobreak >nul
        %SendKeys% %password%
        timeout /t 1 /nobreak >nul
		%SendKeys% "{ENTER}"

@end

var WshShell = WScript.CreateObject("WScript.Shell");
WshShell.SendKeys(WScript.Arguments(0));

"C:\Program Files\Google\Chrome\Application\chrome.exe"