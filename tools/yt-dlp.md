# YT-DLP ([README](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#usage-and-options))

## Installation

### Using pip

Make a new directory:
```
mkdir yt-dlp
cd yt-dlp
```

Create an environment:
```
python -m venv env
source env/bin/activate
```

Install with pip:
```
pip install yt-dlp
```

## Usage

Download a video:

```
yt-dlp [video_ID]
```

- Uses highest quality by default

Download a portion of a video:
```
yt-dlp [video ID] --download-sections "*[start_time]-[end_time]"
```

- Time format: `HH:MM:SS`
- Fractional seconds can be given with a decimal point

Download only audio:
```
yt-dlp -x [video ID] --audio-format [audio_format]
```

- Short form `-x` is equivalent to long form `--extract-audio`
- Available audio formats: `aac`, `alac`, `flac`, `m4a`, `mp3`, `opus`, `vorbis`, `wav`
- Default audio format is `opus`
