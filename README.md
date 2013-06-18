# Find++ [![Donate on Gittip](http://badgr.co/gittip/twolfson.png)](https://www.gittip.com/twolfson/)

Find functionality from [Notepad++][npp] for [Sublime Text 2][subl].

[npp]: http://notepad-plus-plus.org/
[subl]: http://www.sublimetext.com/2

This includes:

- `Find: In Current File` - `Find -> In Current Document` in Notepad++
- `Find: In Open Files` - `Find -> In Opened Documents` in Notepad++
    - Encapsulates `Find -> Replace In Opened Documents` via `Find in Files` prompt that is opened

Additional functionality has been added:

- `Find: In Project` - Search all files and folders listed in the sidebar
- `Find: In...` - Opens a panel to pick a directory to search in

## Installation
`Find++` is available via [Package Control][pkg-ctrl] and can be found as `Find++`.

[pkg-ctrl]: http://wbond.net/sublime_packages/package_control

## Documentation
All commands are accessible via the Command Palette, `Ctrl + Shift + P` on Windows/Linux, `Command + Shift + P` on Mac.

![command_palette](https://f.cloud.github.com/assets/902488/279674/a552365a-9134-11e2-8c89-603fbb89b606.png)

The available commands are:

- `Find: In Current File` - Open `Find in Files` prompt with current file as target
- `Find: In Open Files` - Open `Find in Files` prompt with open files as targets
- `Find: In Project` - Open `Find in Files` prompt with project files and folder as targets
- `Find: In...` - Open panel to pick directory to open `Find in Files` with as its target
- `Find: Show Results Panel` - Reveals the Find Results panel

![find_in_current_file](https://f.cloud.github.com/assets/902488/279675/aa312f96-9134-11e2-8d9e-bad526b3745a.png)

When you search, the normal `Find in Files` search will be executed with one modification. The `Delete` and `Backspace` key will delete an entire row rather than a single character.

![find_in_files](https://f.cloud.github.com/assets/902488/279676/acdae412-9134-11e2-9c3d-10cdaaa6daff.png)

## License
Copyright (c) 2013 Todd Wolfson

Licensed under the MIT license.
