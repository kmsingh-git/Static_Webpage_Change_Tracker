# websitechangetracker
Track changes in multiple URL's html code (which is a good proxy of real/ meaningful change in the website's content)

This script is meant to be running autonomously, in the background, if you want to track changes in HTML on specified URLs. Note, even the slightest change in the HTML will be conisdered a change, and the recepients will be notified of the changes, including stylistic changes, updates in time/ date on the page and so on.

For continued use, you'll have to restart the script everytime there's a change, otherwise the script will keep finding a change and keep bugging you. Or, if you wanna mess with the code, everytime there is a change, you can choose to sendemails() AND update the basefile with the newfile. This way you only get one email ping for every change, and no more.

This script uses your GMail account to send emails to whomever you want to notify about changes in above mentioned URLs. So before you execute the script, you need to enable "Less secure apps to access this account" option on your GMail account. That is adorably easy and you can find clear instructions on how to do that online.

## Workflow
Basically, after putting in the requisite parameters - URL, SENDER_EMAIL (again, this needs to be a Gmail account), PASSWORD, RECEIVER_ADDRESSES, just run the script in your terminal or cloud instance or wherever (and don't quit it for as long as you want it to track changes, obviously), like so:

python main.py

Note: Running the script will create 2 files for each URL you are tracking. One is the base file containing the HTML at the start of the script. The other is the file containing the HTML at every TIME_INTERVAL run of the comaprehtml() function.

Just ignore these files. You can get rid of those files AFTER you stop the script. If you delete the "base .." file during the running of the script, it will give an error since it won't have a reference to compare the new HTML to.

Finally, some URLs may not like that you're accessing them via scripts. It's your responsibility to check that you're allowed to access those URLs via this script.

Enjoy
