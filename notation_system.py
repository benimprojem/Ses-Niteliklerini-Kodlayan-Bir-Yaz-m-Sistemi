# Notation system core

from dataclasses import dataclass, field
from typing import List, Optional


VOLUME_MIN = 1
VOLUME_MAX = 7
PITCH_NAMES = [
    "C2", "D2", "E2", "F2", "G2", "A2", "B2",
    "C3", "D3", "E3", "F3", "G3", "A3", "B3",
    "C4", "D4", "E4", "F4", "G4", "A4", "B4",
    "C5", "D5", "E5", "F5", "G5", "A5", "B5",
]


@dataclass
class Segment:
    text: str
    volume: int = 4
    pitch: str = "C4"
    duration_ms: int = 500
    mode: str = "normal"
    extension: int = 0
    silent_lip: bool = False
    free_sustain: bool = False

    def clamp(self):
        self.volume = max(VOLUME_MIN, min(VOLUME_MAX, self.volume))
        self.pitch = self.pitch if self.pitch in PITCH_NAMES else "C4"
        self.duration_ms = max(100, self.duration_ms)

    def render_compact(self) -> str:
        self.clamp()
        mode = self.mode
        suffix = ""
        if self.silent_lip:
            mode = "lip"
        if self.extension > 0:
            suffix += f"[ext={self.extension}]"
        return f"[v={self.volume}][p={self.pitch}][t={self.duration_ms}ms][m={mode}]{suffix}"

    def render_visual(self) -> str:
        self.clamp()
        vol = "|" * self.volume
        pitch_index = PITCH_NAMES.index(self.pitch) if self.pitch in PITCH_NAMES else 14
        pitch_bar = "|" * (min(7, (pitch_index // 4) + 1))
        ext = "" if self.extension == 0 else ("·" * self.extension)
        if self.silent_lip:
            return f"{self.text} [silent-lip] {vol} {pitch_bar} {ext}"
        return f"{self.text} [v={self.volume}] [p={self.pitch}] [t={self.duration_ms}ms] {ext}"


def encode_segment(text: str, volume: int = 4, pitch: str = "C4", duration_ms: int = 500, mode: str = "normal", extension: int = 0, silent_lip: bool = False, free_sustain: bool = False) -> Segment:
    return Segment(
        text=text,
        volume=volume,
        pitch=pitch,
        duration_ms=duration_ms,
        mode=mode,
        extension=extension,
        silent_lip=silent_lip,
        free_sustain=free_sustain,
    )


def render_segment(segment: Segment) -> str:
    return segment.render_compact()


def parse_compact_text(compact: str) -> Segment:
    # minimal parser for simple annotation form: [v=5][p=C4][t=600ms][m=normal]
    values = {}
    for token in compact.split("]"):
        if "[" not in token:
            continue
        inner = token[token.index("[") + 1:]
        if "=" in inner:
            key, val = inner.split("=", 1)
            values[key.strip()] = val.strip()
    volume = int(values.get("v", 4))
    pitch = values.get("p", "C4")
    duration = int(values.get("t", "500").replace("ms", ""))
    mode = values.get("m", "normal")
    extension = int(values.get("ext", 0) or 0)
    return Segment(text="", volume=volume, pitch=pitch, duration_ms=duration, mode=mode, extension=extension)


def build_annotation_line(text: str, volume: int, pitch: str, duration_ms: int, mode: str = "normal", silent_lip: bool = False, extension: int = 0) -> str:
    seg = encode_segment(text, volume=volume, pitch=pitch, duration_ms=duration_ms, mode=mode, extension=extension, silent_lip=silent_lip)
    return f"{seg.render_compact()}"
