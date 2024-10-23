# Cryptocurrency Analysis

This project performs a simple analysis of cryptocurrency prices using Python. It retrieves current price data and 24-hour price changes from the CoinGecko API and analyzes the trends for selected cryptocurrencies.

## Features

- **Data Retrieval**: Fetches current prices and 24-hour change data for specified cryptocurrencies.
- **Data Analysis**: Analyzes the retrieved data to determine the current price, 24-hour price change, and price trend (up or down).
- **Data Output**: Saves both the raw data and the analysis results to JSON files for easy access.

## Requirements

Make sure to have the following library installed:

- `requests`

You can install it using pip:

```bash
pip install requests
```

## Example Output
After running the script, you will find two JSON files in your directory:

- **crypto_data.json**: Contains the fetched cryptocurrency data, including current prices and 24-hour changes.
- **crypto_analysis.json**: Contains the analysis, which includes current prices, price changes, and trends for each cryptocurrency.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
