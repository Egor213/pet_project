#!/bin/bash

PYTHONDONTWRITEBYTECODE=1 uvicorn --factory src.api.main:create_app --reload --host 127.0.0.1 --port 8000