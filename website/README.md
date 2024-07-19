# Manage users in Dango

Following tutorial from https://www.youtube.com/watch?v=WuyKxdLcw3w

Learning how to implement authentication & authorisation  the Django way.

## Run DB

IN order to start from a clean DB, make sure bind mount is removed and start db:

```bash
sudo rm -rf ./db-data && docker compose up --force-recreate
```