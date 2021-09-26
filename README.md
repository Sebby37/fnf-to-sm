# FNF/SM converter
This is my fork of a tool that converts FNF charts to .sm files. The original one converted them into 8k/double songs (for both enemy and player notes), whereas this one instead converts them into 4k single charts. 

To run it, run the my-fnf-to-sm.py file and follow the prompts. Sometimes your song may not show up on the list, this is most likely due to the freeplaySonglist.txt file not containing every song in the version of the game you are using. It may also not be able to find the audio files or json files if the file structure is different (like the SiIvapack mod).

Feel free to fork this and add improvements, as most of my code was written late at night when I was tired and may not entirely work.
### Original Description
Roughly convert Friday Night Funkin .json charts to doubles simfiles for StepMania \
Or convert StepMania simfiles to FNF charts. \
Very WIP but it works, kinda.

Usage: Drag-and-drop the FNF .json chart or a StepMania .sm simfile onto `fnf-to-sm.exe` \
Or use the command line: `python fnf-to-sm.py [chart_file]`

For FNF-to-SM, if you input the Normal difficulty .json, and have the \
easy & hard .jsons in the same folder, then FNF-to-SM will output \
a single .sm with all 3 difficulties.

SM-to-FNF currently only supports Challenge Single difficulty. \
The output "blammed.json" is meant to replace "Blammed", Normal difficulty.

Written by shockdude in Python 3.7 \
Original chart-to-sm.js by Paturages \
https://github.com/Paturages/

Project Outfox (active StepMania fork): https://projectmoon.dance/ \
Friday Night Funkin: https://ninja-muffin24.itch.io/funkin
