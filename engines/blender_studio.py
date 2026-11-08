"""
Blender 5.2 Headless Integration Engine.
Automates 3D meshes, cinematic camera sweeps, and GPU-accelerated rendering via Blender CLI.
"""

from pathlib import Path
from typing import Optional, Union
import subprocess
import os

BLENDER_EXE = r"C:\Program Files\Blender Foundation\Blender 5.2\blender.exe"

class BlenderStudio:
    """Manages headless 3D asset generation and rendering with Blender 5.2."""

    def __init__(self, blender_path: Optional[str] = None):
        self.blender_exe = Path(blender_path or BLENDER_EXE)

    def is_available(self) -> bool:
        return self.blender_exe.exists()

    def generate_gold_coin_scene(self, output_mp4: Union[str, Path], duration_frames: int = 60) -> Path:
        """
        Creates a standalone python script that sets up a 3D rotating gold emblem in Blender and renders it.
        """
        output_mp4 = Path(output_mp4)
        output_mp4.parent.mkdir(parents=True, exist_ok=True)
        
        script = f'''import bpy
import math

# Clear default objects
bpy.ops.wm.read_factory_settings(use_empty=True)

# Add Camera
bpy.ops.object.camera_add(location=(0, -5, 0), rotation=(math.radians(90), 0, 0))
camera = bpy.context.active_object
bpy.context.scene.camera = camera

# Add Golden Cylinder / Coin
bpy.ops.mesh.primitive_cylinder_add(radius=1.2, depth=0.25, location=(0, 0, 0))
coin = bpy.context.active_object

# Create Gold Material
mat = bpy.data.materials.new(name="Gold")
mat.use_nodes = True
nodes = mat.node_tree.nodes
bsdf = nodes.get("Principled BSDF")
if bsdf:
    bsdf.inputs["Base Color"].default_value = (0.85, 0.65, 0.12, 1.0)
    bsdf.inputs["Metallic"].default_value = 0.95
    bsdf.inputs["Roughness"].default_value = 0.15
coin.data.materials.append(mat)

# Animate 360 degree rotation
coin.rotation_euler = (0, 0, 0)
coin.keyframe_insert(data_path="rotation_euler", frame=1)
coin.rotation_euler = (0, math.radians(360), 0)
coin.keyframe_insert(data_path="rotation_euler", frame={duration_frames})

# Add Sunlight
bpy.ops.object.light_add(type='SUN', location=(4, -4, 5))
sun = bpy.context.active_object
sun.data.energy = 3.5

# Scene output settings
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = {duration_frames}
scene.render.fps = 30
scene.render.resolution_x = 1080
scene.render.resolution_y = 1920
scene.render.image_settings.file_format = 'FFMPEG'
scene.render.ffmpeg.format = 'MPEG4'
scene.render.ffmpeg.codec = 'H264'
scene.render.filepath = r"{str(output_mp4).replace('\\', '/')}"

# Render animation
bpy.ops.render.render(animation=True)
'''
        script_file = output_mp4.parent / "temp_blender_coin.py"
        script_file.write_text(script, encoding="utf-8")

        cmd = [
            str(self.blender_exe),
            "-b",
            "-P", str(script_file)
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if script_file.exists():
            script_file.unlink(missing_ok=True)
            
        if res.returncode != 0:
            raise RuntimeError(f"Blender render failed: {res.stderr}")
        return output_mp4
