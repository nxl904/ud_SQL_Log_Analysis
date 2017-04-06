import webbrowser
import time

count = 0
while (count <= 3):
    time.sleep(3)
    count += 1
print (webbrowser.open('https://www.youtube.com/watch?v=dDgefxckH7Y'))
print (count)

