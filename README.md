# Binomial trees in options pricing
## Introduction
In the binomial options pricing model, the underlying security at one time period,
represented as a node with a given price, is assumed to traverse to two other nodes
in the next time step, representing an up state and a down state. Since options are
derivatives of the underlying asset, the binomial pricing model tracks the underlying
conditions on a discrete-time basis. Binomial option pricing can be used to value
European options, American options, as well as Bermudan options.

The initial value of the root node is the spot price 0 S of the underlying security
with a given probability of returns u p should its value increase, and a probability
of loss d p should its value decrease. Based on these probabilities, the expected
values of the security are calculated for each state of price increase or decrease for
every time step. The terminal nodes represent every value of the expected security
prices for every combination of up states and down states. We can then calculate
the value of the option at every node, traverse the tree by risk-neutral expectations,
and after discounting from the forward interest rates, we can derive the value of
the call or put option.

## Language Environment
* Python 3.9
* Modules: math, numpy
