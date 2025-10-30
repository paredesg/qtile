from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess

mod = "mod4"
terminal = guess_terminal()
myTerm = "alacritty"

keys = [

# Switch between windows
# Basculer entre les fenêtres
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

# Move windows between left/right columns or move up/down in current stack.
# Moving out of range in Columns layout will create new column.
# Déplacer les fenêtres entre les colonnes gauche/droite ou monter/descendre dans la pile actuelle.
# Sortir de la plage en disposition « Colonnes » créera une nouvelle colonne.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

# Grow windows. If current window is on the edge of screen and direction
# will be to screen edge - window would shrink.
# Agrandir les fenêtres. Si la fenêtre actuelle est au bord de l’écran et que la direction choisie pointe vers ce bord, 
# la fenêtre rétrécira.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
# Toggle between split and unsplit sides of stack.
# Split = all windows displayed
# Unsplit = 1 window displayed, like Max layout, but still with
# multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

# Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the Qtile config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "control"], "Return", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),


# My application shortcuts.

    #Key([mod], "b", lazy.spawn("bitwarden"), desc="Launch bitwarden."),
    #Key([mod], "f", lazy.spawn("firefox"), desc="Launch firefox."),
    #Key([mod], "a", lazy.spawn("flameshot"), desc="Launch flameshot."),
    #Key([mod], "g", lazy.spawn("gimp"), desc="Launch gimp."),
    #Key([mod], "p", lazy.spawn("joplin-desktop"), desc="Launch joplin."),
    #Key([mod], "a", lazy.spawn("libreoffice"), desc="Launch libreoffice."),
    #Key([mod], "u", lazy.spawn("pavucontrol"), desc="Launch pavucontrol."),
    #Key([mod], "o", lazy.spawn("rofi -combi-modi window,drun,ssh -font \"Jetbrains Mono 12\" -show combi"), desc="Launch rofi."),
    #Key([mod], "r", lazy.spawn("rustdesk"), desc="Launch rustdesk."),
    #Key([mod], "t", lazy.spawn("thunar"), desc="Launch thunar."),
    #Key([mod], "c", lazy.spawn("vlc"), desc="Launch vlc."),
    #Key([mod], "v", lazy.spawn("codium"), desc="Launch vscodium."),

# Volume Keys
    Key([mod, "control"], "i", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Decrease volume."),
    Key([mod, "control"], "p", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Increase volume."),
    Key([mod, "control"], "o", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mute audio."),

# Brightness Keys
#    Key([mod, "control"], "b", lazy.spawn("brightnessctl set +10%"), desc="Increase brightness."),
#    Key([mod, "control"], "n", lazy.spawn("brightnessctl set 10%-"), desc="Decrease brightness.")


]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = []

# Group("1", screen_affinity=0),
# Group("2", screen_affinity=0),
# Group("3", screen_affinity=0),
# Group("4", screen_affinity=0),
# Group("5", screen_affinity=0),
# Group("6", screen_affinity=1),
# Group("7", screen_affinity=1),
# Group("8", screen_affinity=1),
# Group("9", screen_affinity=1),

# FOR QWERTY KEYBOARDS
#group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

# FOR FRENCH AZERTY KEYBOARDS
group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "minus", "egrave", "underscore", "ccedilla", "agrave",]

group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]


group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "treetab", "floating",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

colors = [
    ["#1a1b26", "#1a1b26"],  # bg        (primary.background)
    ["#a9b1d6", "#a9b1d6"],  # fg        (primary.foreground)
    ["#32344a", "#32344a"],  # color01   (normal.black)
    ["#f7768e", "#f7768e"],  # color02   (normal.red)
    ["#9ece6a", "#9ece6a"],  # color03   (normal.green)
    ["#e0af68", "#e0af68"],  # color04   (normal.yellow)
    ["#7aa2f7", "#7aa2f7"],  # color05   (normal.blue)
    ["#ad8ee6", "#ad8ee6"],  # color06   (normal.magenta)
    ["#0db9d7", "#0db9d7"],  # color15   (bright.cyan)
    ["#444b6a", "#444b6a"]   # color[9]  (bright.black)
]

layout_theme = {
    "border_width" : 1,
    "margin" : 1,
    "border_focus" : colors[6],
    "border_normal" : colors[0],
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


widget_defaults = dict(
    font="JetBrainsMono Nerd Font Propo Bold",
    # font="Ubuntu Bold",
    fontsize=14,
    padding=0,
    background=colors[0],
)


extension_defaults = widget_defaults.copy()

sep = widget.Sep(linewidth=1, padding=8, foreground=colors[9])

screens = [
    Screen(
        bottom=bar.Bar(
            widgets = [
                widget.Spacer(length = 8),
                widget.Image(
                    filename = "~/.config/qtile/icons/hal-9000-eye.jpg",
                    scale = "False",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("qtilekeys-yad")},
                ),
                widget.Prompt(
                    font = "Ubuntu Mono",
                    fontsize=14,
                    foreground = colors[1]
                ),
                widget.GroupBox(
                    fontsize = 16,
                    margin_y = 5,
                    margin_x = 5,
                    padding_y = 0,
                    padding_x = 2,
                    borderwidth = 3,
                    active = colors[8],
                    inactive = colors[9],
                    rounded = False,
                    highlight_color = colors[0],
                    highlight_method = "line",
                    this_current_screen_border = colors[7],
                    this_screen_border = colors [4],
                    other_current_screen_border = colors[7],
                    other_screen_border = colors[4],
                ),
                sep,
                widget.CurrentLayout(
                    foreground = colors[1],
                    padding = 5
                ),
                sep,
                widget.WindowName(
                    foreground = colors[6],
                    padding = 8,
                    max_chars = 40
                ),
                widget.Clipboard(),
                sep,
                widget.CPU(
                    foreground = colors[4],
                    padding = 8, 
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e btop')},
                    format="CPU: {load_percent}%",
                ),
                sep,
                widget.Memory(
                    foreground = colors[8],
                    padding = 8, 
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e btop')},
                    format = 'Mem: {MemUsed:.0f}{mm}',
                ),
                sep,
                widget.DF(
                    update_interval = 60,
                    foreground = colors[5],
                    padding = 8, 
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('notify-disk')},
                    partition = '/',
                    #format = '[{p}] {uf}{m} ({r:.0f}%)',
                    format = '{uf}{m} free',
                    fmt = 'Disk: {}',
                    visible_on_warn = False,
                ),
                # sep,
                # widget.Battery(
                #     foreground=colors[6],           # pick a palette slot you like
                #     padding=8,
                #     update_interval=5,
                #     format='{percent:2.0%} {char} {hour:d}:{min:02d}',  # e.g. "73% ⚡ 1:45"
                #     fmt='Bat: {}',
                #     charge_char='',               # shown while charging
                #     discharge_char='',            # Nerd icon; use '-' if you prefer plain ascii
                #     full_char='✔',                 # when at/near 100%
                #     unknown_char='?',
                #     empty_char='!', 
                #     mouse_callbacks={
                #         'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e upower -i $(upower -e | grep BAT)'),
                #     },
                # ),
                sep,
                widget.Volume(
                    foreground = colors[7],
                    padding = 8, 
                    fmt = 'Vol: {}',
                ),
                sep,
                widget.Clock(
                    foreground = colors[8],
                    padding = 8, 
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('notify-date')},
                    ## Uncomment for date and time 
                    format = "%a, %b %d - %H:%M",
                    ## Uncomment for time only
                    # format = "%I:%M %p",
                ),
                widget.Systray(padding = 6),
                widget.Spacer(length = 8),
            ],
            # 24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            margin=[0, 0, 1, 0], 
            size=30
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])





# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
