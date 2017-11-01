# Pytrexx
Python based command line tool to access the Bittrex cryptocurrency exhange

## Disclaimer:
IN NO EVENT, UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING, SHALL ANY PERSON BE LIABLE FOR ANY LOSS, EXPENSE OR DAMAGE, OF ANY TYPE OR NATURE ARISING OUT OF THE USE OF, OR INABILITY TO USE THIS SOFTWARE OR PROGRAM, INCLUDING, BUT NOT LIMITED TO, CLAIMS, SUITS OR CAUSES OF ACTION INVOLVING ALLEGED INFRINGEMENT OF COPYRIGHTS, PATENTS, TRADEMARKS, TRADE SECRETS, OR UNFAIR COMPETITION.

## Overview
A python based command line application that allows you to check accounts and even buy and sell
cryptocurrencies via a CLI interface.

## Support
This has been tested on Python 3 only. I have not tested this on Python 2,x or Windows as of yet.

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

    python3 pytrexx.py accountbalance BTC

If you want to get your last two deposits:

    python3 pytrexx.py deposits --n 2
