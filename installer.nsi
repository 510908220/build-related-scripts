;--------------------------------
; Headers
;--------------------------------
!include "MUI2.nsh"
!include "FileFunc.nsh"
;--------------------------------
;ShowInstDetails show;用于调试
;--------------------------------

;---------------------------------------------------------
; 安装版本信息
;--------------------------------------------------------
!define FILE_NAME '魔幻英雄'
!define FILE_VERSION '0.0.1.0'
!define FILE_INSTVERSION '0.0.1.0'
!define FILE_OWNER 'Strife Project'
VIAddVersionKey "ProductName" '${FILE_NAME}'
VIAddVersionKey "ProductVersion" '${FILE_VERSION}'
VIAddVersionKey "CompanyName" '${FILE_OWNER}'
VIAddVersionKey "LegalCopyright" 'Copyright 2014 ${FILE_OWNER}'
VIAddVersionKey "FileDescription" '${FILE_NAME} Installer'
VIAddVersionKey "FileVersion" '${FILE_INSTVERSION}'
VIProductVersion '${FILE_INSTVERSION}'
;-----------------------------------------------------------

Name '${FILE_NAME}'
OutFile '${FILE_NAME}-${FILE_VERSION}-setup.exe'
RequestExecutionLevel admin #NOTE: You still need to check user rights with UserInfo!

;SetCompressor zlib

!define MUI_ICON icon.ico
!define MUI_WELCOMEFINISHPAGE_BITMAP "welcome.bmp"

!define MUI_STARTMENUPAGE_REGISTRY_ROOT HKCU
!define MUI_STARTMENUPAGE_REGISTRY_KEY "Software\S2 Games\Strife"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "Start Menu Folder"

;Lang
!define MUI_LANGDLL_ALLLANGUAGES
!define MUI_LANGDLL_REGISTRY_ROOT "HKCU" 
!define MUI_LANGDLL_REGISTRY_KEY "Software\S2 Games\Strife"
!define MUI_LANGDLL_REGISTRY_VALUENAME "Installer Language"
;Lang
InstallDir "$PROGRAMFILES\${FILE_NAME}\"

Var StartMenuFolder
;--------------------------------

;-------------------------------
; Test if Visual Studio Redistributables 2010 SP1 installed
; Returns -1 if there is no VC redistributables intstalled
;--------------------------------
;Function CheckVCRedist
   ;Push $R0
   ;ClearErrors
   ;ReadRegDword $R0 HKLM "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{7299052b-02a4-4627-81f2-1818da5d550d}" "Version"

   ; if VS 2005+ redist SP1 not installed, install it
   ;IfErrors 0 VSRedistInstalled
   ;StrCpy $R0 "-1"

;VSRedistInstalled:
   ;Exch $R0
;FunctionEnd
;--------------------------------

;--------------------------------
; Pages
;--------------------------------
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "license.txt"
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
DirText "魔幻英雄将安装至以下文件夹。要安装到不同文件夹，单击 [浏览(B)] 并选择其他的文件夹。 $_CLICK"
!insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

;--------------------------------

;--------------------------------
; Languages
;--------------------------------
!insertmacro MUI_LANGUAGE "SimpChinese"
;!insertmacro MUI_LANGUAGE "English"
;--------------------------------


;Lang
!insertmacro MUI_RESERVEFILE_LANGDLL
;Installer Functions
Function .onInit

  !insertmacro MUI_LANGDLL_DISPLAY

FunctionEnd
;Lang

