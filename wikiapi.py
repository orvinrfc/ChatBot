import wikipediaapi
import translate as t

# Find a page in wikipedia
# if the page the user's looking for exists, return the page, otherwise return false.
def findPage(wikipedia, string):
    page = wikipedia.page(string)
    if page.exists():
        return page
    else:
        return None

# get the title of the page
def getTitle(page):
    if page is None:
        print("IMDBot: Sorry, the page you are looking for is not in wikipedia")
    else:    
        return page.title

# get the fullURL of the page
def getURL(page):
    if page is None:
        print("IMDBot: Sorry, the page you are looking for is not in wikipedia")
    else:    
        return page.fullurl

# response to the user's request of a certain Actor's name
def respondUserWithWiki(page):
    if page is None:
        print("IMDBot: Sorry, the page you are looking for is not in wikipedia")
    else:
        print("IMDBot: Wikipedia Page of " + page.title)
        print("IMDBot: " + page.summary)
        print('IMDBot: Here\'s the link to the full Wikipedia page' + page.fullurl)

# response to the user's request of a certain Actor's name
def respondUserWithWikiTranslated(page,targetLang):
    if page is None:
        print('IMDBot: ' + t.translate_text("Sorry, the page you are looking for is not in wikipedia", targetLang))
    else:
        print('IMDBot: ' + t.translate_text("Wikipedia Page of :",targetLang)  + page.title)
        print('IMDBot: ' + t.translate_text(str(page.summary),targetLang))
        print('IMDBot: ' + t.translate_text("Here\'s the link to the full Wikipedia page: ",targetLang) + page.fullurl)

# write the whole wikipedia page for the user into a text file
def wikipediaIntoText(page):
    if page is None:
        print("IMDBot: Sorry, the page you are looking for is not in wikipedia")
    else:    
        outFile = open(str(getTitle(page)) + ".txt", "w") # name the file

        text = page.text

        for word in text:
        # write line to output file
            outFile.write(word)

        # close the file    
        outFile.close()

def createWikipedia():
    return wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)   

# -------------- Testing --------------- 
# wikipedia = wikipediaapi.Wikipedia(
#         language='en',
#         extract_format=wikipediaapi.ExtractFormat.WIKI
# )

# page = findPage(wikipedia, "Tom Cruise")
# respondUserWithWiki(page)
# print(getURL(page))
# wikipediaIntoText(page)


# pageFail = findPage(wikipedia,"asdasdasd")
# respondUserWithWiki(pageFail)
# getURL(pageFail)
# wikipediaIntoText(pageFail)
