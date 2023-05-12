#!/usr/bin/python3
import boto3
session = boto3.session.Session(profile_name="default")
logclient = boto3.client('logs')
dict_lg = {}
list_lg = []
def logGroup():
    paginator = logclient.get_paginator('describe_log_groups')
    for page in paginator.paginate():
        for group in page['logGroups']:
            print(group)
            if "retentionInDays" in group:
             dict_lg[group['logGroupName']] = group['retentionInDays']
            else:
                list_lg.append(group['logGroupName'])
def putLogRetention():
    for k,v in dict_lg.items():
        #In case of you want to search any word in loggroup name
        if 'staging' in k or 'Staging' in k:
            if v != 30:
                response = logclient.put_retention_policy(
                logGroupName=k,
                retentionInDays=30
                )
                print(response)
        else:
            if v != 365:
                response = logclient.put_retention_policy(
                logGroupName=k,
                retentionInDays=365
                )
                print(response)
    for i in list_lg:
        if 'staging' in i or 'Staging' in i:
            response = logclient.put_retention_policy(
            logGroupName=i,
            retentionInDays=30
            )
            print(response)
        else:
            response = logclient.put_retention_policy(
            logGroupName=i,
            retentionInDays=365
            )
            print(response)
    print("All logs have retention period as per complicance")
    
logGroup()
putLogRetention()
