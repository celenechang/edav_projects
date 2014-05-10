## What is this?

This is a repository of projects that were inspired by or started during my Exploratory Data Analysis and Visualization course at Columbia. I enrolled in the class in 2013-2014, during my participation in the [Certification program for Data Science](http://idse.columbia.edu/certification) at the Institue of Data Science.

## What are the projects?

### Grand slams junk chart
This was 3-part iteration (currently I only have the last iteration posted), where I found a junk chart (inspired by [Kaiser Fung](http://junkcharts.typepad.com/‎)) on the internet, designed a better viz representation, coded it in D3, and added more features such as exploratory graphs and filters. The main goals were to 1) use this as an exercise to think about how to best represent obtained data and 2) become familiar with D3. [Final viz [here](http://htmlpreview.github.io/?https://github.com/celenechang/edav_projects/blob/master/GrandSlams_junkchart/grand_slamsGrid.html) and [here](http://htmlpreview.github.io/?https://github.com/celenechang/edav_projects/blob/master/GrandSlams_junkchart/grand_slamsGraphs.html).]

### Datadog
This was my opportunity to use data from my workplace (that is, relevant and yet unexplored data) and see what interesting trends we could detect. I was interested in using support data (such as number of support cases, topics, correlations to revenue or signups) and user data (location, company size, etc.). While I cannot post the full visualization on a public repo, because I haven't figured out how to do that while keeping the data private, I've included the full code and some screenshots. (Stay tuned for updated versions and demos.)

## What dependencies do I need?

### Junk chart
If you clone the repo, everything including the data are self-contained.

### Datadog
Data were extracted from [Desk](http://www.desk.com) and [Intercom](http://www.intercom.io).<br/>
`requests_oauthlib`<br/>
`simplejson`<br/>
`pandas`<br/>
`python-intercom`<br/>
`requests`<br/>
`json`<br/>
`time`<br/>

## Tips

### Run server locally
Use `SimpleHTTPServer` to serve locally:<br/>
`$ python -m SimpleHTTPServer 9999`

### Run Python code to get data in ipython notebook
This saves your workspace so you don't have to run costly functions everytime you get back to your project<br/>
`$ ipython notebook`

