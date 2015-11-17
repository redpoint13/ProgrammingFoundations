import time
import webbrowser

breaks = 3
break_count = 0

while break_count < breaks:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=3GwjfUFyY6M")
    break_count = break_count + 1
