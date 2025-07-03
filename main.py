import yfinance as yf
import os
from datetime import datetime


def get_tickers():
    while True:
        tickers_str = input(
            "Enter ticker symbols separated by commas (e.g., SPY,AAPL,GOOG): "
        ).upper()
        tickers = [ticker.strip() for ticker in tickers_str.split(",")]
        if tickers and all(
            yf.Ticker(ticker).history(period="1d").empty is False for ticker in tickers
        ):
            return tickers
        print("Invalid ticker symbol found. Please try again.")


def get_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def get_directory():
    while True:
        path = input("Enter the directory to save the CSV files: ")
        if os.path.isdir(path):
            return path
        try:
            os.makedirs(path)
            return path
        except OSError:
            print("Invalid or non-creatable directory. Please try again.")


def main():
    tickers = get_tickers()
    start_date = get_date("Enter the start date (YYYY-MM-DD): ")
    end_date = get_date("Enter the end date (YYYY-MM-DD): ")
    output_dir = get_directory()

    for ticker in tickers:
        output_file = os.path.join(output_dir, f"{ticker}.csv")

        print(f"Downloading data for {ticker} from {start_date} to {end_date}...")

        # Download the data
        data = yf.download(ticker, start=start_date, end=end_date)

        if data.empty:
            print(f"No data found for {ticker} in the given date range.")
            continue

        data.rename(
            columns={
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Volume": "volume",
            },
            inplace=True,
        )

        final_data = data[["open", "high", "low", "close", "volume"]]

        # Save to CSV
        final_data.to_csv(output_file)

        print(f"Data for {ticker} saved successfully to {output_file}")


if __name__ == "__main__":
    main()
