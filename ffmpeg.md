# FFMPEG

**Extract a portion of a video:**

`ffmpeg -i [input.mpg] -ss 00:00:30 -t 00:00:05 -vcodec copy -acodec copy [output.mpg]`

- -i: Input file.
- -ss: Start time index of the clip.
- -t: Duration of the clip to extract.

**Extract a subtitle track into an .srt file:**

`ffmpeg -i [video.mkv] -map 0:s:0 [subtitles.srt]`

- -i: Input file.
- -map: Designate one or more input streams as a source for the output file.
- s:0: Specifies a subtitle stream. The number is the subtitle track to use.
