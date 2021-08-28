# Setup

First, make sure you have Python 3 and Pip installed. These are the tools you need to run this auto-importer.

You can download them from here if you don't have them: https://www.python.org/downloads/

**IMPORTANT:** When you run the installer **MAKE SURE YOU CHECK THE** `Add Python to PATH` **CHECKBOX AT THE BOTTOM OF THE FIRST WINDOW!**

The installer will install both Python and Pip

Make sure you have this tool unzipped and in a location that you know (desktop, downloads, or documents make it easier)

Open a new PowerShell window (Terminal on Linux/Mac OS) and navigate to the location of this directory using the `cd` (change directory) command. If you have questions, ask in the Telegram.

Once you are in this directory, run `pip3.exe install -r requirements.txt` (remove the `.exe` if on Linux/Mac OS) to install some dependencies. Once this completes you are ready to run the program.

# Config

1. Rename `config.json.example` to `config.json`
2. Open the `config.json` file in some sort of text editor (notepad works best).
3. Fill in all the information that you can for usernames/emails and passwords. If you have session ids that you want to manually input, you can add them to the lists under the section for each website.
    a. For example, if I had some extra Fantia sessions I wanted to use I could add them to the session_ids list like this (this is not common, so only add email/password if you can):
```json
        "fantia": {
            "email": "myemail@email.com",
            "password": "mysecurepassword",
            "session_ids": ["somesession1", "somesession2", "somesession3"],
        }
```
4. For Fanbox, you need to provide your session id instead of your login credentials. Use the same session you would normally use when importing to kemono/seiso.
5. If you want to have the import re-run more (or less) than 1 time 24 hours, change the `run_every_X_hours` config setting to a lower (or higher) number
6. If you do not want the script to attempt imports every 24 hours (or whatever you configured in step 4) then you can disable the `run_forever` mode by setting the config value to 'false'

# Running

There are two options for running this tool:
1. Manually run it and/or keep the tool open forever
2. Set it up as a Windows Task or cronjob so it runs automatically every day without you having to worry
We recommend you use method #2 as it is the most hands-off approach and you don't ever have to worry about it

## How to set up a Windows Scheduled Task
1. Open your `config.json` file and make sure the `run_forever` setting is set to `false`. This is important because the Windows Scheduled Task is going to be the thing running it, so we don't need to have `run_forever` enabled.
1. Locate your Python binary.
    1. Open Command Prompt (not PowerShell) and type `where python.exe` to get a list of known python programs
    1. Locate the line that has some sort of Python3 in the path name (Python3, Python39, Python37, etc.)
    1. Copy the entire path and save it in a notepad somewhere because we will need it
1. Get the path of your auto-import script
    1. Make sure you have unzipped this auto-import script directory and saved it somewhere. You will not be able to move it after this, so make sure it's where you want it to be kept long-term.
    1. Open the directory in your Windows Explorer, click the navigation bar at the top to get the path, and copy the entire thing. Save this path alongside the python one from the previous step.
1. Create a file that will run the auto importer program. This is a simple 2-line file. Create a file called `run_importer.bat`

    1. The file's contents should look like this:

        ```bat
        cd /D "your auto import directory"
        "your python path" import.py
        ```
    
        Replace the stuff in quotes with the paths you saved to your notepad earlier. Don't forget to add the quotes around each of them! Example:
    
        ```bat
        cd /D "C:\Users\MyUser\Documents\auto-importer\"
        "C:\Users\MyUser\AppData\Local\Programs\Python\Python37\python.exe" import.py
        ```
    1. Save the file in your auto-importer directory as `run_importer.bat`

1. Open Task Scheduler in Windows
1. Click `Create Basic Task...` under the Actions panel
    1. Set a name and description that you want
    1. Set the trigger to be daily (and set the time to a time you will be around most days)
    1. Set the action to `Start a program`
    1. Click the `Browse` button when asked for the program/script and select your `run_importer.bat` script that you saved earlier
    1. On the `Finish` step, check the box for  `Open the properties dialog for this task when I click Finish` and click Finish
1. The Properties window should have opened for the new task. Go to the `Settings` tab and check the box that says `Run this task as soon as possible after a scheduled start is missed` (this will run it if your computer was asleep when it was supposed to run)
1. Go back to the General tab in the Properties window and click `Change User or Group`.
    1. Where it says `Enter the object name to select` type `SYSTEM` and click `Check Names` then press `OK`
1. Press `OK` in the Properties window and your task is now successfully set up and it will run once per day

### Veryifying that the script works
1. Open Windows Explorer and navigate to the directory that you have your `run_importer.bat` saved in
1. Right click the .bat file and select `Open`. The program should run and it should begin giving you output as each of your imports begin.
    1. If you see errors or the script immediately exits, try running it again to see if that resolves the issues
    1. If you are still having problems, ask in Telegram for help
Once you have verified that it runs properly, you are good to go! If you ever update your username/password on Fantia, Patreon, or Seiso you will need to update your `config.json` file with the new information or you may run into issues later.

It may also help to refresh your Fanbox session id every few weeks just in case it was invalidated by their system

## How to set up as a cronjob (Linux/Mac OS)

TODO (you can probably figure it out cause it's not complicated like it is on Windows)

## How to run manually

1. Make sure you've configured your config.json file (read the CONFIG section below)
2. Navigate to this directory in PowerShell or Terminal and run `python3.exe import.py` (remove the `.exe` if on Linux/Mac OS) and it will begin running

**IMPORTANT:** If your computer restarts or you close the window running this script, IT WILL STOP RUNNING! After a reboot you need to remember to start this script again.
