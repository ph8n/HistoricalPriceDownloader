# Historical Price Downloader

A simple, interactive command-line tool to download historical stock price data from Yahoo Finance and save it to CSV files.

## Features

- Download data for multiple ticker symbols at once.
- Specify a custom date range.
- Choose the output directory for the CSV files.
- Interactive prompts with input validation.

## Prerequisites

Before you begin, ensure you have [uv](https://github.com/astral-sh/uv) installed. `uv` is an extremely fast Python package installer and resolver, written in Rust, that is used to manage this project's dependencies.

## Installation & Setup

1. **Clone the repository (or download the source code):**

    ```bash
    git clone https://github.com/ph8n/HistoricalPriceDownloader
    cd historical-price-downloader
    ```

2. **Create a virtual environment and install dependencies:**

    `uv` makes this a seamless one-step process. Run the following command in the project root directory:

    ```bash
    uv sync
    ```

    This command creates a local virtual environment (`.venv`) and installs all the dependencies specified in `pyproject.toml` (`yfinance`).

## Usage

Once the dependencies are installed, you can run the script using `uv`:

```bash
uv run main.py
```

The script will guide you through the process with interactive prompts:

1. **Enter Ticker Symbols:** Provide a comma-separated list of symbols (e.g., `AAPL,GOOG,MSFT`).
2. **Enter Start Date:** Use `YYYY-MM-DD` format.
3. **Enter End Date:** Use `YYYY-MM-DD` format.
4. **Enter Output Directory:** Specify the path where the CSV files will be saved.

The script will then download the data for each ticker and save it to a separate CSV file in the specified directory.

## Packaging the Project

To make this project easily distributable, you can build it into a wheel file. A wheel is a standard Python distribution format that contains the packaged code and can be easily installed elsewhere.

1. **Build the wheel:**

    ```bash
    uv build --wheel
    ```

2. **Distribute the wheel:**

    The command will create a `.whl` file in the `dist/` directory (e.g., `dist/historical_price_downloader-0.1.0-py3-none-any.whl`). You can share this file with others.

3. **Install the wheel:**

    Another user can install your project from the wheel file using `pip` or `uv`:

    ```bash
    uv pip install historical_price_downloader-0.1.0-py3-none-any.whl
    ```

This will install the script and its dependencies, allowing them to run it from anywhere.
