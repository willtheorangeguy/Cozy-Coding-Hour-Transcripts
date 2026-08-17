# Cozy Coding Hour Transcripts — Pipeline

The archive is built by 6 scripts run in numeric order. `main.py` is a thin runner that calls each one in turn with the arguments you gave it, so running a stage by hand and letting `main.py` do it are equivalent.

| Stage | Script | What it does | Resume log |
|---|---|---|---|
| 1 | `1_download.py` | This script uses yt-dlp to download videos, by year, from the Cozy Coding Hour podcast. | — |
| 2 | `2_converter.py` | This script converts all video files in a specified folder to audio files using ffmpeg. | `converted.log` |
| 3 | `3_tagger.py` | This script processes MP3 files, and matches their titles to the YouTube playlist metadata for the Cozy Coding Hour podcast. It updates the tags of the MP3 files with artist, album, title, track number. | `tagged.log` |
| 4 | `4_transcriber.py` | This script transcribes audio files from the Cozy Coding Hour episodes using OpenAI's Whisper model. | `transcribed.log` |
| 5 | `5_summarizer.py` | This script summarizes a transcript file by splitting it into manageable chunks, summarizing each chunk using the Ollama API, and then combining the summaries into a final summary. | `summarized.log` |
| 6 | `6_cleanup.py` | This script processes all .txt and .md files in the current directory, correcting their grammar and spelling using LanguageTool. | `cleaned.log` |

## Running a single stage

Every stage takes the same arguments as `main.py`, so any one of them can be re-run on its own without repeating the stages before it:

```bash
python 1_download.py <year>
```

## Re-running and resume logs

The expensive stages append to a log file as they finish each item, and skip anything already listed there on a later run. That is what makes the pipeline resumable after an interruption.

| Log | Written by |
|---|---|
| `converted.log` | `2_converter.py` |
| `tagged.log` | `3_tagger.py` |
| `transcribed.log` | `4_transcriber.py` |
| `summarized.log` | `5_summarizer.py` |
| `cleaned.log` | `6_cleanup.py` |

Delete a log to force its stage to redo everything.

## A note on accuracy

Transcription and summarisation are both lossy. Neither the transcripts nor the summaries in this repository are an authoritative record — check the original recording where it matters. See [`CONTENT_LICENSE.md`](../CONTENT_LICENSE.md).
