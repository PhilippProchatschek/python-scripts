# update_all_pip.py
import pkg_resources
import subprocess

print("🔍 Prüfe installierte Pakete...\n")

for dist in pkg_resources.working_set:
    pkg = dist.project_name
    print(f"⬆️  Aktualisiere {pkg} ...")
    subprocess.call(["pip", "install", "--upgrade", pkg])

print("\n✅ Alle Pakete wurden aktualisiert!")
