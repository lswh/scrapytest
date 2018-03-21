import os


#Writes all the URLs in the folder into a list of filenames
dirListing = os.listdir(os.getcwd())


#Initialize list of files
editFiles = []

for item in dirListing:
	if ".html" in item:
		editFiles.append(item)
print editFiles

# Checks for common words DIRECT and RESELLER present on ads.txt file. 
AdsTxtPositive = []

for website in editFiles:
	with open(website) as f:
	   for line in f:
	       if 'DIRECT' in line:
	           print f.name
	           AdsTxtPositive.append(f.name)
	           break
	       elif 'RESELLER' in line:
	           print f.name
	           AdsTxtPositive.append(f.name)
	           break
	   f.close


woohoo = open('000_ADSTEXT POSITIVE DOMAINS.txt', 'w')

for item in AdsTxtPositive:
	woohoo.write("%s\n" %item)

