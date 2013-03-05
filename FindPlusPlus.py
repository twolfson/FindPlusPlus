import sublime
import sublime_plugin

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


# Use SideBarEnhancements' logic for find in current file
# Menu -- https://github.com/titoBouzout/SideBarEnhancements/blob/875fa106af2f4204aecc8827e72edf81e9442e0d/Side%20Bar.sublime-menu#L27
# Command -- https://github.com/titoBouzout/SideBarEnhancements/blob/875fa106af2f4204aecc8827e72edf81e9442e0d/SideBar.py#L243-L255
class FppFindInPathsCommand(sublime_plugin.WindowCommand):
    def run(self, paths=[]):
        # Hide the search panel
        self.window.run_command('hide_panel')

        # Set up options for the current version
        options = {"panel": "find_in_files", "where": ",".join(paths)}
        if int(sublime.version()) < 2134:
            options['location'] = options['where']
            del options['where']

        # Open the search path
        self.window.run_command("show_panel", options)

class FppFindInCurrentFileCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Grab the file name
        window = self.window
        file_name = window.active_view().file_name()

        # If there is one, run FppFindInPathsCommand on it
        if file_name:
            window.run_command("find_in_paths", {'paths': [file_name]})

# TODO: Find in project command
# TODO: Find in open files
