import os
import time
import webbrowser


def start():

    def startagain():
        print("Please input another search term\s that you would like to search:")
        interm = input()
        if interm == "exit":
            exit()
        
        search(interm)

    def search(term):
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        url = "https://www.google.com/search?q=" + term
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
        startagain()

    print("Please input the search term\s you would like to search:")
    interm = input()
    if interm == "exit":
        exit()
        
    search(interm)

start()

    
    
