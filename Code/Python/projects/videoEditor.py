from moviepy.editor import *

clip = VideoFileClip("video.mp4")

clip = clip.subclip(0, 10)

# clip = clip.rotate(180)

# clip = clip.volumex(0.5)

clip.ipython_display(width = 280)