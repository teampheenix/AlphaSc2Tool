# AlphaSC2Tool

Alpha SC2 Teamleague: http://alpha.tl/

## General Information

AlphaSC2-Tool is a Python 3.6 script that can load all relevant data from an Alpha SC2 Teamleague match and convert it such that the information can be readily included for streaming, e.g., in OBS-Studio. Moreover, the tool generates corresponding map icons for presentation on your stream, including the map, the players, their races and the score (if played). Additionally, the title of your Twitch stream can be updated accordingly by a single click.

This tool should run on any operating system that supports Python, e.g., Windows, MacOS, and Linux.

## Installation

Download the latest version of Python 3.6 at https://www.python.org/downloads. Download this tool, e.g., via https://github.com/teampheenix/AlphaSC2Tool/archive/master.zip. This tool requires the additional Python Packages *PyQt5*, *requests*, and *configparser*. To install these packages run the script *downloadLibaries.py* once or do it manually. Run *AlphaSC2Tool.pyw* to start the AlphaSC2-Tool.

## Instructions for Use

Run *AlphaSC2Tool.pyw* to start the AlphaSC2-Tool. Enter the Match-ID or URL of an Alpha SC2 Teamleague match, e.g., "http://alpha.tl/match/2392" or "2392". Press *Load Data from URL* and edit the data if necessary. The sliders control the score of each map. Press "Update OBS Data" or alter the score to update the data for streaming, which can be found in the directory *OBS_data*. If you want to include the team logos and the matchbanner it is recommended to include them as browser source via the html files given in the directory *OBS_html*. The map icons can be found in the directory *OBS_mapicons* and may be included in your stream as browser source.

To update your Twitch title via click on *Update Twitch Title* you have to set your *channel*, *clientid*, and *oauth* in the *data.ini* file that can be edited with any text editor. For instructions how to obtain these, see **Twitch Integration** below. The template for the title can be customized in config file *data.ini*.

The top slider is to select *your* team. Once selected the border of the map icons turn green or red depending on your result. To select your team my default you can set the parameter *myteam* in *data.ini*.

## Customization

Some basic options for customization can be found in *data.ini*. For additional customization of the map icons you can alter the *\OBS_mapicons\src\map.css* file, e.g., try to replace *map.css* with *map_alternative.css*.

## Help & Contribution

If you need help, have bugs to report or want to contribute to this project go to #dev channel of the Alpha SC2 Discord Server https://discordapp.com/invite/yRWNYr and/or message me Discord *pres.sure#5247*.

## Support

If you want to support this project, consider subscribing to https://www.twitch.tv/teampheenix.

## Twitch Integration

To update your Twitch title via click on *Update Twitch Title* you have to set your *channel*, *clientid*, and *oauth* in the *data.ini* file that can be edited with any text editor. *channel* is the name of your channel, e.g., 
*teampheenix* for https://www.twitch.tv/teampheenix.

### Creating a twitch application which the script can access to update the title
* Go to https://www.twitch.tv/settings/connections
* Scroll down and click "Register your application"
* App Name: enter any unique name like "AlphaSC2Tool"
* Use this Redirect URI: http://localhost
* App category: Game Integration -> hit "Register"
* Look for the "Client ID" on that website and save it. This is the parameter *clientid* you need to enter in *data.ini* file.

### Getting the token from the twitch application
* Replace the "INSERT_CLIENT_ID" in the following link with the "Client ID" from the last step, and then open it in your browser https://api.twitch.tv/kraken/oauth2/authorize?response_type=token&client_id=INSERT_CLIENT_ID&redirect_uri=http://localhost&scope=channel_editor
* So it should look something like this https://api.twitch.tv/kraken/oauth2/authorize?response_type=token&client_id=l3jijexx69n17s56a8s1ddv8x5j5nsm&redirect_uri=http://localhost&scope=channel_editor
* Click "Authorize"
* Now you get redirected to a blank website with some similar URL like http://localhost/#access_token=k9y42hj9df8fg73vd3zpsop7erbsp32jco1t&scope=channel_editor
* Copy that token (key) from the URL between "access_token=" and "&scope=channel_editor" and save it for the next step. This is the parameter *oauth* you need to enter in *data.ini* file.
