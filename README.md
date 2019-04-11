# Web Scraper 
---
version: 0.0.1
method: GET
---
## Parameters:
## Query string:
* **url** *(str)* :from which website you want text and images
* **directory** *(str)*: new folder where you download images and
* **path** *(str)*: choose path where you want to save text and 

## Example on localhost to return data on screen only url parametr needed
```
curl "http://localhost:5000/taker?url=https://realpython.com/read-write-files-python/"
```
## Example on localhost to save images and text
```
curl "http://localhost:5000/taker/save?url=https://realpython.com/read-write-files-python/&directory=realpython1&path=C:/Users/piotr.rybinski.1/obrazy_z_internet/"
```
## Build
Always remeber to be on the micro_for_text directory! Otherwise it won't work.

### Windows:
```
docker build -f .\Dockerfile -t web_scrap:0.0.1 .
```
## Run

### Windows:
```
docker run -it -p 5000-6000:5000 web_scrap:0.0.1

```
