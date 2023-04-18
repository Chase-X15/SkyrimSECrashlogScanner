# SkyrimSE Crashlog Scanner
Just a simple script to parse crash logs produced by the crash logger (https://www.nexusmods.com/skyrimspecialedition/mods/59596) and attempt to identify possible culprits.

# How To Use
_It should be noted that you need python installed to run a python script_
1. Simply place the script in a folder
2. Add any crash logs to that folder (Must be a file named "crash-[date].log" this is the default output from the above mentioned mod)
3. Double click the script and a new *-SCANNED log should populate

# Notes
Please note that what this script identifies may not be the source of your crash. I tried to add in common indicators and call out the more useful information from the crashlog. Just due to the nature of crash logs, the information in the log itself isn't always the most reliable to figure out why you are crashing and I am not an expert.  
Taking note of things like: 
* Can you re-create the crash?
* What were you doing when you crashed?
* What was happening when you crashed?
* Where were you when you crashed?  

Can all potentially point to the culprit better than the crashlog can

I've tried to use information I've found across articles on Nexus Mods and some forums for both Skyrim and Fallout, but it is most certainly not a complete or perfect script.  
Shout out to Poet for their fallout crash log reading document and Fikthenig for their skyrim .net script framework document.  
Shout out to Canberk, Max, and Geeknasty from the Immersive & Adult collection discord for making an amazing modpack and providing me with test logs.
