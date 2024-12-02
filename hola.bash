#!/usr/bin/env bash
# Store icon and AppImage in variable
icon_path=$HOME/Descargas/obsidian-icon.png
exec_path=$HOME/Descargas/Obsidian-1.6.3.AppImage

# Copy both files
cp $icon_path ~/.local/share/applications/
cp $exec_path ~/.local/share/applications/

# Create a Desktop Entry file
echo "[Desktop Entry]
Name=Obsidian
Categories=<AudioVideo|Audio|Video|Development|Education|Game|Graphics|Network|Office|Science|Settings|System|Utility
>
Icon=$icon_path
Exec=$exec_path" >> ~/.local/share/applications/Obsidian.desktop