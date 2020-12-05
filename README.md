# [Basketball Reference ](https://www.basketball-reference.com/)

## Prject OverView
![](https://i.imgur.com/u2QHEMG.jpg)

This project aims to collect **33892** players' bigraphical information, and award records, providing statistical data for research group at **NTNU** (National Taiwan Normal University).   

## Static Page
Parse plain html to fetch the required data. 
ex. Check whether the player was honored with the Hall of Fame or All Star shown in the blue box.

![](https://i.imgur.com/POrZSE2.png)

## Dynamic Page
Since some personal information isn't revealed on requesting the url, Chromedriver is needed to mock human clicking a button and expand the section and finally get extended pages.

![](https://i.imgur.com/8GhMt9x.png)


## Collet the following information with plain html

1. Whether the player was be admitted into the Hall of Fame
2. The season in which the player was named to All-Star Game rosters
3. The players' personal information such as nation, weight, height, educational background

## Required Package

1. [Chromedriver](http://chromedriver.chromium.org)
version:  2.43.600229

## Python package
1. selenium 3.14.1
2. requests 2.19.1
3. bs4 0.0.1
4. xlrd 1.1.0
