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
	print(subprocess.check_output(["git", "--no-pager", "tag", "--sort", "-taggerdate", "--points-at" , "HEAD"]).decode("utf-8"))
	tag = (
		subprocess.check_output(["git", "--no-pager", "tag", "--sort", "-taggerdate", "--points-at" , "HEAD"])
			.split("\n")[0]
			.strip()
			.decode("utf-8")
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
