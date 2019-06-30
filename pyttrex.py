#!/usr/bin/env python3
__author__ = 'Dennis.Gyor'

from bittrex import Bittrex
import datetime
import click
from forex_python.bitcoin import BtcConverter
from tabulate import tabulate
import logging
from configparser import ConfigParser
from termcolor import colored, cprint

# Datetimestamp
dts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Parser object for creating the config file
config = ConfigParser()

# Read in config file entries and create vars
config.read('APIkey.ini')
key = config.get('API keys', 'key')
secret = config.get('API keys', 'secret')

# Bittrex API key object
# my_bittrex = Bittrex(secret, 'few') <-- for testing invalid API calls
my_bittrex = Bittrex(key, secret)

# set array got tabulate formats
tabfmt = ("plain", "simple", "grid", "fancy_grid", "pipe", "orgtbl", "jira", "presto", "psql", "rst", "mediawiki", "moinmoin", "youtrack", "html", "latex", "latex_raw", "latex_booktabs", "textile")

# create the command line group for the click framework
@click.group()
@click.version_option('1.0.0')
@click.pass_context

# The top level cli command
def cli(self):
    """******************Pytrexx******************\n
\n
    Bittrex account and trading bot command line utility.\n

    Features:\n
      Fiat to BTC Converter\n
      Bittrex markets (Execute manual trades)\n
      Bittrex account (Query account information)\n
      Bittrex public (Retrieve exchange information)\n
      COMING SOON: Bittrex trading bot (automated trading)\n
    """

# Convert command code block START
@cli.command('convert', help='<currency> type and <amount> to convert.')
# Arguments for convert
@click.argument('currency', nargs=1, type=str)
@click.argument('amount', nargs=1, type=float)

def convert(currency, amount):
    """Converter method to convert fiat to BTC."""
# Create a new converter object with standardized date
    b = BtcConverter()
    x = b.get_latest_price(currency)

    cprint('Powered by Coindesk | https://www.coindesk.com/price/', 'green')
    cprint("[" + str(dts) + "]" + "  " + currency.upper() + " for 1.0 Bitcoin (BTC) is " + str(x), "green")

    # convert to BTC
    conversion_amount = b.convert_to_btc(amount, currency.upper())
    cprint("[{}]  Converting {} to BTC: {} {} is currently worth {} BTC!".format(str(dts), currency.upper(), "%0.2f" %(amount), currency.upper(), conversion_amount), "green")
# Convert command code block END

### ACCOUNT API CALLS ###

# accountbalances command code block START
@cli.command('accountbalances', help='Check your Bittrex total account balance')
@click.option('-f')    # set output based on tabulate supported formats

def accountbalances(f):
  """Used to retrieve the balance from your account for a specific currency."""
  # print(type(my_bittrex)) <-- for debugging
  # sets format or default to grid style
  fmt = f or "grid"
  # checks to see if the option equals contents in the tabfmt list
  if fmt in tabfmt:
    tx = my_bittrex.get_balances()
    print(tabulate(tx['result'], headers="keys", tablefmt=fmt))
  else:
    print("ERROR: Invalid format. Refer to valid tabulate formats here: https://pypi.python.org/pypi/tabulate.")
# accountbalances command code block END

# accountbalance command code block START
@cli.command('accountbalance', help='Check your Bittrex account balance for a currency')
# required
@click.argument('cryptocurrency', nargs=1, type=str)

def accountbalance(cryptocurrency):
  """Used to retrieve the balance from your account for a specific currency."""
  # print(type(my_bittrex)) <-- for debugging
  try:
    tx = my_bittrex.get_balance(cryptocurrency)
    table = tabulate([tx['result']], headers="keys", tablefmt="grid")
    print(table)
  except TypeError as e:
    if tx['message'] ==  'INVALID_SIGNATURE':
      print("Invalid Credentials. Check your API keys.")
    elif tx['message'] ==  'INVALID_CURRENCY':
      print("Invalid Currency specified. Check your symbol.")
    else:
      print("Unknown error.")
  except:
    print(e)
# accountbalance command code block END

# getdepositaddress command code block START
@cli.command('address', help='Retrieve your currency wallet address')
# required argument to add the crypto 3 letter symbol
@click.argument('cryptocurrency', nargs=1, type=str)

