#!/bin/bash
## Script para cambiar apariencia de xubuntu 19.04. 
#Creador: Adolfo Silerio a.k.a ZAYRONXIO
#mail: zayronxio@gmail.com
###########
#Installa apps:
echo install apps, Your password will be used only to install the necessary packages.
sudo apt install xfce4-appmenu-plugin python python-gi plank
echo install configs for xfce4.12.

xfconf-query -c xfce4-keyboard-shortcuts -n -t string -p "/commands/custom/<Primary><Alt>k" -s $HOME/.local/share/katalina/katalina.sh && xfconf-query -c xfwm4 -p /general/button_layout -s CMH && xfconf-query -c xsettings -p /Gtk/FontName -s "SF UI Display 10"

echo giving permissions to katalina script.
chmod +x $HOME/.local/share/katalina/katalina.sh
chmod +x $HOME/.local/share/katalina/katalina
#echo moving katalina launcher script
sudo rm /bin/katalina
sudo cp $HOME/.local/share/katalina/katalina /bin
#
echo created plank starter launcher
echo -e "[Desktop Entry]\nEncoding=UTF-8\nVersion=0.9.4\nType=Application\nName=dock\nComment[en]=Dock similar to "macos"\nComment[es]=dock similar al de macos\nExec=plank OnlyShowIn=XFCE;\nStartupNotify=false\nTerminal=false\nHidden=false" | cat > $HOME/.config/autostart/dock.desktop
#
echo created katalina-script starter launcher
echo -e "[Desktop Entry]\nName=general theme\nName[es_MX]=Tema General\nVersion=0.1\nComment=change from night theme to light theme in one click\nType=Application\nEncoding=UTF-8\nIcon=katalina\nExec=katalina\nCategories=XFCE;GTK;Settings;DesktopSettings;X-XFCE;X-XFCE-SettingsDialog;X-XFCE-PersonalSettings;\nNoDisplay=false" | cat > $HOME/.local/share/applications/katalina.desktop
#
echo giving permissions to katalina-script
chmod +x $HOME/.local/share/applications/katalina.desktop
#
echo Start plank
plank &&


