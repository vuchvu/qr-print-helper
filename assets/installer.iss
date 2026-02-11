; Inno Setup Script for QR Print Helper

[Setup]
AppName=QR Print Helper
AppVersion=1.0.5
AppPublisher=Your Name
AppPublisherURL=https://github.com/vuchvu/qr-print-helper
DefaultDirName={userdocs}\QR Print Helper
DefaultGroupName=QR Print Helper
OutputDir=..\build
OutputBaseFilename=qr-print-helper-installer
Compression=lzma2
SolidCompression=yes
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
WizardStyle=modern
SetupIconFile=icon.ico
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
VersionInfoVersion=1.0.5

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"

[Tasks]
Name: "desktopicon"; Description: "デスクトップにショートカットを作成"; GroupDescription: "追加のアイコン:"

[Files]
Source: "..\build\qr-print-helper.exe"; DestDir: "{app}"
Source: "..\build\README.txt"; DestDir: "{app}"; Flags: isreadme

[Icons]
Name: "{group}\QR Print Helper"; Filename: "{app}\qr-print-helper.exe"
Name: "{autodesktop}\QR Print Helper"; Filename: "{app}\qr-print-helper.exe"; Tasks: desktopicon

[Run]
; インストール後に起動するか確認
FileName: "{app}\qr-print-helper.exe"; Description: "QR Print Helperを起動"; Flags: nowait postinstall skipifsilent