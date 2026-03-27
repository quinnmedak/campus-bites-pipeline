# Campus Bites Pipeline

Local PostgreSQL database for analyzing Campus Bites order data.

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Setup

```bash
docker compose up -d
```

That's it. On first run, Docker will:
1. Start a PostgreSQL 16 container
2. Create the `campus_bites` database
3. Create the `orders` table
4. Load all rows from `campus_bites_orders.csv`

## Connect with DBeaver

| Field    | Value          |
|----------|----------------|
| Host     | localhost      |
| Port     | 5432           |
| Database | campus_bites   |
| Username | postgres       |
| Password | postgres       |

## Table: `orders`

| Column             | Type           |
|--------------------|----------------|
| order_id           | INTEGER (PK)   |
| order_date         | DATE           |
| order_time         | TIME           |
| customer_segment   | TEXT           |
| order_value        | NUMERIC(8,2)   |
| cuisine_type       | TEXT           |
| delivery_time_mins | INTEGER        |
| promo_code_used    | TEXT           |
| is_reorder         | TEXT           |

## Common Commands

```bash
# Start the database
docker compose up -d

# Stop the database
docker compose down

# Stop and delete all data (full reset)
docker compose down -v
```

## Reset / Reload Data

If you need to reload the CSV from scratch:

```bash
docker compose down -v
docker compose up -d
```
