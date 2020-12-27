# mass_upload_data

A program to upload multiple xml files to WOVOdat database automatically 

#what to do before running the code: 
- Install [chromedriver](https://chromedriver.chromium.org/downloads), make sure it is compatible with your Chrome browser's version
- Install selenium by using terminal:
`pip install selenium`
- Change the value of `chromedriver_location` variable to your computer's directory path to webdriver.exe file
- Change the value of `filepath` variable to your computer's directory path to the folder containing xml files that you want to upload
- Edit username and password in `username` and `password` variable

Error that may occur:
![Duplicate data error](https://github.com/hungdp123/mass_upload_data/blob/master/duplicate%20data%20error.png) 

This means there are two events in the xml file with similar NetworkEventCode

Solution:
- Open the xml file with error in your xml editor
- Search for event with NetworkEventCode
- Check the <comments> section of two events, delete the one with earlier update (i.e keep the one with latest update)
 
 For example, these two events have the same NetworkEventCode
 ![Duplicate data solution](https://drive.google.com/file/d/1IStygybUXPNWBY8b8BHjUYbwECQTim_Y/view)
 
 In this case, keep the one with "updated=2018-07-25T01:23:02.395Z" (the one above) because it has the latest updated time.
