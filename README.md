## Adding settings.yaml at root for handling token 

```
#settings.yaml

client_config_backend: file
client_config:
    client_id: <your_client_id>
    client_secret: <your_secret>

save_credentials: True
save_credentials_backend: file
save_credentials_file: credentials.json

get_refresh_token: True

oauth_scope:
    - https://www.googleapis.com/auth/drive
    - https://www.googleapis.com/auth/drive.install
```

https://stackoverflow.com/a/48312989


## Changing Folder ID in gdrive_download.py 

folder_id = '<folder_id>'  # folder ID  you can easily get the ID from browser URL


## Start download
```
python gdrive_download.py
```


## troubleshoot

If getting error, try delete credentials.json 
'''oauth2client.client.HttpAccessTokenRefreshError: invalid_grant: Bad Request'''