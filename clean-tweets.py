import sys
import re
import json


# Argumen
if len(sys.argv) !=4 :
    print ("\n\nPenggunaan\n\tClean-tweets.py [fileInput.js] [fileOut.js] [labelName]\n")
    sys.exit(1)

data_source = sys.argv[1]
data_output = sys.argv[2]

#read file
file = open(data_source).read()
list_file = file.split("\n")

# Clean string function
def clean_str(text) :
    text = (text.encode('ascii', 'ignore')).decode("utf-8")
    text = re.sub("pic.twitter.com/(.*?)\s", "", text)
    text = re.sub("pic.twitter.com/(.*?)$", "", text)
    text = re.sub("pic.twitter.com/(.*?)\.", "", text)
    text = re.sub("http://(.*?)\s", "", text)
    text = re.sub("https://(.*?)\s", "", text)
    text = re.sub("http://(.*?)$", "", text)
    text = re.sub("https://(.*?)$", "", text)
    text = re.sub("http://(.*?)\.", "", text)
    text = re.sub("https://(.*?)\.", "", text)
    text = re.sub("&.*?;", "", text)
    text = re.sub(">", "", text)    
    text = re.sub("[\]\|\[\@\,\$\%\*\&\\\(\)\":]", "", text)
    text = re.sub("-", " ", text)
    text = re.sub(u"\xc2\xa0/", " ", text)
    # text = re.sub(u"[\u2013\u2018\u2019\u2026]+", " ", text)
    text = re.sub("\.+", "", text)
    text = re.sub("\n+", " ", text)
    text = re.sub("\s+\.", ". ", text)
    text = re.sub("\.\s+", ". ", text)
    text = re.sub("\s+", " ", text)
    text = re.sub("^$", "", text)
    text = re.sub("\.\s$", "", text)
    text = re.sub("^\s+","" ,text)
    return text

with open( data_output, 'w') as outfile:

    for content in list_file :
        
        if content == "" :
            continue

        load_data = json.loads(content)
        clean_content = clean_str(load_data['tweet'])
        data = {
            'date' : load_data['date'],
            'time' : load_data['time'],
            'tweet' : clean_content,
            'label' : sys.argv[3]
        }
        
        json.dump(data, outfile)
        outfile.write("\n")
