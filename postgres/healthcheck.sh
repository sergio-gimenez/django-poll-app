#!/bin/bash
POSTGRES_USER=postgres
POSTGRES_DB_NAME=todoapp

pg_isready --username "$POSTGRES_USER" --dbname "$POSTGRES_DB_NAME"
