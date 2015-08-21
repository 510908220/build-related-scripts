;--------------------------------
; Headers
;--------------------------------
!include "MUI2.nsh"
!include "FileFunc.nsh"
;--------------------------------
;ShowInstDetails show;ÓÃÓÚµ÷ÊÔ
;--------------------------------
SilentInstall silent
;---------------------------------------------------------
; °²×°°æ±¾ÐÅÏ¢
;--------------------------------------------------------
!define FILE_NAME 'Ä§»ÃÓ¢ÐÛ'
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
OutFile 'make_uninstaller.exe'
RequestExecutionLevel admin #NOTE: You still need to check user rights with UserInfo!

;SetCompressor zlib

!define MUI_ICON icon.ico
!define MUI_UNICON icon.ico
!define MUI_WELCOMEFINISHPAGE_BITMAP "welcome.bmp"
!define MUI_UNWELCOMEFINISHPAGE_BITMAP "welcome.bmp"


!define MUI_STARTMENUPAGE_REGISTRY_ROOT HKCU
!define MUI_STARTMENUPAGE_REGISTRY_KEY "Software\S2 Games\Strife"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "Start Menu Folder"

;Lang
!define MUI_LANGDLL_ALLLANGUAGES
!define MUI_LANGDLL_REGISTRY_ROOT "HKCU" 
!define MUI_LANGDLL_REGISTRY_KEY "Software\S2 Games\Strife"
!define MUI_LANGDLL_REGISTRY_VALUENAME "Installer Language"
;Lang
InstallDir "$EXEDIR"

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
!insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_COMPONENTS
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH
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
	SetOutPath "$0"
	WriteUninstaller "$0\uninstall.exe"
SectionEnd


Section "un.${FILE_NAME}"
	ReadRegStr $0 HKCU "Software\S2 Games\Strife" "InstallDir"

	; Game files
	RMDir /r "$0\modelviewer"
	RMDir /r "$0\editor"
	RMDir /r "$0\game"
	RMDir /r "$0\base"
	RMDir /r "$0\compat"
	RMDir /r "$0\Update"
	RMDir /r "$0\locales"
	RMDir /r "$0\updater"
	RMDir /r "$0\game\bink"
	RMDir /r "$0\updater_resume_data"


	Delete "$0\vcredist_x86.exe"
	RMDir /r "$0\directxredist"
	
	RMDir /r "$0\bin"
	
	Delete "$0\ca-bundle.crt"
	Delete "$0\icon.ico"
	Delete "$0\libraries.txt"
	Delete "$0\license.txt"
	Delete "$0\strife.manifest"
	Delete "$0\strife.version"
	Delete "$0\strife_update.log"
	
	
	; Shortcuts
	SetShellVarContext all
	!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
	Delete "$DESKTOP\Ä§»ÃÓ¢ÐÛ.lnk"
	Delete "$SMPROGRAMS\$StartMenuFolder\${FILE_NAME}.lnk"
	;Delete "$SMPROGRAMS\$StartMenuFolder\Strife Repair.lnk"
	;Delete "$SMPROGRAMS\$StartMenuFolder\Strife Update.lnk"
	Delete "$SMPROGRAMS\$StartMenuFolder\Ä§»ÃÓ¢ÐÛÐ¶ÔØ.lnk"
	RMDir "$SMPROGRAMS\$StartMenuFolder"
	!insertmacro MUI_STARTMENU_WRITE_END

	; Registry keys
	DeleteRegKey HKCR "strife"
	DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\strife"
	DeleteRegKey HKCU "Software\S2 Games"
	;DeleteRegKey HKLM "Software\Classes\strife.Replay"

	; Uninstaller
	Delete "$0\Ä§»ÃÓ¢ÐÛÐ¶ÔØ.exe"
	RMDir "$0"
SectionEnd

Section /o "un.ÓÃ»§Êý¾Ý(ÅäÖÃ, ½ØÍ¼,...)"
	RMDir /r "$DOCUMENTS\Strife"
SectionEnd
;--------------------------------
