# https://water2litter.net/rum/post/python_redmine_control/

from redminelib import Redmine
import time
import pprint

redmine = Redmine('http://redmine.serori.co.jp', key='58422508ffc64945d8231a5cc0e9bdbbebfb01aa')
project = redmine.project.get('108_rozan')
issues = project.issues

ids = [34460, 32656, 34522, 32656, 33272, 33276, 33279]

start_time = time.time()

for id in ids:
    issue = redmine.issue.get(id)
    print(issue.subject, issue.status.id, issue.status.name)

end_time = time.time()
print("WorkingTime: {} sec".format(end_time-start_time))
