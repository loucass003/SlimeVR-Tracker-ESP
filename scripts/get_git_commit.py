import subprocess
import os

revision = ""

env_rev = os.environ.get("GIT_REV")
if not env_rev is None and env_rev != "":
    revision = env_rev
else:
    try:
        revision = (
            subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
            .strip()
            .decode("utf-8")
        )
    except Exception:
        revision = "NOT_GIT"

tag = ""
try:
	tag = (
		os.environ.get('RELEASE_VERSION')
	)
	print("tag 0", tag)
	if tag.startswith("v"):
		tag = tag[1:]
except Exception:
	tag = ""

branch = ""
try:
	branch = (
		subprocess.check_output(["git", "symbolic-ref", "--short", "-q", "HEAD"])
			.strip()
			.decode("utf-8")
	)
except Exception:
	branch = ""

output = f"-DGIT_REV='\"{revision}\"'"

print("tag 1", tag)


if tag != "":
	output += f" -DFIRMWARE_VERSION='\"{tag}\"'"
elif branch != "":
	output += f" -DFIRMWARE_VERSION='\"{branch}\"'"
else:
	output += f" -DFIRMWARE_VERSION='\"git-{revision}\"'"

print(output)
