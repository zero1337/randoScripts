@if (@CodeSection == @Batch) @then

@echo off
    set SendKeys=CScript //nologo //E:JScript "%~F0"
    cls
    color 0a
    :loop
        %SendKeys% "^{ESC}"
        timeout /t 2 /nobreak >nul
        %SendKeys% "^{ESC}"
        timeout /t 222 /nobreak >nul
    goto :loop

@end

var WshShell = WScript.CreateObject("WScript.Shell");
WshShell.SendKeys(WScript.Arguments(0));