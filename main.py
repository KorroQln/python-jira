from jira import JIRA

jira_connection = JIRA(
    basic_auth=('hazim.aqlan97@gmail.com', 'ATATT3xFfGF0_mkRLmWZ5tDpDJp5H1oMl_QGCeBFUchJTVU0LkhbRCTwlmYMVkfJxExUsVF7tqsmmnAiNzzeuUzsL7NVwQTdCWsmd9j-5HG-o0Mc6fnhI_kw8onngNPIR2HNz6MF64ITSrKqUqHyIpNegoe71ptTymbQpib7CQcS50opsxgQ8Rg=3563A69B'),
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