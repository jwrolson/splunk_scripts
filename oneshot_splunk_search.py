import datetime as dt
import splunklib.client as client
import splunklib.results as results

# Create dict for splunk configs
config = {}
config['host'] = "10.206.36.185"
config['port'] = 8089
config['username'] = ''
config['password'] = ''
config['owner'] = "nobody"
config['app'] = "gi_entapps_em_web"
config['autologin'] = True

# Create service for interacting with Splunk search heads
service = client.connect(**config)

# Create dict for oneshot search
kwargs_oneshot = {}

# Get current time
current_time = dt.datetime.now()

# Get time -5mins
minus_5m_time = current_time - dt.timedelta(minutes = 5)

# Set latest time
kwargs_oneshot['latest_time'] = dt.datetime.strftime(current_time, '%Y-%m-%dT%H:%M:%S%Z')

# Set earliest time
kwargs_oneshot['earliest_time'] = dt.datetime.strftime(minus_5m_time, '%Y-%m-%dT%H:%M:%S%Z')

# Search query stanza
searchquery_oneshot = "search index=appdev | head 10"

# Dispatch and wait for search to complete
oneshotsearch_results = service.jobs.oneshot(searchquery_oneshot, **kwargs_oneshot)

# iterate through results
reader = results.ResultsReader(oneshotsearch_results)
for item in reader:
    print(item)
