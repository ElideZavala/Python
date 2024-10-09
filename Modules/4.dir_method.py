# --------------------------------------------------------------------------------
# *! The Build-in dir() Method !*

from videos import user_videos

# print(dir(user_videos)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']

print(user_videos.__name__)  # 'videos.user_videos'

print(user_videos.__package__)  # 'videos'

# 'C:\\Users\\User\\Desktop\\Python\\Modules\\videos\\user_videos.py'
print(user_videos.__file__)
