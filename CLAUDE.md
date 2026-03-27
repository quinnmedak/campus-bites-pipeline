# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

A local PostgreSQL database for analyzing Campus Bites food order data. The goal is to run SQL queries against order data stored in `data/campus_bites_orders.csv`.

## Database Commands

```bash
# Start the database (background)
docker compose up -d

# Stop the database
docker compose down

# Full reset — wipes all data and reloads from scratch
docker compose down -v && docker compose up -d
```

Connect via DBeaver or any SQL client at `localhost:5432`, database `campus_bites`, user/password `postgres`.

## Setup Flow

```bash
docker compose up -d   # start the database
python load_data.py    # create the orders table and load the CSV
```

`load_data.py` uses `pandas` + `psycopg2` to create the `orders` table (if it doesn't exist) and bulk-insert all rows from the CSV. Safe to re-run — uses `ON CONFLICT (order_id) DO NOTHING`.

## Data

Single table: `orders` — 1,132 rows of food delivery orders with columns for date, time, customer segment (`Greek Life`, `Grad Student`, `Off-Campus`, `Dorm`), order value, cuisine type, delivery time, promo code usage, and reorder flag. Data spans 2025-07 through 2026-06.
