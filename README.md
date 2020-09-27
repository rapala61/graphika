![Nightly](https://github.com/rapala61/graphika/workflows/Nightly/badge.svg)

# Summary

The current project is a Proof-of-Concept app built for Graphika. The purpose of this app is to analyze the influx of Tweets from a source, match certain terms against their text content, and ultimately output the matching of the Tweet id and term.

# Technologies

| Name | Description |
|---|---|
|Python| Developed using version `3.8.5`|
|flashtext [🔗](https://github.com/vi3k6i5/flashtext)| Library to search for keywords in documents at scale. Based on the [FlashText algorithm](https://arxiv.org/abs/1711.00046)|

# How to use

## Prerequisites

These instructions are for running the script from a Mac environment. Any other environment could most likely be used to run it from. However, it's not supported at this time.

- [Install](https://brew.sh/) (or update) Homebrew.
- [Install](https://opensource.com/article/20/4/pyenv) `pyenv` via `brew` 🍺.
- [Install](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-install) Python 3.8.5 via `pyenv`.
- [Install](https://pipenv.pypa.io/en/latest/install/#isolated-installation-of-pipenv-with-pipx) `pipenv`.
    - I used the "pipx" method described in the link. However, it might be easier to install with `brew`. Here's the [link](https://pipenv.pypa.io/en/latest/install/#homebrew-installation-of-pipenv-discouraged) for that alternative (read why they discourage it).

## Running in a local environment

- Clone and change directory to the root of the repo.
- Run `pipenv install`
- Execute the script by running `pipenv run src/main.py`

## Running as a Github Action (Scheduled job)

There is an example scheduled Github Action job [included](/.github/workflows/nightly.yml) in this repo. It can be a good starter for a custom GA job.

# TODO

## V2
- Add unit tests 
- Take tweets, groups and terms as arguments to the script.

## v3
- Create interfaces to obtain terms, node groups, and tweets in a source-agnostic way.

Made with :heart: by Rafa Pacas from 🇵🇦 and 🇺🇸.