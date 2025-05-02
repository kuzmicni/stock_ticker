# stock_ticker
Cli tool to help you easily get the top-performing Stocks, ETFs, and Bonds.

## Setup

### Conda
```
conda create -n stockenv python=3.10
conda activate stockenv
pip install --upgrade pip
pip install .
```
### Python3 VENV
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install .

```
## Run the CLI tool and get the Stock performance. Example: Robinhood (Ticker: HOOD)
```
stock_ticker HOOD
```
Sample output
```
HOOD is +18.20% YTD.
```