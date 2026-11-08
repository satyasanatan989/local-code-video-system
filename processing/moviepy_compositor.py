"""
MoviePy & OpenTimelineIO Video Processing & Transition Engine.
Composites video clips, performs crossfades, overlays audio, and manages multi-clip timelines.
"""

from pathlib import Path
from typing import List, Optional, Union
import moviepy as mp

class MoviePyCompositor:
    """Manages programmatic video concatenation, audio mixing, and transitions."""

    @staticmethod
    def concatenate_scenes(
        video_paths: List[Union[str, Path]],
        output_path: Union[str, Path],
        fps: int = 30
    ) -> Path:
        """Concatenates multiple video clips sequentially into a single deliverable."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        clips = [mp.VideoFileClip(str(p)) for p in video_paths]
        final_clip = mp.concatenate_videoclips(clips, method="compose")
        final_clip.write_videofile(
            str(output_path),
            fps=fps,
            codec="libx264",
            audio_codec="aac",
            preset="fast"
        )
        for c in clips:
            c.close()
        final_clip.close()
        return output_path

    @staticmethod
    def mux_audio_track(
        video_path: Union[str, Path],
        audio_path: Union[str, Path],
        output_path: Union[str, Path]
    ) -> Path:
        """Muxes an external audio track onto a video."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        video = mp.VideoFileClip(str(video_path))
        audio = mp.AudioFileClip(str(audio_path))
        
        # Trim audio or video to shortest
        min_duration = min(video.duration, audio.duration)
        video = video.subclipped(0, min_duration)
        audio = audio.subclipped(0, min_duration)
        
        final_video = video.with_audio(audio)
        final_video.write_videofile(
            str(output_path),
            codec="libx264",
            audio_codec="aac",
            preset="fast"
        )
        video.close()
        audio.close()
        final_video.close()
        return output_path
