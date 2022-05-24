# https://water2litter.net/rum/post/python_redmine_control/

from redminelib import Redmine

def getRedmineIssueById(isshueId):
    redmine = Redmine('http://redmine.serori.co.jp', key='58422508ffc64945d8231a5cc0e9bdbbebfb01aa')
    issue = redmine.issue.get(isshueId)

    print(issue.subject, issue.status.id, issue.status.name)
    return issue
