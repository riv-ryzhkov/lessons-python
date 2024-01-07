from moviepy.editor import *

video1 = VideoFileClip("v1.mp4").subclip(3, 5).rotate(180)
video2 = VideoFileClip("v1.mp4").subclip(7, 9)

video_res = concatenate_videoclips([video1, video2])
# video_res = video_res.subclip(3, 5)

video_res.write_videofile('1-2.mp4')


# video2 = VideoFileClip("2.mov").rotate(180)
# video1.ipython_display(width=280)
# video = VideoFileClip("1.mov").subclip(50, 60)

# Make the text. Many more options are available.
# txt_clip = (TextClip("My Holidays 2013", fontsize=70, color='white')
#              .set_position('center')
#              .set_duration(10))

# result = CompositeVideoClip([video, txt_clip])  # Overlay text on video
# result = CompositeVideoClip([video, video])  # Overlay text on video
# result.write_videofile("myHolidays_edited.webm", fps=25)  # Many options...


# =========================================================
# from moviepy.editor import *
#
# video = VideoFileClip("myHolidays.mp4").subclip(50,60)
#
# # Make the text. Many more options are available.
# txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
#              .set_position('center')
#              .set_duration(10) )
#
# result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
# result.write_videofile("myHolidays_edited.webm",fps=25) # Many options...