import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess
import commands


class Handler:
    def gtk_main_quit(self, *args):
        Gtk.main_quit()


    def on_button_clicked (self, button1):
        commands.getstatusoutput('xfconf-query -c xsettings -p /Net/IconThemeName -s Os-Catalina-icons && xfconf-query -c xsettings -p /Net/ThemeName -s Os-Catalina-gtk && xfconf-query -c xfwm4 -p /general/theme  -s Os-Catalina-gtk && xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s $HOME/.local/share/wallpapers/Walllight.jpg && xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorVGA-1/workspace0/last-image -s $HOME/.local/share/wallpapers/Walllight.jpg && xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor1/image-path -s $HOME/.local/share/wallpapers/Walllight.jpg && xfdesktop -R')

    def on_button1_clicked (self, button2):
        commands.getstatusoutput('xfconf-query -c xsettings -p /Net/IconThemeName -s Os-Catalina-Night && xfconf-query -c xsettings -p /Net/ThemeName -s Os-Catalina-Gtk-night && xfconf-query -c xfwm4 -p /general/theme  -s Os-Catalina-Gtk-night && xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s $HOME/.local/share/wallpapers/Wallnight.jpg && xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorVGA-1/workspace0/last-image -s $HOME/.local/share/wallpapers/Wallnight.jpg && xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor1/image-path -s $HOME/.local/share/wallpapers/Wallnight.jpg && xfdesktop -R')

builder = Gtk.Builder()
builder.add_from_file("katalina1.ui")
builder.connect_signals(Handler())

window = builder.get_object("window_general")
window.show_all()

Gtk.main()


