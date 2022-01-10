# Healthchecks for Python

A ***super*** simple wrapper for the Healthchecks API. When adding Healthchecks to a lot a scripts, having the `start()` and `finish()` in a lil' module is more convenient then adding `requests.get`, etc.

Healthchecks docs:
* [https://healthchecks.io/docs/measuring_script_run_time/](https://healthchecks.io/docs/measuring_script_run_time/)

## Installation
```bash
$ python setup.py install
$ # -- OR --
$ python setup.py install --user
```

## Usage

```python
import healthchecks as hc

hc_url = 'https://hc-ping.com/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee'
hc.start(hc_url)

#
# do stuff
#

hc.finish(hc_url)
```