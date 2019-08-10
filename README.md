# NewClassesSync
## Introduction
Newclasses, the class portal used at New York University powered by [Sakai](https://www.sakailms.org/accessibility), allows file transfer through the WebDAV protocol. This repository contains a script that takes utilizes [Duck CLI](https://duck.sh/) that establishes a WebDAV link in order to automatically download resources from the site.  

## System Prerequisites
•	Duck CLI, install the version for your OS: https://duck.sh
• Python 3, https://www.python.org/downloads/

## How it works
The script derives user input from a provided csv file. It loops through all the classes the user provided info for and downloads resources from the associated newclasses site. In the current configuration, the script will not overwrite a new version of the same file but will always download new files. This can be changed by modifying the script. Check out the Duck CLI documentation [here](https://trac.cyberduck.io/wiki/help/en/howto/cli) If a new version of a file is desired,  rename the current version and rerun the script.

## Running the script
Make sure that the provided template csv is in the same directory as the script. Change the number of classes to sync based on what you want. Replace the netid with yours. Copy and paste the dav sequences from newclasses for each class that you want to sync. You can get this from the resources tab after clicking transfer files. 
![Screenshot](images/davseq.png)
Finally, for each class that you want to sync input the absolute directory that you would like to download and sync the files to.
