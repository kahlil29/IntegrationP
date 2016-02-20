import sublime, sublime_plugin
import os
import sys

current_working_directory = os.getcwd() 																			#current working directory 
sys.path.append("/home/kahlil/.config/sublime-text-3/Packages/User" + "/lib/python3.4/site-packages")		#Tells sublime python interpreter where modules are store

from git import *	

settings = sublime.load_settings("IntegrationP.sublime-settings")

class myOpener(sublime_plugin.EventListener):		
	global no_of_commits
	no_of_commits = {}
	global directory_is_git_versioned
	directory_is_git_versioned = {}
	global file_path

	def repo_check(self,file_path):																									#code checks for .git in the folder	
			global repo
			global directory_is_git_versioned						
			repo = Repo(file_path,search_parent_directories=True)
			directory_is_git_versioned[file_path]=1

	def push_repo(self):
			  				
			repo = Repo(file_path,search_parent_directories=True)
			o = repo.remotes.origin
			o.pull()	
			o.push()
			sublime.message_dialog("repository pushed")

	def on_load(self,view):
		global file_path
		global directory_is_git_versioned
		global no_of_commits
		file_path = str(view.file_name())
		directory_is_git_versioned[file_path] = 0
		self.repo_check(file_path)
		sublime.message_dialog("File has been opened and it is git versioned")
		no_of_commits[file_path]=0
					
	def on_post_save(self,view):

		global directory_is_git_versioned
		global no_of_commits
		global file_path
		file_path = str(view.file_name())
		
		if directory_is_git_versioned[file_path] == 0 : 
			sublime.message_dialog("File is not git versioned")
		else :
			repo = Repo(file_path,search_parent_directories=True)

			if  file_path in no_of_commits:			
				no_of_commits[file_path] +=1					
			# else:
			# 	no_of_commits[file_path]=1						
				

			sublime.message_dialog("on_post_save")
			sublime.message_dialog(str(repo.git.status()))
			
			sublime.message_dialog(str(repo.git.add(file_path)))
			sublime.message_dialog(str(repo.git.commit( m='committed current file' )))

			sublime.message_dialog(str(repo.git.status()))
	
			sublime.message_dialog(str(no_of_commits[file_path]))
			if no_of_commits[file_path] == settings.get("X_SAVES_Push") :
				no_of_commits[file_path] = 0
				sublime.message_dialog("Push is being called")
				self.push_repo()