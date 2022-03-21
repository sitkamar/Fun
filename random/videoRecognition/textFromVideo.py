import speech_recognition as sr
import moviepy.editor as mp
import moviepy.io.ffmpeg_tools as ffmpeg_tools

num_seconds_videos = 52*60
print("The video is {} seconds long".format(num_seconds_videos))
l = list(range(0, num_seconds_videos + 1, 60))

dlzs = []
for i in range(len(l) - 1):
    ffmpeg_extract_subclip("video.mp4", l[i], l[i + 1], targetname="clip.mp4")
    clip = mp.VideoFileClip("clip.mp4")
    clip.audio.write_audiofile("audio.wav")
    r = sr.Recognizer()
    audio = sr.AudioFile('audio.wav')
    with audio as source:
        r.adjust_for_ambient_noise(source)
        audio_file = r.record(source)
    result = r.recognize_google(audio_file)
    dlzs.append(result)
l_chunks = [dlzs[i:i + 10] for i in range(0, len(dlzs), 10)]
text = "\n".join([" ".join(chunk) for chunk in l_chunks])
with open("text.txt", "w") as f:
    f.write(text)
