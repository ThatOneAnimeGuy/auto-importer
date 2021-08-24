# Setup

First, make sure you have Python 3 and Pip installed. These are the tools you need to run this auto-importer.

You can download them from here if you don't have them: https://www.python.org/downloads/

**IMPORTANT:** When you run the installer **MAKE SURE YOU CHECK THE** `Add Python to PATH` **CHECKBOX AT THE BOTTOM OF THE FIRST WINDOW!**

The installer will install both Python and Pip

Make sure you have this tool unzipped and in a location that you know (desktop, downloads, or documents make it easier)

Open a new PowerShell window (Terminal on Linux/Mac OS) and navigate to the location of this directory using the `cd` (change directory) command. If you have questions, ask in the Telegram.

Once you are in this directory, run `pip3.exe install -r requirements.txt` (remove the `.exe` if on Linux/Mac OS) to install some dependencies. Once this completes you are ready to run the program.

# Running

1. Make sure you've configured your config.json file (read the CONFIG section below)
2. Navigate to this directory in PowerShell or Terminal and run `python3.exe import.py` (remove the `.exe` if on Linux/Mac OS) and it will begin running

**IMPORTANT:** If your computer restarts or you close the window running this script, IT WILL STOP RUNNING! After a reboot you need to remember to start this script again.

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
