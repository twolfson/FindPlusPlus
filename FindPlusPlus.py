import sublime
import sublime_plugin


# DEV: On focus of a window, give me an error message
class FindPlusPlus(sublime_plugin.EventListener):
    def on_activated(self, view):
        sublime.error_message("Hello world!")
