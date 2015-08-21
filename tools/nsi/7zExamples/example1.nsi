Name "nsis7zsample"

; The file to write
OutFile "nsis7zsample.exe"

; The default installation directory
InstallDir "$EXEDIR"

Section "" 
  File 7z.exe
  nsExec::Exec '"$INSTDIR\7za.exe" x "$INSTDIR\bastion_act1_intro.7z.001" -o"$INSTDIR\out"'
  ;Delete "7za.exe"  
SectionEnd ; end the section
