import re
import sys


def smpte_to_srt(smpte, frame_rate):
    # Validate and parse SMPTE
    match = re.match(r"^(\d{2}):(\d{2}):(\d{2}):(\d{2})$", smpte)
    if not match:
        raise ValueError("Invalid SMPTE format")

    hours, minutes, seconds, frames = match.groups()
    hours, minutes, seconds, frames = (
        int(hours),
        int(minutes),
        int(seconds),
        int(frames),
    )

    # Convert to milliseconds
    milliseconds = round(frames / frame_rate * 1000)

    # Construct SRT format
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"


def srt_to_smpte(srt, frame_rate):
    # Validate and parse SRT
    match = re.match(r"^(\d{2}):(\d{2}):(\d{2}).(\d{3})$", srt)
    if not match:
        raise ValueError("Invalid SRT format")

    hours, minutes, seconds, milliseconds = match.groups()
    hours, minutes, seconds, milliseconds = (
        int(hours),
        int(minutes),
        int(seconds),
        int(milliseconds),
    )

    # Calculate frame count
    frames = round(milliseconds / 1000 * frame_rate)

    # Construct SMPTE
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{frames:02d}"


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Not enough arguments")
        print("Usage: convert.py <SMPTE/SRT> <timecode> <frame rate>")
        sys.exit(1)

    direction = sys.argv[1]
    timecode = sys.argv[2]
    frame_rate = float(sys.argv[3])

    if direction.lower() == "smpte":
        print(smpte_to_srt(timecode, frame_rate))
    elif direction.lower() == "srt":
        print(srt_to_smpte(timecode, frame_rate))
    else:
        print("Invalid direction. Must be SMPTE or SRT.")
