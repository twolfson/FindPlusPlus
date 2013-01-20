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
        self.window = window

        # Save name of output panel
        panel_name = 'FindPPResults'
        self.panel_name = panel_name

        # Get a panel
        results = window.get_output_panel(panel_name)
        self.results = results

        # Show the panel
        self.show()

        # Write out some content
        self.write('hello world')
        pass

    def get_window(self):
        return sublime.active_window()

    def output_name(self):
        return 'output.' + self.panel_name

    def show(self):
        # Open the panel
        output_name = self.output_name()
        self.window.run_command('show_panel', {'panel': output_name})

    def hide(self):
        # Hide the panel
        output_name = self.output_name()
        self.window.run_command('hide_panel', {'panel': output_name})

    def write(self, content):
        # Grab the result panel
        results = self.results

        # Begin editing it
        edit = results.begin_edit()

        # Insert some text
        results.insert(edit, 0, content)

        # Stop editing
        results.end_edit(edit)
