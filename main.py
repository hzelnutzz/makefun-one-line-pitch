from pathlib import Path
import os

# Runner-ups:
# "Got an app idea? Tell make.fun's AI what you'd love it to do, and see your first version come to life—even if you've never coded."
# "You bring the app idea, make.fun's AI helps build it: a friendly first step from 'what if?' to something you can try."
pitch = "Got an app idea? Tell make.fun's AI what you'd love it to do, and see your first version come to life—even if you've never coded."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(pitch, encoding="utf-8")
