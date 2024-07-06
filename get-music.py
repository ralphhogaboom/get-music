import os
import subprocess

musicDir = "/home/ralph@hogaboom.org/Nextcloud/development/MusicDownloader"
spotifyURIs = "/home/ralph@hogaboom.org/Nextcloud/development/MusicDownloader/requests.txt"

# cd to folder
os.chdir(musicDir)

# open text file, for each line, download it
with open(spotifyURIs, "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    runline = f'spotdl download {line} --output "{{artists}}/{{album}}/{{title}}.{{ext}}"'
    subprocess.run(runline, shell=True)

# wipe the file and resave it
open(spotifyURIs, "w").close()

