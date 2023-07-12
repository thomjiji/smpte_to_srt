import sys


def smpte_to_milliseconds(smpte: str, frame_rate: float):
    hh, mm, ss, frame = map(int, smpte.split(":"))
    milliseconds = int(
        (hh * 3600 + mm * 60 + ss) * 1000 + frame * 1000 / frame_rate
    )
    return f"{hh:02d}:{mm:02d}:{ss:02d}.{milliseconds % 1000:03d}"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: smpte_to_milliseconds.py <SMPTE timecode> <frame rate>")
        sys.exit(1)

    smpte = sys.argv[1]
    frame_rate = float(sys.argv[2])

    result = smpte_to_milliseconds(smpte, frame_rate)
    print(result)
