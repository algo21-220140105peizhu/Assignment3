# Using the binomial option pricing model gives us a present value of $4.826 for the European put option
from StockOption import StockOption
from BinomialEuropeanOption import BinomialEuropeanOption
 eu_option = BinomialEuropeanOption
... 50, 50, 0.05, 0.5, 2,
... {"pu": 0.2, "pd": 0.2, "is_call": False})
print option.price()
4.82565175126

# The American put option is priced at $5.113. Since American options can be exercised
# at any time and European options can only be exercised at maturity, this added
# flexibility of American options increases their value over European options in certain
# circumstances.
# For American call options on an underlying asset that does not pay dividends, there
# might not be an extra value over its European call option counterpart. Because of
# the time value of money, it costs more to exercise the American call option today
# before the expiration at the strike price than at a future time with the same strike
# price. For an in-the-money American call option, exercising the option early loses the
# benefit of protection against adverse price movement below the strike price as well
# as its intrinsic time value. With no entitlement of dividend payments, there are no
# incentives to exercise American call options early.

from BinomialAmericanOption import BinomialTreeOption
am_option = BinomialTreeOption(
... 50, 50, 0.05, 0.5, 2,
... {"pu": 0.2, "pd": 0.2, "is_call": False, "is_eu": False})
print am_option.price()
5.11306008282

# Consider again the two-step binomial tree. The non-dividend paying stock has a
# current price of $50 and a volatility of 30 percent. Suppose that the risk-free rate is 5
# percent per annum and the time to maturity T is 0.5 years. We would like to find the
# value of an European put option with a strike price K of $50 by the CRR model:

from BinomialCRROption import BinomialTreeOption
eu_option = BinomialCRROption(
... 50, 50, 0.05, 0.5, 2,
... {"sigma": 0.3, "is_call": False})
print "European put: %s" % eu_option.price()
European put: 3.1051473413
am_option = BinomialCRROption(
... 50, 50, 0.05, 0.5, 2,
... {"sigma": 0.3, "is_call": False, "is_eu": False})
print "American put: %s" % am_option.price()
American put: 3.4091814964
  
# Using the same examples as before, we can price the options using an LR tree:
from BinomialLROption import BinomialLROption
eu_option = BinomialLROption(
... 50, 50, 0.05, 0.5, 3,
... {"sigma": 0.3, "is_call": False})
print "European put: %s" % eu_option.price()
European put: 3.56742999918
am_option = BinomialLROption(
... 50, 50, 0.05, 0.5, 3,
... {"sigma": 0.3, "is_call": False, "is_eu": False})
print "American put: %s" % am_option.price()
American put: 3.66817910413
  
