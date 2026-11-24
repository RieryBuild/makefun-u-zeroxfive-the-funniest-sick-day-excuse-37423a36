import os

LINE = "Can't come in. My Roomba dragged the wifi router into the street and a neighbor's dog is holding it hostage"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
