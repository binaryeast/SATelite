import webbrowser

url = "https://trello.com/b/C0y0RQFt/sat"
path = """\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" --profile-directory="Profile 3" %s"""

webbrowser.get(path).open(url)