"""
Local Whisper Word-Level Captioning & Forced Alignment Engine.
100% offline speech-to-text using locally installed OpenAI Whisper.
Generates word-level timestamps, kinetic subtitle cards, and keyword highlights.
"""

from pathlib import Path
from typing import List, Dict, Optional, Union
import json
import torch
import whisper

class LocalWhisperCaptioner:
    """
    Offline transcription & word-level captioning.
    Optimized for NVIDIA RTX 2050 (FP16 CUDA) with CPU fallback.
    """

    def __init__(self, model_size: str = "base"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_size = model_size
        self._model = None

    def _ensure_loaded(self):
        if self._model is None:
            # Loads locally cached model weights or downloads to user cache once
            self._model = whisper.load_model(self.model_size, device=self.device)

    def transcribe_with_word_timestamps(self, audio_path: Union[str, Path]) -> Dict:
        """
        Transcribes audio and extracts word-level timestamps.
        Returns full transcript and per-word timestamps {word, start, end}.
        """
        self._ensure_loaded()
        audio_path = str(audio_path)
        
        # Word-level timestamps via Whisper internal attention weights
        result = self._model.transcribe(
            audio_path,
            word_timestamps=True,
            verbose=False
        )

        words_data = []
        for segment in result.get("segments", []):
            for w in segment.get("words", []):
                words_data.append({
                    "word": w.get("word", "").strip(),
                    "start": round(w.get("start", 0.0), 3),
                    "end": round(w.get("end", 0.0), 3),
                    "probability": round(w.get("probability", 1.0), 3)
                })

        return {
            "text": result.get("text", "").strip(),
            "language": result.get("language", "en"),
            "duration": round(result.get("segments", [{}])[-1].get("end", 0.0), 2) if result.get("segments") else 0.0,
            "words": words_data
        }

    def generate_kinetic_srt(self, words_data: List[Dict], max_words_per_card: int = 3) -> str:
        """
        Groups words into punchy short phrases for MeanwhileMayank / Vox style kinetic captions.
        """
        srt_lines = []
        chunk = []
        counter = 1

        for w in words_data:
            chunk.append(w)
            if len(chunk) >= max_words_per_card:
                start_s = chunk[0]["start"]
                end_s = chunk[-1]["end"]
                text = " ".join([c["word"] for c in chunk])

                srt_lines.append(f"{counter}")
                srt_lines.append(f"{self._format_timestamp(start_s)} --> {self._format_timestamp(end_s)}")
                srt_lines.append(text)
                srt_lines.append("")
                counter += 1
                chunk = []

        if chunk:
            start_s = chunk[0]["start"]
            end_s = chunk[-1]["end"]
            text = " ".join([c["word"] for c in chunk])
            srt_lines.append(f"{counter}")
            srt_lines.append(f"{self._format_timestamp(start_s)} --> {self._format_timestamp(end_s)}")
            srt_lines.append(text)
            srt_lines.append("")

        return "\n".join(srt_lines)

    @staticmethod
    def _format_timestamp(seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
