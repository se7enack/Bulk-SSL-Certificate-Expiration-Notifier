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
<img width="708" alt="this" src="https://gist.github.com/user-attachments/assets/b30cf4ab-306d-4022-91f8-8260181b73a6" />

