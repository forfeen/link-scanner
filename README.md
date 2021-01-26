## Link Scanner Application

A Python program that scans a web page for hyperlinks.  It prints all the hyperlinks found on a page and then prints (again) any bad links.

## Prerequisite
- Python 3.7 or newer
- Selenium with Python
- ChromeDriver

Usage:
```
python3 link_scan.py  url-to-scan
```

Example:
```
cmd> python3 link_scan.py https://brew.sh/

https://brew.sh/
https://docs.brew.sh/Installation
https://formulae.brew.sh/formula/
...
https://exomel.com/
https://mikemcquaid.com/
https://cargocollective.com/danilalo


Bad Links:
https://mxcl.github.io/
```
