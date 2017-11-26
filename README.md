# Pyttrex
Python based command line tool to access the Bittrex cryptocurrency exhange

## Disclaimer:
IN NO EVENT, UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING, SHALL ANY PERSON BE LIABLE FOR ANY LOSS, EXPENSE OR DAMAGE, OF ANY TYPE OR NATURE ARISING OUT OF THE USE OF, OR INABILITY TO USE THIS SOFTWARE OR PROGRAM, INCLUDING, BUT NOT LIMITED TO, CLAIMS, SUITS OR CAUSES OF ACTION INVOLVING ALLEGED INFRINGEMENT OF COPYRIGHTS, PATENTS, TRADEMARKS, TRADE SECRETS, OR UNFAIR COMPETITION.

## Overview
A python based command line application that allows you to check accounts and even buy and sell
cryptocurrencies via a CLI interface.

## Support
This has been tested on Python 3 only. I have not tested this on Python 2.x or Windows as of yet.

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

  * accountbalance   Check your Bittrex account balance for a...
  * accountbalances  Check your Bittrex total account balance
  * address          Retrieve your currency wallet address
  * buy              Set buy limit order <currency pair>...
  * cancel           Cancel an existing buy/sell order
  * convert          <currency> type and <amount> to convert.
  * currencies       List all supported currencies on Bittrex
  * deposits         Check your Bittrex deposit history by...
  * open_orders      Get all open orders or by market
  * order            Check a Bittrex order by <UUID>
  * orders           Check your Bittrex order history
  * sell             Set buy limit order <currency pair>...
  * ticker           Used to get the current tick values for a...
  * withdrawals      Check your Bittrex withdrawal history


## Examples:

Get a balance of all of your coins on the Bittrex exchange:
```python
python3 pyttrex.py accountbalances
```
Check your Bitcoin account balance on Bittrex:
```python
python3 pyttrex.py accountbalance BTC
```
Get the last two deposits from your account:
```python
python3 pyttrex.py deposits --n 2
```
Sell 20 Vertcoin at 0.025 BTC:
```python
python3 pyttrex.py sell BTC-VTC 20 0.025
```
Check your Bittrex account balance for Bitcoin:
```python
python3 pyttrex.py accountbalance BTC
```
## Donations accepted:

ETH: 0xf691104b8d26a7a7e48CbCa41385d41F5DbCD205

BTC: 3J4DCcB8Wf9gLqmZXuNev6pkCqThHtgxzG
