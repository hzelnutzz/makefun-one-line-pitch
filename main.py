from pathlib import Path
import os

# Previous pitch: "Got an app idea? Tell make.fun's AI what you'd love it to do, and see your first version come to life—even if you've never coded."
pitch = "Curious what your app idea could look like? Describe it to make.fun's AI for a no-pressure first try—no coding experience needed."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(pitch, encoding="utf-8")
