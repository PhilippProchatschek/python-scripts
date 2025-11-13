# update all packages who are listed after the command: pip list --outdated
import pkg_resources
import subprocess

print("Check of installed packages\n")

for dist in pkg_resources.working_set:
    pkg = dist.project_name
    print(f"Update {pkg} ...")
    subprocess.call(["pip", "install", "--upgrade", pkg])

print("\n✅ All packages are installed!")
