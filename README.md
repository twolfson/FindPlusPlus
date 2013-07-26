# Find++

Find code quickly in [Sublime Text][subl].

This was built to allow quick shuffling between search directories. It is useful for projects using multiple repositories to isolate noise in search results.

[npp]: http://notepad-plus-plus.org/
[subl]: http://www.sublimetext.com/

- `Find: In Current File` - Open `Find in Files` with `Where` as the current file
- `Find: In Open Files` - Open `Find in Files` with `Where` as `<open files>`
- `Find: In Project` - Open `Find in Files` with `Where` as `<open files>,<open folders>`
- `Find: In...` - Shows panel to pick directory to open `Find in Files` with as its `Where`
- `Find: Show Results Panel` - Reveals the `Find Results` panel

## Installation
`Find++` is available via [Package Control][pkg-ctrl] and can be found as `Find++`.

[pkg-ctrl]: http://wbond.net/sublime_packages/package_control

For manual installation, run the following script in the Sublime Text 2 terminal (``ctrl+` ``) which utilizes `git clone`.

```python
import os; path=sublime.packages_path(); (os.makedirs(path) if not os.path.exists(path) else None); window.run_command('exec', {'cmd': ['git', 'clone', 'https://github.com/twolfson/sublime-request', 'request'], 'working_dir': path})
```

Packages can be uninstalled via `Package Control: Remove Package`, located in the Command Palette.

## Documentation
All commands are accessible via the Command Palette, `Ctrl + Shift + P` on Windows/Linux, `Command + Shift + P` on Mac.

![command_palette](https://f.cloud.github.com/assets/902488/279674/a552365a-9134-11e2-8c89-603fbb89b606.png)

The `Find: In...` command opens a quick panel with relevant paths and the ability to filter.

![find_in_current_file](https://f.cloud.github.com/assets/902488/279675/aa312f96-9134-11e2-8d9e-bad526b3745a.png)

When you search, the normal `Find in Files` search will be executed with one modification. The `Delete` and `Backspace` key will delete an entire row rather than a single character.

![find_in_files](https://f.cloud.github.com/assets/902488/279676/acdae412-9134-11e2-9c3d-10cdaaa6daff.png)

## Donating
Donations are accepted via [gittip][].

[![Donate on Gittip](http://badgr.co/gittip/twolfson.png)][gittip]

[gittip]: https://www.gittip.com/twolfson/

## Inspiration
As the name of this project suggests, this plugin was started to gain the same `Find` functionality of [Notepad++][npp].

## License
Copyright (c) 2013 Todd Wolfson

Licensed under the MIT license.