# Used to retrieve the balance from your account for a specific currency.
def getdepositaddress(cryptocurrency):
  # print(type(my_bittrex)) <-- for debugging
  try:
    tx = my_bittrex.get_balance(cryptocurrency)
    table = tabulate([tx['result']], headers="keys", tablefmt="grid")
    print(table)
  except TypeError as e:
    if tx['message'] ==  'INVALID_SIGNATURE':
      print("Invalid Credentials. Check your API keys.")
    elif tx['message'] ==  'INVALID_CURRENCY':
      print("Invalid Currency specified. Check your symbol.")
    else:
      print("Unknown error.")
  except:
    print(e)
# getdepositaddress command code block END

# withdraw command code block START
# @cli.command('withdraw', help='Withdraw coins from Bittrex into an external wallet address')
#TODO: create this method
# withdraw command code block END

# get order command code block START
@cli.command('order', help = 'Check a Bittrex order by <UUID>')
@click.argument('id', type = str)

def order(id):
  tx = my_bittrex.get_order(id)
  print(tabulate([tx['result']], headers="keys", tablefmt="grid"))
# get order command code block END

# orderhistory command code block START
@cli.command('orders', help='Check your Bittrex order history')
@click.option('--cp')    # cryptocurrency pair option (i.e. BTC-ETH)

def orders(cp):
  tx = my_bittrex.get_order_history(cp)
  print(tabulate(tx["result"], headers="keys", tablefmt="grid"))
  print(tx['message'])
# orderhistory command code block END

# deposit history command code block START
@cli.command('deposits', help='Check your Bittrex deposit history by currency or number of deposits ')
@click.option("-c")              # specify cryptocurrency option
@click.option("-n", type=int)    # number of deposits option

def deposits(c, n):
  tx = my_bittrex.get_deposit_history(c)
  if n != None:
    print(tabulate(tx["result"][:n], headers="keys", tablefmt="grid"))
  else:
    print(tabulate(tx["result"], headers="keys", tablefmt="grid"))
# deposit history command code block END

# withdrawal history command code block START
@cli.command('withdrawals', help='Check your Bittrex withdrawal history')
@click.option("--c")
@click.option("--n", type=int)

def withdrawals(c, n):
  tx = my_bittrex.get_withdrawal_history(c)
  if n != None:
    print(tabulate(tx["result"][:n], headers="keys", tablefmt="grid"))
  else:
    print(tabulate(tx["result"], headers="keys", tablefmt="grid"))
# withdrawal history command code block END

### MARKET API CALLS ###

# market/buylimit command code block START
@cli.command('buy', help='Set SELL LIMIT order <currency pair> <quantity> <rate> in BTC')
@click.argument('cp', type=str)
@click.argument('quantity', type=float)
@click.argument('rate', type=float)

# Limit buy method
def buy(cp, quantity, rate):
  if click.confirm('Are you sure you want to set this BUY LIMIT order?', abort=True):
      tx = my_bittrex.buy_limit(cp, quantity, rate)
      if tx['message'] == 'ZERO_OR_NEGATIVE_NOT_ALLOWED':
        cprint("Check your balances. You may have insufficient funds.", 'red')
      elif tx['message'] == 'INVALID_MARKET':
        cprint("Invalid Currency pair specified. Check your currency pairs.", 'red')
      elif tx['message'] == 'DUST_TRADE_DISALLOWED_MIN_VALUE_50K_SAT':
        cprint("Unable to trade dust. Minimum 50k Satoshis.", 'red')
      elif tx['message'] == 'APIKEY_INVALID':
        cprint("API Key is invalid. Check APIkey.ini and verify your API key is valid.", 'red')
      else:
        cprint("BUY-LIMIT order of {} {} at {} BTC was successful! ".format(quantity, cp, rate), "green")
        cprint(tabulate([tx["result"]], headers="keys", tablefmt="grid"), "green")
# market/buylimit command code block END

# market/selllimit command code block START
@cli.command('sell', help='Set SELL LIMIT order <currency pair> <quantity> <rate> in BTC')
@click.argument('cp', type=str)
@click.argument('quantity', type=float)
@click.argument('rate', type=float)

