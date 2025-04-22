# 📁 FileRenom

**FileRenom** is a Python-based GUI application that allows you to batch rename files with various numbering options and a modern interface.

---

##  Running with Python

1. Make sure Python is installed.
2. Run the following command in the terminal or command prompt:

```bash
py FileRenom.py
```

>  **Tip**: If you don't want to use the application icon, remove the following line in `FileRenom.py`:
```python
root.iconbitmap("Icon.ico")
```

---

##  Creating the `.exe` File

1. Install **Nuitka** (only once):

```bash
pip install nuitka
```

2. Compile `FileRenom.py` into a standalone `.exe` application:

```bash
python -m nuitka FileRenom.py --standalone --enable-plugin=tk-inter --windows-icon-from-ico=Icon.ico --windows-disable-console --output-dir=dist
```

---

##  Creating an Installer with Inno Setup

1. Download and install Inno Setup from:  
    [https://jrsoftware.org/isdl.php](https://jrsoftware.org/isdl.php)

2. Create a file named `FileRenom.iss` in the project directory with the following content:

```ini
[Setup]
AppName=FileRenom
AppVersion=1.0
DefaultDirName={commonpf}\FileRenom
DefaultGroupName=FileRenom
OutputBaseFilename=FileRenomInstaller
Compression=lzma
SolidCompression=yes
SetupIconFile=Icon.ico
DisableProgramGroupPage=yes

[Files]
Source: "dist\FileRenom.dist\*"; DestDir: "{app}"; Flags: recursesubdirs
Source: "Icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional icons:"; Flags: unchecked

[Icons]
Name: "{group}\FileRenom"; Filename: "{app}\FileRenom.exe"; IconFilename: "{app}\Icon.ico"
Name: "{commondesktop}\FileRenom"; Filename: "{app}\FileRenom.exe"; Tasks: desktopicon; IconFilename: "{app}\Icon.ico"
Name: "{group}\Uninstall FileRenom"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\FileRenom.exe"; Description: "Launch FileRenom"; Flags: nowait postinstall skipifsilent
```

3. Save the `.iss` file in the `FileRenom` directory.

4. Open the `.iss` file with **Inno Setup**, then press `Ctrl + F9` to compile it into an installer `.exe`.


🔗 **Quick Download for Windows**:  [Download](https://github.com/Naoda7/RenameFiles/releases/tag/renamefiles)

---
