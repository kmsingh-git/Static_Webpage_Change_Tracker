# websitechangetracker
Track changes in multiple URL's html code (which is a good proxy of real/ meaningful change in the website's content)

This script is meant to be running autonomously, in the background, if you want to track changes in HTML on specified URLs. Note, even the slightest change in the HTML will be conisdered a change, and the recepients will be notified of the changes, including stylistic changes, updates in time/ date on the page and so on.

## Workflow
Basically, after putting in the requisite parameters, just run the script in your terminal or cloud instance or wherever:

python main.py

Note: Running the script will create 2 files for each URL you are tracking. One is the base file containing the HTML at the start of the script. The other is the file containing the HTML at every TIME_INTERVAL run of the comaprehtml() function.

Just ignore these files. You can get rid of those files AFTER you stop the script. If you delete the "base .." file during the running of the script, it will give an error since it won't have a reference to compare the new HTML to.

Finally, some URLs may not like that you're accessing them via scripts. Not sure what happens then.

Enjoy