# Limit sell method
def sell(cp, quantity, rate):
  if click.confirm("Are you sure you want to make this SELL LIMIT order?", abort=True):
      tx = my_bittrex.sell_limit(cp, quantity, rate)
      if tx['message'] == 'ZERO_OR_NEGATIVE_NOT_ALLOWED':
        cprint("Check your balances. You may have insufficient funds.", 'red')
      elif tx['message'] == 'INVALID_MARKET':
        cprint("Invalid Currency pair specified. Check your currency pairs.", 'red')
      elif tx['message'] == 'DUST_TRADE_DISALLOWED_MIN_VALUE_50K_SAT':
        cprint("Unable to trade dust. Minimum 50k Satoshis.", 'red')
      elif tx['message'] == 'APIKEY_INVALID':
        cprint("API Key is invalid. Check APIkey.ini and verify your API key is valid.", 'red')
      else:
        cprint("SELL-LIMIT order of {} {} at {} BTC was successful! ".format(quantity, cp, rate), "green")
        cprint(tabulate([tx["result"]], headers="keys", tablefmt="grid"), "green")

# market/selllimit command code block END

# market/cancel command code block START
@cli.command('cancel', help='Cancel an existing buy/sell order')
@click.argument('id', type=str)

def cancel(id):
  if click.confirm('Are you sure you want to cancel order ' + id + '?', abort=True):
    cancel_count = my_bittrex.cancel(id)
    if cancel_count['success']:
      cprint('Order ' + id + ' cancelled successfully!', 'green')
    else:
      cprint('Order ' + id + ' cancellation ERROR! You may need to check your UUID.', 'red')
# market/cancel command code block END

# market/getopenorders command code block START
@cli.command('open_orders', help='Get all open orders or by market')
@click.option('--cp', type=str)

# GetOpenOrders method
def open_orders(cp):
  tx = my_bittrex.get_open_orders(cp)
  if len(tx["result"]) == 0:
    print("There are currently no open orders active.")
  else:
    print(tabulate(tx["result"], headers="keys", tablefmt="grid"))
# market/getopenorders command code block END

### PUBLIC API CALLS ###

# public/currencies command code block START
@cli.command('currencies', help='List all supported currencies on Bittrex')

def currencies():
    """GET a list of all currencies supported on the Bittrex platform."""
    tx = my_bittrex.get_currencies()
    print(tabulate(tx["result"], headers="keys", tablefmt="grid"))
# public/currencies command code block END

# public/getticker command code block START
@cli.command('ticker', help='Used to get the current tick values for a market.')
@click.argument('markets', type=str)

def ticker(markets):
  """Used to get the current tick values for a market."""
  tx = my_bittrex.get_ticker(markets)
  print(tabulate([tx["result"]], headers="keys", tablefmt="grid"))
# public/getticker command code block END

# public/getmarketsummaries command code block START
@cli.command('summaries', help='Used to get the last 24 hour summary of all active exchanges.')

def summaries():
  """Used to get the last 24 hour summary of all active exchanges."""
  tx = my_bittrex.get_market_summaries()
  print(tabulate(tx["result"], headers="keys", tablefmt="grid"))
# public/getmarketsummaries command code block END

# public/getmarketsummary command code block START
@cli.command('summary', help='Used to get the last 24 hour summary of all active exchanges.')
@click.argument('markets', type=str)

def summary(markets):
  """Used to get the last 24 hour summary of all active exchanges."""
  tx = my_bittrex.get_marketsummary(markets)
  print(tabulate(tx["result"], headers="keys", tablefmt="grid"))
# public/getmarketsummary command code block END

# public/getorderbook command code block START
@cli.command('order_book', help='Used to get retrieve the orderbook for a given market.')
@click.argument('markets', type=str)
@click.argument('order_type', type=str)    # buy, sell or both are the 3 valid entries

def order_book(markets, order_type):
  """Used to get retrieve the orderbook for a given market."""
  tx = my_bittrex.get_orderbook(markets, order_type)
  print(tabulate(tx["result"], headers="keys", tablefmt="grid"))
# public/getorderbook command code block END

# public/getmarkethistory command code block START
@cli.command('history', help='Used to retrieve the latest trades that have occured for a specific market.')
@click.argument('markets', type=str)
@click.option("--n", type=int)

def history(markets, n):
  """Used to retrieve the latest trades that have occured for a specific market."""
  tx = my_bittrex.get_market_history(markets, n)
  if tx['message'] == 'INVALID_MARKET':
    cprint("Invalid currency specified. Check your currency pair.", 'red')
  else:
    print(tabulate(tx["result"][:n], headers="keys", tablefmt="grid"))

# public/getmarkethistory command code block END

if __name__ == '__main__':
    cli()
