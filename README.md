

[Create Jira Issue](https://pythonjira.com/create-a-jira-ticket-with-python/)

Create multiple issues
```
from jira import JIRA

jira_connection = JIRA(
    basic_auth=('workspace_email', 'api_token'),
    server="https://server_name.atlassian.net"
)

issue_list = [
    {
        'project': {'key': 'PJH'},
        'summary': 'Jira issue 1 from Python Jira Handbook',
        'description': 'Detailed ticket 1 description',
        'issuetype': {'name': 'Bug'},
    },
    {
        'project': {'key': 'PJH'},
        'summary': 'Jira issue 2 from Python Jira Handbook',
        'description': 'Detailed ticket 2 description',
        'issuetype': {'name': 'Bug'},
    },
    {
        'project': {'key': 'PJH'},
        'summary': 'Jira issue3 from Python Jira Handbook',
        'description': 'Detailed ticket 3 description',
        'issuetype': {'name': 'Bug'},
    }]

issues = jira_connection.create_issues(field_list=issue_list)
```


[Link issues](https://pythonjira.com/how-to-link-issues-on-jira-with-python/)

* Blocks: This relationship indicates that one issue is blocking the progress of another issue.
* Clones: This relationship indicates that one issue is a clone of another issue.
* Depends: This relationship indicates that one issue depends on the completion of another issue.
* Duplicates: This relationship indicates that one issue is a duplicate of another issue.
* Relates: This relationship indicates that two issues are related, but there is no direct dependency.


[Create Epic](https://pythonjira.com/how-to-create-epic-on-jira-with-python/)
```
# Create a new epic with the given name and description
ticket_options = {
    'project': {'key': 'PJH'},
    'summary': 'Testing epic from Python Jira Handbook',
    'description': 'This epic was created using the Python Jira Handbook',
    'issuetype': {'name': 'Epic'},
    'customfield_10011': 'Testing epic from Python Jira Handbook'
}

epic = jira_connection.create_issue(fields=ticket_options)
```
Note: ```customfield_10011``` is required when creating Epics only, the custom field is used to pass the Epic Name value. 


LINKS
* https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/#creating-an-issue-examples