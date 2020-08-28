# README.md
This sub-directory containes 3 assignments I have done during the course "Applied Plotting, Charting & Data Representation in Python" by University of Michigan on Coursera.

* 1st File: Assignment3
Aim: Want to draw a interactive bar graph which changes color according to the input y value.


Ferreira, N., Fisher, D., & Konig, A. C. (2014, April). Sample-oriented task-driven visualizations: allowing users to make better, more confident decisions.(https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_Tasks.pdf)       
In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 571-580). ACM.(video) https://www.youtube.com/watch?v=BI7GAs-va-Q

In this paper the authors describe the challenges users face when trying to make judgements about probabilistic data generated through samples. As an example, they look at a bar chart of four years of data (replicated below in Figure 1). Each year has a y-axis value, which is derived from a sample of a larger dataset. For instance, the first value might be the number votes in a given district or riding for 1992, with the average being around 33,000. On top of this is plotted the 95% confidence interval for the mean (see the boxplot lectures for more information, and the yerr parameter of barcharts).


Figure 1
        Figure 1 from (Ferreira et al, 2014).

A challenge that users face is that, for a given y-axis value (e.g. 42,000), it is difficult to know which x-axis values are most likely to be representative, because the confidence levels overlap and their distributions are different (the lengths of the confidence interval bars are unequal). One of the solutions the authors propose for this problem (Figure 2c) is to allow users to indicate the y-axis value of interest (e.g. 42,000) and then draw a horizontal line and color bars based on this value. So bars might be colored red if they are definitely above this value (given the confidence interval), blue if they are definitely below this value, or white if they contain this value.

In this file we implemented this in 3 ways:

First:
Ask the viewer for a y value and plot the color of the bar accordingly

Scond:
User can select any y value by click on y axis and the color will change accordingly

Third:
Viewer can select a range of Y value by clicking on y-axis and color will be change according to the probability of mean of population lie in that range.


* 2nd : UnderstandingDistributionThroughSampling

Creates a number of subplots using the `pyplot subplots` functionality.

Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.


* 3rd: Assinment_2 *

An NOAA dataset has been use for this assignment. 
Note: The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) Daily Global Historical Climatology Network (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.

Each row in the assignment datafile corresponds to a single observation.

The following variables are provided to you:

id : station identification code
date : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
element : indicator of element type
TMAX : Maximum temperature (tenths of degrees C)
TMIN : Minimum temperature (tenths of degrees C)
value : data value for element (tenths of degrees C)

In this assignment:

* This python code returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
* Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
  (Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization).
