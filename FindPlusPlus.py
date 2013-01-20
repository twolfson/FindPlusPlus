# import sublime
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
        print "focus gained"
        a = FindResults('hey')
        pass

# TODO: Class for searching options


# Class to handle find results
class FindResults:
    def __init__(self, settings):
        print 'init'
        pass
