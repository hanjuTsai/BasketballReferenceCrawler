# crawler
### The project is tailored for the research group at National Taiwan Normal University. 
### [basketball reference] (https://www.basketball-reference.com)

### info/

##### player_search_list.csv 
players' names

##### player_info_my_df.csv
players' first name, last name

#### info2.xlsx
weight, height, pick, college of players ...

##### all_data3
the pickle file store the list
of 
1. `Whether the player is in Hall of fame` 
2. `The season in which he got the award` 
3. `The season in which he selected as all star`
4. `Whether the player is American`

##### Required
1. [Chromedriver](http://chromedriver.chromium.org)
version:  2.43.600229

##### Python package
1. selenium 3.14.1
2. requests 2.19.1
3. bs4 0.0.1
4. xlrd 1.1.0

##### Jupyter Notebook
1. `crawler` : simulate chromedriver to click the button and download the 'all_per_game' table 
2. `functions` : to collect some information of the players
3. `charcateristic`: weight, height, pick, college of players...
4. `revise`: revise some mistake
