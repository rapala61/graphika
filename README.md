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

## Running as Scheduled job

There are many ways to run this script as a schedules job. The best way to do it would depend entirely on the already existing architecture and expertise of the team. Here are 2 ways to schedule the job.

### Github Actions

Using Github Actions is as simple as adding a `.yml` file and let Github run the job for us. The benefits are many. We are already using Github in some capacity in our ecosystem. Github usually has stellar documentation. A huge community. There is a Marketplace for all types of actions. E.g. Slack integration, CloudWatch logs, etc.

There is an example scheduled Github Action job [included](/.github/workflows/nightly.yml) in this repo. It can be a good starter for a custom job.

### Jenkins

If we are using a managed Jenkins solution or host it in an EC2 instance ourselves. We can schedule a job to pull the github repo, install dependencies and run the script. We can monitor the job via an integration via email, slack, Pagerduty, etc.

# TODO

This is a list of nice-to-have features/changes if this PoC were to become a production ready tool.

- Add unit tests
- Eliminate hard coded values from the code and use ENV variables.
- Create API integrations w/ the sources of terms, node groups, and Tweets.
    - Implement high level interfaces to obtain terms, node groups, and Tweets in a source-agnostic way.
- Depending on the scheduling strategy we pick. Implement logging and pipe to a compatible Cloud log manager.
- If we are storing this data for BI and analysis purposes:
    - Save the output of the script as a CSV in an S3 bucket.
        - This is assuming we have a data infrastructure that uses S3 as a data lake or can load data from S3.
- If we are storing this data into an existing DB:
    - Store the tuples in the correct collection/table as part of the job.


Made with :heart: by Rafa Pacas from 🇵🇦 and 🇺🇸.