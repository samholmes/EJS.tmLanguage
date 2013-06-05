import sublime, sublime_plugin

class EjsQmarksCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.set_syntax_file("Packages/EJS/EJS_alternative.tmLanguage")

class EjsPercentsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.set_syntax_file("Packages/EJS/EJS_default.tmLanguage")