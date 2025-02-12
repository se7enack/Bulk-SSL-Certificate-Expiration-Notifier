# Bulk-SSL-Certificate-Expiration-Notifier
Checks a list of domains for existing and upcoming SSL certificate expirations and emails you if they expire within the day threshold you've set. Add to a daily or weekly cronjob for automation.

## Setup:
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

Modify ./stuff.py to add your domains, pending days-left threshold, and email information.


## Usage: 
```./ssl-certificate-expiration-checker.py```

## Example:

<img width="708" alt="Example" src="https://github.com/user-attachments/assets/d8e89bb4-d1dd-41ac-8dc7-01ed2ae3e554" />




   
#### Go(GoLang) Version:
https://gist.github.com/se7enack/047a43f7e3b14a5068e8b224d36c0664
