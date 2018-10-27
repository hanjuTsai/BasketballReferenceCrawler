# crawler
### This repo is to crawl the information of all player in [basketball reference](https://www.basketball-reference.com)

### info/

##### player_search_list.csv 
all the name and year players play

##### player_info_my_df.csv
all the firstName, LastName, url of players 

#### info2.xlsx
weight, height, pick, college of players ...

##### all_data3
the pickle file store the list
of 
1. `Whether the player is in Hall of fame` 
2. `The season in which he got the award` 
3. `The season in which he selected as all star`
4. `Whether the player is American`


##### FinalVersion.xlsx
The info mentioned above gathered for each season each player

##### Required
1. Chromedriver

##### Python package
1. Selenium
2. requests
3. bs4

##### Jupyter Notebook
1. `crawler` : simulate chromedriver to click the button and download the 'all_per_game' table 
2. `functions` : to collect some information of the players
3. `charcateristic`: weight, height, pick, college of players...
4. `revise`: revise some mistake
