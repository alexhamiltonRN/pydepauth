import yaml 
import tomllib 
import tomli_w 
from pathlib import Path 

deps_file = Path("env/deps.yaml")
req_file = Path("env/requirements.in")

# convert YAML -> requirements.in
if deps_file.exists():
    data = yaml.safe_load(deps_file.read_text())
    req_file.write_text("\n".join(data.get("dependencies", [])))

# inject into pyproject
with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

deps = [line.strip() for line in req_file.read_text().splitlines() if line.strip()]
config["project"]["dependencies"] = deps

with open("pyproject.toml", "wb") as f: 
    tomli_w.dump(config, f)
