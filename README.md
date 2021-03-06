![logo](https://github.com/dennisgyor/Pyttrex/blob/master/pyttrex_logo.jpg "Pyttrex logo image")

# Pyttrex
Python based command line tool to access the Bittrex cryptocurrency exhange

## Disclaimer:
IN NO EVENT, UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING, SHALL ANY PERSON BE LIABLE FOR ANY LOSS, EXPENSE OR DAMAGE, OF ANY TYPE OR NATURE ARISING OUT OF THE USE OF, OR INABILITY TO USE THIS SOFTWARE OR PROGRAM, INCLUDING, BUT NOT LIMITED TO, CLAIMS, SUITS OR CAUSES OF ACTION INVOLVING ALLEGED INFRINGEMENT OF COPYRIGHTS, PATENTS, TRADEMARKS, TRADE SECRETS, OR UNFAIR COMPETITION.

## Overview
A python based command line application that allows you to check accounts and even buy and sell
cryptocurrencies via a CLI interface. This is essentially the Bittrexx application available via the command
line. Almost everything you can do in the Bittrex GUI, you can accomplish via Pyttrex (no 2FA needed).

## Support
This has been tested on Python 3 only. I have not tested this on Python 2.x or Windows as of yet.

In addition, if you want to take a deeper dive into the API calls and the paramaters for the various calls, reference the API documentation [here](https://www.bittrex.com/Home/Api).

## Set up

1. Clone the repo onto your system and cd into the pyttrex directory.

2. Install the proper modules in order to run pyttrex by running the following command:

    pip3 install -r requirements.txt

3. After you install the modules, open the APIkey.ini and enter your secret and key from your bittrexx API key. This should be all that you need to start making API calls with your account.

## Usage
Usage: pyttrex.py [OPTIONS] COMMAND [ARGS]...

  ******************pyttrex******************

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

Commands:

  * accountbalance:   Check your Bittrex account balance for a...
  * accountbalances:  Check your Bittrex total account balance
  * address:          Retrieve your currency wallet address
  * buy:              Set buy limit order <currency pair>...
  * cancel:           Cancel an existing buy/sell order
  * convert:          <currency> type and <amount> to convert.
  * currencies:       List all supported currencies on Bittrex
  * deposits:         Check your Bittrex deposit history by...
  * history:          Used to retrieve the latest trades that have...
  * open_orders:      Get all open orders or by market
  * order:            Check a Bittrex order by <UUID>
  * order_book:       Used to get retrieve the orderbook for a...
  * orders:           Check your Bittrex order history
  * sell:             Set buy limit order <currency pair>...
  * summaries:        Used to get the last 24 hour summary of all...
  * summary:          Used to get the last 24 hour summary of all...
  * ticker:           Used to get the current tick values for a...
  * withdrawals:      Check your Bittrex withdrawal history


## Examples:

Get a balance of all of your coins on the Bittrex exchange:

    python3 pyttrex.py accountbalances

Check your Bitcoin account balance on Bittrex:

    python3 pyttrex.py accountbalance BTC

Get the last two deposits from your account:

    python3 pyttrex.py deposits --n 2

Sell 20 Vertcoin at 0.025 BTC:

    python3 pyttrex.py sell BTC-VTC 20 0.025

Check your Bittrex account balance for Bitcoin:

    python3 pyttrex.py accountbalance BTC

To get a list of all currencies supported on the Bittrex platform:

    python3 pyttrex.py currencies

To retrieve the last 24 hours of all active exchanges:

    python3 pyttrex.py summaries

Retrieving the order book for BTC-LTC for all buys:

    python3 pyttrex.py order_book BTC-LTC buy

Check the last three exchange transactions for DOGE coin:

    pyttrex.py history BTC-DOGE --n 3

## Donations accepted:

ETH: 0xf691104b8d26a7a7e48CbCa41385d41F5DbCD205

BTC: 3J4DCcB8Wf9gLqmZXuNev6pkCqThHtgxzG