;--------------------------------
; Sections
;--------------------------------
RequestExecutionLevel user
Section "${FILE_NAME}" main_install
	SetOutPath "$INSTDIR"
	; Visual studio redistributables
	File vcredist_x86.exe
	;Call CheckVCRedist
	;Pop $R0
	;StrCmp $R0 "-1" installvcredist skipvcredist
	;installvcredist:
	ExecWait 'vcredist_x86.exe /q /norestart'
	;Delete "$INSTDIR\vcredist_x86.exe"
	;skipvcredist:

	; DirectX
	SetOutPath "$INSTDIR\directxredist"
	File directxredist\*
	ExecWait '$INSTDIR\directxredist\dxsetup.exe /silent'
	;Delete "$INSTDIR\directxredist\*"
	SetOutPath "$INSTDIR"
	;RMDir "$INSTDIR\directxredist"

	;/*
	; Core files
	File ca-bundle.crt
	File icon.ico
	File libraries.txt
	File license.txt
	File strife.manifest
	File strife.version
	File 魔幻英雄卸载.exe
	
	; Binaries
	SetOutPath "$INSTDIR\bin"
	File bin\*
	
	SetCompress off
	
	; Base files
	SetOutPath "$INSTDIR\base"
	File base\*.s2z
	
	; Game files
	SetOutPath "$INSTDIR\game"
	File game\*.s2z
	
	; Game bink files
	SetOutPath "$INSTDIR\game\bink"
	File game\bink\*

	; updater files
	SetOutPath "$INSTDIR\updater"
	File updater\*

	SetCompress auto
	
	SetOutPath "$INSTDIR"
	
	; Default settings
	CreateDirectory "$DOCUMENTS\Strife\game\"
	FileOpen $9 "$DOCUMENTS\Strife\game\startup.cfg" w


;-------------------------------------------------
;Lang
	FileWrite $9 "SetSave host_language zh$\r$\n"
;Lang
	FileClose $9
;------------------------------------------------


	;Create start menu shortcuts
	SetShellVarContext all
	!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
 	CreateDirectory "$SMPROGRAMS\$StartMenuFolder"
	CreateShortCut "$SMPROGRAMS\$StartMenuFolder\${FILE_NAME}.lnk" "$INSTDIR\bin\strife.exe" "" "$INSTDIR\bin\strife.exe"
	;CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Strife Repair.lnk" "$INSTDIR\bin\strife.exe" "-repair" "$INSTDIR\bin\strife.exe"
	;CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Strife Update.lnk" "$INSTDIR\bin\strife.exe" "-update" "$INSTDIR\bin\strife.exe"
	;CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Model Viewer.lnk" "$INSTDIR\strife.exe" "-mod game;modelviewer" "$INSTDIR\strife.exe"
	;WriteINIStr "$SMPROGRAMS\$StartMenuFolder\Match Replays.url" "InternetShortcut" "URL" "http://replays.heroesofnewerth.com/"
	;WriteINIStr "$SMPROGRAMS\$StartMenuFolder\Create Account.url" "InternetShortcut" "URL" "https://www.heroesofnewerth.com/"
	;WriteINIStr "$SMPROGRAMS\$StartMenuFolder\Player Rankings.url" "InternetShortcut" "URL" "http://www.heroesofnewerth.com/players/"
	CreateShortCut "$SMPROGRAMS\$StartMenuFolder\魔幻英雄卸载.lnk" "$INSTDIR\魔幻英雄卸载.exe" "" "$SYSDIR\shell32.dll" 145
 	!insertmacro MUI_STARTMENU_WRITE_END

	; Create URL association
	;WriteRegStr HKCR "hon" "" "URL:Strife Server"
	;WriteRegStr HKCR "hon" "URL Protocol" ""
	;WriteRegStr HKCR "hon\DefaultIcon" "" "$INSTDIR\strife.exe"
	;WriteRegStr HKCR "hon\shell\open\command" "" '$INSTDIR\strife.exe -connect %1'

	WriteRegStr HKCU "Software\S2 Games\Strife" "InstallDir" "$INSTDIR"

	; Replay file association
	;WriteRegStr HKLM "Software\Classes\.honreplay" "" "hon.Replay"
	;WriteRegStr HKLM "Software\Classes\hon.Replay\shell" "" "WatchReplay"
	;WriteRegStr HKLM "Software\Classes\hon.Replay\shell\WatchReplay" "" "Watch replay"
	;WriteRegStr HKLM "Software\Classes\hon.Replay\shell\WatchReplay\command" "" '"$INSTDIR\strife.exe" set host_autoexec StartReplay #SystemPath(%1)#'
	;WriteRegStr HKLM "Software\Classes\hon.Replay\DefaultIcon" "" "$INSTDIR\strife.exe"
	
	; Uninstaller
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\strife" "DisplayName" "${FILE_NAME}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\strife" "UninstallString" "$INSTDIR\魔幻英雄卸载.exe"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\strife" "InstallLocation" "$INSTDIR"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\strife" "DisplayIcon" "$INSTDIR\bin\${FILE_NAME}.exe"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\strife" "Publisher" "S2 Games"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\strife" "HelpLink" "http://strife.s2games.com/"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\strife" "URLUpdateInfo" "http://strife.s2games.com/"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\strife" "DisplayVersion" "0.0.1"
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\strife" "NoModify" 1
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\strife" "NoRepair" 1
	
	;WriteUninstaller "$INSTDIR\uninstall.exe"

SectionEnd

Section "桌面快捷方式"
	CreateShortCut "$DESKTOP\${FILE_NAME}.lnk" "$INSTDIR\bin\strife.exe" "" "$INSTDIR\bin\strife.exe"
SectionEnd


;--------------------------------
