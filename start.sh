#!/bin/bash

PYTHONDONTWRITEBYTECODE=1 uvicorn --factory src.api.main:create_app --reload --host 0.0.0.0 --port 8000