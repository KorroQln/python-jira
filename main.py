from jira import JIRA

jira_connection = JIRA(
    basic_auth=('abc@mail.com', 'xxx'),
    server="https://korroqln.atlassian.net/"
)

# issue_dict = {
#     'project': {'key': 'SWIN'},
#     'summary': 'Testing ',
#     'description': 'Detailed description.',
#     'issuetype': {'name': 'Group'},
# }

# new_issue = jira_connection.create_issue(fields=issue_dict)


new_issue = jira_connection.create_issue_link(
    type="Relates",
    inwardIssue="SWIN-1",
    outwardIssue="SWIN-2",
    comment={'body': "This is a comment explaining why the issues are linked"}
)

print(new_issue)
