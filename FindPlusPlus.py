import sublime
import sublime_plugin


# Class to make Find matching easier
class Finder:
    # TODO: Is this how constructors work in Python?
    def __init__(self, settings):
        # Save settings for later
        # TODO: We might just read directly from settings?
        self.settings = settings

    def find(self, view):
        pass


# DEV: On focus of a window, give me an error message
class FindPlusPlus(sublime_plugin.EventListener):
    def on_activated(self, view):
        # If this is a FindPlusPlus.py
        file_name = view.file_name() or ''
        if file_name.endswith('FindPlusPlus.py'):
            print "focus gained"
            a = FindResults('hey')
            pass


# TODO: Class for searching options


# Class to handle find results
class FindResults:
    def __init__(self, settings):
        # TODO: All actions inside of init should be methods themself?
        # Get the window
        window = self.get_window()

        # Get a panel
        results = window.get_output_panel('FindPPResults')

        # Open the panel
        window.run_command('show_panel', 'output.FindPPResults')

        # Begin editing it
        edit = results.begin_edit()

        # Insert some text
        results.insert(edit, 0, 'hello')

        # Stop editing
        results.end_edit(edit)
        pass

    def get_window(self):
        return sublime.active_window()
