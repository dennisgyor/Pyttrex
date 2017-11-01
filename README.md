# Pytrexx
Python based command line tool to access the Bittrex cryptocurrency exhange

## Overview
A python based command line application that allows you to check accounts and even buy and sell
cryptocurrencies via a CLI interface.

## Set up
After you install the script, open the APIkey.ini and enter your secret and key from your bittrexx API key. This should be all that you need to start making API calls with your accont.

## Usage
Usage: pytrexx.py [OPTIONS] COMMAND [ARGS]...

  ******************Pytrexx******************

  Bittrex account and trading bot command line utility.

  Features:

    Fiat to BTC Converter

    Bittrex markets (Execute manual trades)

    Bittrex account (Query account information)

    Bittrex public (Retrieve exchange information)

    COMING SOON: Bittrex trading bot (automated trading)

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

## Available Commands:

accountbalance  Check your Bittrex account balance options:<currency>

buy             Set buy limit order <currency pair> <quantity> <rate> *(in BTC)*

cancel          Cancel an existing buy/sell limit order <UUID>

convert         <currency> type and <amount> to convert.

currencies      List all supported currencies on Bittrex.

deposits        Check your Bittrex deposit history.

order           Check a Bittrex order.

orders          Check your Bittrex order history.

sell            Set buy limit order <currency pair> <quantity> <rate> *(in BTC)*

withdrawals     Check your Bittrex withdrawal history

## Examples:

If you want to check your Bitcoin account balance on Bittrex:

```python
  python3 pytrexx accountbalance BTC
