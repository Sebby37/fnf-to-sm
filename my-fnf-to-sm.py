# Imports
from os import system, mkdir, remove, path
from pydub import AudioSegment
from shutil import copy

# Initialisation
game_dir = input("Input the path to your FNF EXE of choice: ")#"C:\\Users\\Seb C\\Documents\\Gamez\\Friday Night Funkin\\funkin - Kapi\\bin" #input("Input the path to your FNF EXE of choice: ")
songs = [line.strip().split(":")[0] for line in open(game_dir + "\\assets\\data\\freeplaySonglist.txt").readlines()]

# Getting the song the user wants to convert
chosen_song = ""
if True:#while chosen_song not in songs:
    print("Avaliable songs:\n" + "\n".join(songs))
    chosen_song = input("Choose a song from the list above you want to convert: ")

if not path.exists(game_dir + "\\assets\\songs\\" + chosen_song):
    chosen_song = chosen_song.replace(" ", "-")

print("""\nAvailable conversion types:
1: Only Enemy
2: Only BF
3: Merge both (May not completely work)""")
conversion = input("Choose a conversion type from above: ")[0]

# Running the normal converter
system(f'fnf-to-sm.exe "{game_dir + "/assets/data/" + chosen_song.lower() + "/" + chosen_song.lower() + ".json"}"')
print("Conversion complete!")

# Combining the voice and background sound files
print("Creating ogg file...")

inst = AudioSegment.from_ogg(game_dir + "\\assets\\songs\\" + chosen_song + "\\Inst.ogg")
voices = AudioSegment.from_ogg(game_dir + "\\assets\\songs\\" + chosen_song + "\\Voices.ogg")

combined_song = inst.overlay(voices)
combined_song.export(chosen_song + ".ogg", format="ogg").close()

print("Ogg file created!")

# Converting the doubles to singles
def chstr(string: str, char: str):
    return sum(chr == char for chr in string)

print("Converting doubles charts to singles charts...")
simfile = open(chosen_song + ".sm", "r").readlines()

for i, line in enumerate(simfile):
    if "dance-double" in line:
        simfile[i] = line.replace("dance-double", "dance-single")
    if len(line.strip()) == 8 and ("1" in line or "0" in line or "2" in line or "3" in line):
        if conversion == "1":
            # Strip out last 4 chars
            simfile[i] = line[0:4]
        elif conversion == "2":
            # Strip out first 4 chars
            simfile[i] = line[4:8]
        else:
            # Merge the first four and last four chars
            enemy = line[0:4]  # Player 1 (enemy)
            bf = line[4:8]  # Player 2 (BF)

            # If there are no notes on one side, we simply choose the side with notes
            if enemy == "0000":
                simfile[i] = bf + "\n"
                continue
            elif bf == "0000":
                simfile[i] = enemy + "\n"
                continue

            # Intelligent code that compares the enemy and bf side, with it picking the side with more notes (maybe later if I feel like it)
            if chstr(enemy, "0") > chstr(bf, "0"):  # If there are more 0s in the enemy's side than the players, we choose the player's side
                simfile[i] = bf + "\n"
            elif chstr(enemy, "0") < chstr(bf, "0"): # Like the above but for the player instead
                simfile[i] = enemy + "\n"
            else:  # If they are equal (or any other type I guess) then we choose the bf's side so the player knows what they are playing
                simfile[i] = bf + "\n"

output_file = open(chosen_song + ".sm", "w")
output_file.truncate(0)
output_file.writelines(simfile)
output_file.close()
print("Conversion complete!")

# Moving the files to their own directory
print("Moving files to new directory...")
try:
    mkdir(chosen_song)
except:
    pass
copy(chosen_song + ".sm", chosen_song) #rename(chosen_song + ".sm", chosen_song + "\\" + chosen_song + ".sm")
copy(chosen_song + ".ogg", chosen_song) #rename(chosen_song + ".ogg", chosen_song + "\\" + chosen_song + ".ogg")
try:
    remove(chosen_song + ".sm")
    remove(chosen_song + ".ogg")
except Exception as e:
    print("Error deleting files: " + str(e))
print("Move complete!")

system("pause")