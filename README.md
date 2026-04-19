# Commodities Pipeline

A real-time data pipeline for commodity price tracking, built to demonstrate production-grade data engineering patterns.

## What it does

Tracks simulated live prices for WTI Oil, Copper, Wheat, and Gold. Prices are generated every second, stored in Redis, and served via a REST API with statistical processing.

## Architecture

Price Simulator -> Redis -> FastAPI

## Tech Stack

- **Python** — core language
- **FastAPI** — REST API framework
- **Redis** — time-series price storage
- **Docker** — containerization

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /price/{commodity}` | Latest price |
| `GET /average/{commodity}?window=10` | Moving average (configurable window) |
| `GET /stats/{commodity}` | Full stats: min, max, average, count |

## Running locally

**Prerequisites:** Docker Desktop, Python 3.12+

```bash
# Start the API and Redis
docker-compose up --build

# In a second terminal, start the price simulator
python -m simulator.price_simulator
```

API docs available at `http://localhost:8000/docs`

## Commodities supported

`WTI_OIL` `COPPER` `WHEAT` `GOLD`

## Phase 2 (coming soon)

- Custom Kafka-inspired message broker built from scratch
- AWS EC2 deployment
- Monitoring and alerting