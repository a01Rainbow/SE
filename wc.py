# wc
#!/usr/bin/python 
#*-*coding:utf8*-* 

def wc (filename, model):
	lengh = len(filename)
	i = 0
	if model == "-l":
		totalline = 0
		while i < lengh:	
			try:
				contents = open(filename[i], 'rb').read()
				s = contents.decode("utf8","ignore")
				linecount = s.count("\n")
			except IOError:
				print ("wc: " + filename[i] + ": No such file or directory")
			else:
				print ("\t" + str(linecount) + "\t" + filename[i])
				totalline = totalline + linecount
			i = i + 1
		if lengh != 1:
			print ("\t" + str(totalline) + "\t" + "total")

	elif model == "-w":
		totalwords = 0
		while i < lengh:	
			try:
				contents = open(filename[i], 'rb').read()
				s = contents.decode("utf8","ignore")
				line = s.replace('\x00','')
				wordcount = len(line.split())
			except IOError:
				print ("wc: " + filename[i] + ": No such file or directory")
			else:
				print ("\t" + str(wordcount) + "\t" + filename[i])
				totalwords = totalwords + wordcount
			i = i + 1
		if lengh != 1:
			print ("\t" + str(totalwords) + "\t" + "total")

	elif model == "-c":
		totalbyte = 0
		while i < lengh:	
			try:
				bytecount = len(open(filename[i], "rb").read())
			except IOError:
				print ("wc: " + filename[i] + ": No such file or directory")
			else:
				print ("\t" + str(bytecount) + "\t" + filename[i])
				totalbyte = totalbyte + bytecount
			i = i + 1
		if lengh != 1:
			print ("\t" + str(totalbyte) + "\t" + "total")

	else:
		totalline = 0
		totalwords = 0
		totalbyte = 0
		while i < lengh:	
			try:
				contents = open(filename[i], 'rb').read()
				s = contents.decode("utf8","ignore")
				linecount = s.count("\n")
				line = s.replace('\x00','')
				bytecount = len(open(filename[i], "rb").read())
				wordcount = len(line.split())
			except IOError:
				print ("wc: " + filename[i] + ": No such file or directory")
			else:
				print ("\t" + str(linecount) + "\t" + str(wordcount) + "\t" + str(bytecount) + "\t" + filename[i])
				totalline = totalline + linecount
				totalwords = totalwords + wordcount
				totalbyte = totalbyte + bytecount
			i = i + 1
		if lengh != 1:
			print ("\t" + str(totalline) + "\t" + str(totalwords) + "\t" + str(totalbyte) + "\t"+ "total")

if __name__ == "__main__":
	import sys
	model = sys.argv[1]
	if model == "-l":
		filename = sys.argv[2:]
		wc (filename, model)
	elif model == "-w":
		filename = sys.argv[2:]
		wc (filename, model)
	elif model == "-c":
		filename = sys.argv[2:]
		wc (filename, model)
	elif model == "--help":
		print ("Usage: wc [OPTION]... [FILE]...")
		print ("  or:  wc [OPTION]... --files0-from=F")
		print ("Print newline, word, and byte counts for each FILE, and a total line if")
		print ("more than one FILE is specified.  With no FILE, or when FILE is -,")
		print ("read standard input.  A word is a non-zero-length sequence of characters")
		print ("delimited by white space.")
		print ("The options below may be used to select which counts are printed, always in")
		print ("the following order: newline, word, character, byte, maximum line length.")
		print ("  -c, --bytes            print the byte counts")
		print ("  -l, --lines            print the newline counts")
		print ("      --files0-from=F    read input from the files specified by")
		print ("                           NUL-terminated names in file F;")
		print ("                           If F is - then read names from standard input")
		print ("  -w, --words            print the word counts")
		print ("      --help     display this help and exit")
	else:
		filename = sys.argv[1:]
		if model[0] == "-":
			if len(model) < 2:
				print ("No such file or directory")
			else:
				print ("We don’t handle that situation yet!")
		else:
			wc (filename, model)
