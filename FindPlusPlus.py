import sublime
import sublime_plugin
from DirectoryPanel import DirectoryPanel

# TODO: Definitely use code from Default/Find in Files.sublime-menu
# We are already using Default/Find Results.hidden-tmLanguage for Default.sublime-keymap insights


# Command to delete a line (used by Find Results)
class FindPlusPlusDeleteLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # DEV: This is blantantly ripped from Packages/Default/Delete Line.sublime-macro

        # Localize view
        view = self.view

        # TODO: If this is a file name we are deleting (e.g. start of a set of results), delete them all

        # Expand selection to line, include line feed, delete lines
        view.run_command("expand_selection", {"to": "line"})
        view.run_command("add_to_kill_ring", {"forward": True})
        view.run_command("left_delete")

# TODO: For full blown implementation, result stacking and double click to fold/unfold

# TODO: Modify output from Find in Files (partial work on this in dev/exploration)

class FppModified(sublime_plugin.EventListener):
    def on_modified(self, view):
        print view, view.name(), view.id(), view.buffer_id()
        print view.visible_region()


# Use SideBarEnhancements' logic for find in current file
# Menu -- https://github.com/titoBouzout/SideBarEnhancements/blob/875fa106af2f4204aecc8827e72edf81e9442e0d/Side%20Bar.sublime-menu#L27
# Command -- https://github.com/titoBouzout/SideBarEnhancements/blob/875fa106af2f4204aecc8827e72edf81e9442e0d/SideBar.py#L243-L255
# class FppFindInPathsCommand(sublime_plugin.WindowCommand):
class FppFindInPathsCommand(DirectoryPanel):
    def open_path(self, path=None):
        if path:
            self.open_paths([path])

    def open_paths(self, paths=[]):
        # Hide the search panel
        window = self.window
        window.run_command('hide_panel')

        # Set up options for the current version
        options = {"panel": "find_in_files", "where": ",".join(paths)}
        if int(sublime.version()) < 2134:
            options['location'] = options['where']
            del options['where']

        # Open the search path
        window.run_command("show_panel", options)


class FppFindInCurrentFileCommand(FppFindInPathsCommand):
    def run(self):
        # Grab the file name
        window = self.window
        file_name = window.active_view().file_name()

        # If there is one, run FppFindInPathsCommand on it
        if file_name:
            self.open_paths(**{'paths': [file_name]})


class FppFindInOpenFilesCommand(FppFindInPathsCommand):
    def run(self):
        self.open_paths(**{'paths': ['<open files>']})


class FppFindInProjectCommand(FppFindInPathsCommand):
    def run(self):
        self.open_paths(**{'paths': ['<open files>', '<open folders>']})


class FppFindInPanelCommand(FppFindInPathsCommand):
    INPUT_PANEL_CAPTION = 'Find in:'

    def run(self):
        # Open a search panel which will open the respective path
        self.open_panel(lambda path: self.open_path(path))

# TODO: Make these settings rather than more commands -- people will only use one or the other (I think)
# TODO: Find in project command (explicit)
# TODO: Find in open files (explicit)
# TODO: Find in pane files?

# TODO: We can overkill it with additive/subtractive file searches -- leave those for another module
# That is, include open file to search -- exclude open file from search