# siliconvalleystands.org

This document explains how to do local developement and how to push changes to
the siliconvalleystands.org website.

## Developement

First download the Google Cloud SDK: https://cloud.google.com/sdk/downloads

After installing the Cloud SDK, install the Python App Engine tools:

``` shell
gcloud components install app-engine-python
```

Restart your shell, then launch the development server (from the same directory
as this README file):

``` shell
dev_appserver.py app/ --port 7777 --host 0.0.0.0
```

Navigate to localhost:7777 to view the website.

## Pushing Changes

To push the changes to App Engine, run:

``` shell
gcloud app deploy app/app.yaml
```

Note that this requires you to be an editor of the Google Cloud Platform project
we are using.

Also note that the command above creates a new version of the app and
IMMEDIATELY starts directing traffic to the new version. If you are making a big
change, pass in `--no-promote` to the command above so traffic doesn't go to the
new version. You can switch traffic to the new version through
http://console.cloud.google.com AFTER you verify that the new version works as
intended.
