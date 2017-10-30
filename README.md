# Pytrexx
Python based command line tool to access the Bittrex cryptocurrency exhange

## Overview
A python based command line application that allows you to check accounts and even buy and sell
cryptocurrencies via a CLI interface.

## Set up
This is still in the inital stages but for now, you have to generate an API key on Bittrexx and
then insert the two keys in line 20 of the Pytrexx.py file. THis will be stored in a configuration
file in future builds.

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

Commands:
  accountbalance  Check your Bittrex account balance
  buy             Set buy limit order <currency pair>...
  cancel          Cancel an existing buy/sell limit order
  convert         <currency> type and <amount> to convert.
  currencies      List all supported currencies on Bittrex
  deposits        Check your Bittrex deposit history
  order           Check a Bittrex order
  orders          Check your Bittrex order history
  sell            Set buy limit order <currency pair>...
  withdrawals     Check your Bittrex withdrawal history
