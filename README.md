This is for Monitoring and Observability Implementation repo.

app: It has yaml files to deploy our application on kubernetes.

backend application: It has backend application with Jaeger tracer code.

frontend application: It has frontend application with Jaeger tracer code.

service monitor files: It has serviceMonitor files to monitor(get info related cpu usage or metrics) application in prometheus.

===========================================================================================================================
Task to complete file has some doubt which I described here please suggess me this as well:
------------------------------------------------------------------------------------------------------------------
## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.
-->  for this I have add some handler in python code but not getting in prometheus. Please help me to understand
_____________________________________________________________________________________________________________________________


## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.
--> for this I add the screenshot 'jaeger metrics' please check once . is it correct or need anything else

______________________________________________________________________________________________________________________________

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.
======================================
this has some doubt in correct answer :
======================================
TROUBLE TICKET

Name: Getting response from endpoint

Date: 05-01-2023

Subject: Exploring one error with Jaeger Tracer

Affected Area: In Jaeger trecable application , there is one endpoint ('/star') has problem related to 'POST' methods.

Severity: The defect has moderate priority because we are unable to achieve desired response and unable to implement it successfully.(screenshot: error detail)

Description: We are unable to trace this function with 'POST' methods and If we change this 'POST' method to 'GET' then we have error in this code but now Jaeger is able to trace it and give the logs of error(screenshot: error detail). 
________________________________________________________________________________________________________________________________________

These tasks also has some problem in understand: 
=================================
## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.
________________________________________
---> please suggess some code type hint
________________________________________

_________________________________________________________________________________________________________________________________________

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

__________________________________________________________________________________________________________________________________________

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  



