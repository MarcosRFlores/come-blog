#!/bin/bash

APP_NAME="come-blog"
INSTALL_DIR="$HOME/.local/bin"
ICON_DIR="$HOME/.local/share/icons"
DESKTOP_DIR="$HOME/.local/share/applications"

# Crear directorios
mkdir -p "$INSTALL_DIR" "$ICON_DIR" "$DESKTOP_DIR"

# Compilar con PyInstaller
pyinstaller --onefile --windowed --icon=odin.ico --add-data="odin.png:." textEditor.py

# Copiar archivos
cp dist/textEditor "$INSTALL_DIR/$APP_NAME"
cp odin.png "$ICON_DIR/$APP_NAME.png"

# Crear archivo .desktop
cat > "$DESKTOP_DIR/$APP_NAME.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Come's Blog
Comment=Editor de texto simple
Exec=$INSTALL_DIR/$APP_NAME
Icon=$ICON_DIR/$APP_NAME.png
Terminal=false
Categories=Utility;TextEditor;
EOF

# Hacer ejecutable
chmod +x "$INSTALL_DIR/$APP_NAME"
chmod +x "$DESKTOP_DIR/$APP_NAME.desktop"

# Actualizar base de datos
update-desktop-database "$DESKTOP_DIR"

echo "✓ Instalación completada"
echo "  Ejecutable: $INSTALL_DIR/$APP_NAME"
echo "  Puedes ejecutarlo desde el menú de aplicaciones o con: $APP_NAME"