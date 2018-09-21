# Py-todo
Python(with PyQt5) GUI to-do manager

Hello, bros. This program is simple to-do manager that made by programming beginner.
I found docs or explains about PyQt5 very hard. So, I want to share this short codes for PyQt5 sample.
Some beginners who wants adventure will need it.

I even made .exe file using Pyinstaller, it will be explain soon.

Anyway, my development settings:
Windows 10 edu
Python 3.5.3

1. Open the cmd with administrator privileges.

2.If python3 is registered in your envir path, you can use pip.
write this;

$pip install -r requirements.txt

In my opinion, PyQt5 versions will not problem.

3.download this code.

4.Make a folder wherever you can make. Of course, do not make a folder in a sensitive place!

Now important, attention!

5.You need two kinds of libraries for compile. One is PyQt5 bin pyds. You can find bin folder ~/python/Lib/site-packages/PyQt5/Qt.
 another is api-ms-\*-dlls. It will be in the C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64. Copy all.
 
6.Paste all dlls in your folder. Now almost done. Open cmd on the folder. Of course admin. If you don't know how to move cmd folder, just do google. or youtube.

$pyinstaller --noconsole -p yourfoldername main.py
 
7.Finished! you can attach icon add --icon=icon.ico command. .ico file must in your folder.

now, you can click main.exe. But it will do not work.

main.exe need 'real.db' to work. that db file is sqlite db.

you can use my files. Also, You can make it run sqlmake.py.

Doubleclick sqlmake.py. If anything not happened, run that file on the shell.
'real.db' must in the folder that located main.exe

Thanks.
