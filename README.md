# Perudo Calculator

After playing a few rounds of [Perudo](https://en.wikipedia.org/wiki/Dudo) during the end of the year 2020, I've decided to try to code up a decision-helper for the game.
My aim here is to use something like [Dash](https://dash.plotly.com/) to have a working UI.

### How to use

If you want to start the calculator, simply clone the repo, install the dependencies (Python libraries) and start Dash with:
```bash
python app.py
```

You can then take your favorite web browser, navigate to `http://127.0.0.1:8050/` and start having fun !

## TODO List

* Make the UI a bit clearer: something inspired by https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-clinical-analytics for example ?
* Introduce the notion of players
* Take into account one's own dices for which we know the values (using Bayes' rule ?)

## What I learned

* Apparently Plotly requires pandas ?
* Unittests are not run if they don't start with "test_"
* How HTML and CSS work (I mean the basics)
* How to setup Vim for autocompleting CSS

## Done

* Add the Perudo rule for the value 1 which acts like a wildcard
* Create a first static page
* Perform a calculation for 1 player with 1 normal dice.
* Add the ability to have several dices (still no notion of players yet).

## References

* Wikipedia article regarding [Binomial Coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient)
* Gérard Villemin's blog regarding [dice statistics](http://villemin.gerard.free.fr/Denombre/JeuxDes.htm)
* [This post](https://community.plotly.com/t/splitting-callback-definitions-in-multiple-files/10583/2) about splitting a dash app and especially putting the callbacks in other file than app.py

Yannick Schini, 2021
