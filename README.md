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
<img width="638" alt="Screen Shot 2025-02-12 at 3 43 11 PM" src="https://github.com/user-attachments/assets/4a7369f0-774b-4f7b-857e-0f45dea8d1f0" />





   
#### Go(GoLang) light Version:
https://gist.github.com/se7enack/047a43f7e3b14a5068e8b224d36c0664
