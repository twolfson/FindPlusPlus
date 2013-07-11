"""
Shamlessly copied/modified from SublimeQuickFileCreator
https://github.com/noklesta/SublimeQuickFileCreator
"""
import os
import re
import sublime
import sublime_plugin
SETTINGS_KEY = 'FindPlusPlus'


class DirectoryPanelCommand(sublime_plugin.WindowCommand):
    relative_paths = []
    full_torelative_paths = {}
    rel_path_start = 0

    def complete(self):
        # If there ia selected directory, callback with it
        selected_dir = self.selected_dir
        if selected_dir:
            self.cb(selected_dir)

    def open_panel(self, cb):
        # Build out exclude pattern, paths, and save cb
        self.construct_excluded_pattern()
        self.build_relative_paths()
        self.cb = cb

        # If there is only one directory, return early with it
        print 'heeey', self.relative_paths
        if len(self.relative_paths) == 1:
            self.selected_dir = self.relative_paths[0]
            self.selected_dir = self.full_torelative_paths[self.selected_dir]
            self.complete()

        # Otherwise, if there are multiple directories, open a panel to search on
        elif len(self.relative_paths) > 1:
            self.move_current_directory_to_top()
            self.window.show_quick_panel(self.relative_paths, self.dir_selected)

        # Otherwise, attempt to resolve the directory of the current file
        else:
            view = self.window.active_view()
            self.selected_dir = os.path.dirname(view.file_name())
            self.complete()

    def construct_excluded_pattern(self):
        patterns = [pat.replace('|', '\\') for pat in self.get_setting('excluded_dir_patterns')]
        self.excluded = re.compile('|'.join(patterns))

    def get_setting(self, key):
        settings = None
        view = self.window.active_view()

        if view:
            settings = self.window.active_view().settings()

        if settings and settings.has(SETTINGS_KEY) and key in settings.get(SETTINGS_KEY):
            # Get project-specific setting
            results = settings.get(SETTINGS_KEY)[key]
        else:
            # Get user-specific or default setting
            settings = sublime.load_settings('%s.sublime-settings' % SETTINGS_KEY)
            results = settings.get(key)
        return results

    def build_relative_paths(self):
        print 'mah'
        folders = self.window.folders()
        print 'yyy', folders
        self.relative_paths = []
        self.full_torelative_paths = {}
        for path in folders:
            rootfolders = os.path.split(path)[-1]
            self.rel_path_start = len(os.path.split(path)[0]) + 1
            if not self.excluded.search(rootfolders):
                self.full_torelative_paths[rootfolders] = path
                self.relative_paths.append(rootfolders)

            print 'mmm'
            for base, dirs, files in os.walk(path):
                for dir in dirs:
                    relative_path = os.path.join(base, dir)[self.rel_path_start:]
                    if not self.excluded.search(relative_path):
                        print 'zzz'
                        self.full_torelative_paths[relative_path] = os.path.join(base, dir)
                        print 'abc'
                        self.relative_paths.append(relative_path)

    def move_current_directory_to_top(self):
        print 'hai'
        view = self.window.active_view()
        if view and view.file_name():
            cur_dir = os.path.dirname(view.file_name())[self.rel_path_start:]
            if cur_dir in self.full_torelative_paths:
                i = self.relative_paths.index(cur_dir)
                self.relative_paths.insert(0, self.relative_paths.pop(i))
            elif view:
                self.relative_paths.insert(0, os.path.dirname(view.file_name()))
        return

    def dir_selected(self, selected_index):
        if selected_index != -1:
            self.selected_dir = self.relative_paths[selected_index]
            self.selected_dir = self.full_torelative_paths[self.selected_dir]
            self.complete()