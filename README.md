           __            _     
 ___  ____/ /____ __  __(_)__ _
/ _ \/ __/ __/ _ `/ |/ / / _ `/
\___/\__/\__/\_,_/|___/_/\_,_/ 
                               
# octavia
> Advanced wrapper for youtube-dl. Makes downloading and converting videa breeze!


[Project summary]

![](screenshot.png)

### Features
- **Feature 1** Copy and paste youtube links and bulk download.
- **Feature 2** Cleans up common junk from video/song titles.

---

### Prerequisities
Python 2
youtube-dl

#### Uses
* 


### Installing
- **Linux:**

Install(or upgrade) youtube-dl
```
$ python octavia.py -U
```

Create a symlink to octavia.py. Places the symlink in your ~/bin folder so it's universally accessible(or should be)

```
$ ./setup.py
```

---

## Usage
```
$ python octavia.py
```
For help: python octavia.py -h

***EXAMPLES:***
> Extract just the mp3 audio and clean the titles.
```
octavia.py -c
```

> Extract just the videos:
```
$ octavia.py -V
```

> Pass in a text file of URL's
```
$ octavia.py -l listofurls.txt
```

---


## Meta
##### Author: Erik Lunna
##### Email -- eslunna@gmail.com

[![](http://img.shields.io/badge/license-WTFPL-blue.svg)]
[WTFPL]: See ``LICENSE`` for full text.
