Very basic purely python3 XSS catcher. No need to worry about what field you put your cookie or such in. Just ensure it gets to your box, the script will parse everything out for you.

# Use
```bash
$ ./xss_catcher.py -h
usage: xss_catcher.py [-h] [-ip IP] [-port PORT]

Catch XSS or just record who hits your port.

optional arguments:
  -h, --help  show this help message and exit
  -ip IP      IP Address to listen on (default 0.0.0.0)
  -port PORT  Port to listen on (default 8000)
```

# Structure
Should be self explanatory...

BaseDir/IP_OF_SERVER:PORT/IP_OF_CLIENT/TIMESTAMP_OF_CONNECTION/[GET/Headers/Path]
