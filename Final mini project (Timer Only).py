
import sublime, sublime_plugin
import os
import sys

current_working_directory = os.getcwd() 																			#current working directory 
sys.path.append("/home/kahlil/.config/sublime-text-3/Packages/User" + "/lib/python3.4/site-packages")		#Tells sublime python interpreter where modules are store

from git import *	



settings = sublime.load_settings("IntegrationP.sublime-settings")




#some global variables																													#imports all from module git, because exceptions file needs to be imported
#counter123 = 0

counter = 1
#repo = Repo(settings.get("REPO_PATH"))

# class UserinputCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
# 		#temp_dir = "/home/kahlil/TestingGit"
# 		#join = os.path.join
# 		#sublime.message_dialog("control is here")
# 		sublime.message_dialog(str(settings.get("X_SAVES_Push")))
# # 		self.view.window().show_input_panel("Push after number of commits", "Enter number here", self.on_done, None, None)																										#creates a git.Repo object to represent your repository.
		

# # 	def on_done(self, user_input):
# # 		sublime.message_dialog("Push after "+ X_SAVES_Push + " commits")
# # 		global commit_before_push
# # 		commit_before_push = int(user_input)


# class GitfunctionsCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
		
# 		#join = os.path.join																											#creates a git.Repo object to represent your repository.
		

class myOpener(sublime_plugin.EventListener):		
	global list_of_files
	list_of_files = {}

	def on_post_save(self,view):


		temp_dir = str(view.file_name())

		def repo_check(temp_dir):																									#code checks for .git in the folder	
			try :		
				global repo								
				repo = Repo(temp_dir,search_parent_directories=True)
				#self.view.insert(edit, 0, str(repo))
			except InvalidGitRepositoryError :																			#exception handled when .git is not found
					# forwd_slash_index = temp_dir.rfind('/', 0, len(temp_dir))   				#finds index of last forward slash

					#self.view.insert(edit, 0, str(forwd_slash_index))
					
					# temp_dir = temp_dir[0:forwd_slash_index]														#goes up one file level
					
					#self.view.insert(edit, 0, temp_dir)
					
					# if forwd_slash_index == 0 :																					#if file not versioned by git
					# 	sublime.message_dialog("No git repo found")
					global counter
					counter = 0
						
					# else :																															#recursive call to repo_check with upper file level
					# 	repo_check(temp_dir)



		repo_check(temp_dir)													#function call to repo_check
		

		global counter
		if counter == 1:
			global repo

			#Below is the code that checks if the file has been committed, if yes, checks the number of times and accordingly modifies the counter
			
			if  temp_dir in list_of_files:			
				list_of_files[temp_dir] +=1					#If it is already in dictionary, increment and then commit
				
			else:
				list_of_files[temp_dir]=1						#Else add to dictionary with value 1
				sublime.message_dialog("Just added new entry to the dictionary")

			sublime.message_dialog("on_post_save")
			sublime.message_dialog(str(repo.git.status()))
			#sublime.message_dialog("You have saved the file")

			sublime.message_dialog(str(repo.git.add(temp_dir)))
			sublime.message_dialog(str(repo.git.commit( m='committed current file' )))

			#sublime.message_dialog("and now it has been committed")
			sublime.message_dialog(str(repo.git.status()))

			def push_repo():
				forwd_slash_index = temp_dir.rfind('/', 0, len(temp_dir))   				#finds index of last forward slash
				new_dir = temp_dir[0:forwd_slash_index]
				repo = Repo(new_dir)
				o = repo.remotes.origin
				o.pull()	
				o.push()
				#asdadsas
				#asdaasddsasdsfsfASDSFDS
				#sublime.message_dialog(new_dir)
				sublime.message_dialog("repository pushed")

			# global counter123
			# counter123 += 1 
			#sublime.message_dialog(str(list_of_files[temp_dir]))

			#sublime.message_dialog(str(list_of_files.keys()))
			if list_of_files[temp_dir] == settings.get("X_SAVES_Push") :
				list_of_files[temp_dir] = 0
				push_repo()
				

		


		
		#sublime.set_timeout(on_post_save, Y_SECONDS_COMMIT * 1000)

