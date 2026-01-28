# FFMPEG ([docs](https://ffmpeg.org/documentation.html))

Extract a portion of a video:
```
ffmpeg -i [input_file] -ss [start_time] -to [end-time] [output_file]
```

- `-i` identifies the input file.
- `-ss` specifies the start time of the clip.
- `-to` specifies the end time of the clip.
- `-t` can be used in place of `-to` to specify duration instead of end time.

---

Extract a subtitle track into an .srt file:
```
ffmpeg -i [input_file] -map 0:s:0 [subtitle_file]
```

- `-i` identifies the input file.
- `-map` designates one or more input streams as a source for the output file.
- `s:0:n` Specifies a subtitle stream. The variable `n` is the subtitle track to use.

---

Create a video from an audio file and an image:
```
ffmpeg -r 1 -loop 1 -i [image.jpg] -i [audio.mp3] -acodec copy -shortest [output.mp4]
```

- `-i` identifes the image file and the audio file.
- `-r` indicates the frame rate.
- `-acodec`: force audio codec. Copy indicates that it should be copied as is.
- `-shortest`: finish encoding when shortest input stream ends.
- Be aware that the order of the arguments matters.
