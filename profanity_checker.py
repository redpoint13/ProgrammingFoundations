import urllib

def main():
	read_text()

def read_text():
	quotes = open("C:\Users\Tony\Documents\GitHub\ProgrammingFoundations\movie_quotes.txt")
	contents_of_file = quotes.read()
	quotes.close
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
	output = connection.read()
	connection.close
	if "true" in output:
		print("Profanity ALERT!!!")
	elif "false" in output:
		print("This document has no profanity.")
	else:
		print("Could not read the file properly.")


main()
