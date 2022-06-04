import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
import DataUtils
import GenericTransformers
import GroupsTransformers
import StdResponses
import StdAPIUtils

def get_group_remove_users_resources(sessionname,token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = {
        "groupID":JsonData['itemid'],
        "userIDS":JsonData['userids']
    }

    Body = """
        mutation addUsersToGroup($groupID: ID!, $userIDS: [ID!]){
        groupUpdate(id: $groupID, removedUserIds: $userIDS) {
          ok
          error
          entity{
            id
            name
            isActive
            createdAt
            updatedAt
            type
            users {
                edges{
                    node{
                        id
                        email
                        firstName
                        lastName
                    }
                }
            }
          }

        }
    }
    """

    return True,api_call_type,Headers,Body,variables


def get_group_add_users_resources(sessionname,token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = {
        "groupID":JsonData['itemid'],
        "userIDS":JsonData['userids']
    }

    Body = """
        mutation addUsersToGroup($groupID: ID!, $userIDS: [ID!]){
        groupUpdate(id: $groupID, addedUserIds: $userIDS) {
          ok
          error
          entity{
            id
            name
            isActive
            createdAt
            updatedAt
            type
            users {
                edges{
                    node{
                        id
                        email
                        firstName
                        lastName
                    }
                }
            }
          }

        }
    }
    """

    return True,api_call_type,Headers,Body,variables


def get_group_list_resources(sessionname,token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"

    Body = """
            {
  groups(after: null, first:1000) {
    edges {
      node {
        id
        name
        createdAt
        updatedAt
        isActive
        type
        users {
            edges{
                node{
                    id
                    email
                    firstName
                    lastName
                }
            }
        }
        resources {
            edges{
                node{
                    id
                    name
                    address {
                        type
                        value
                    }
                    isActive
                }
            }
        }

      }
    }
    pageInfo {
      startCursor
      hasNextPage
    }
  }
}
    """

    return True,api_call_type,Headers,Body,None

def get_group_show_resources(sessionname,token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = {"itemID":JsonData['itemid']}
    Body = """
         query
         getObj($itemID: ID!){
            group(id:$itemID) {
                        id
                        name
                        createdAt
                        updatedAt
                        isActive
                        type
                        users {
                            edges{
                                node{
                                    id
                                    email
                                    firstName
                                    lastName
                                }
                            }
                        }
                        resources {
                            edges{
                                node{
                                    id
                                    name
                                    address {
                                        type
                                        value
                                    }
                                    isActive
                                }
                            }
                        }
      }
  }
    """

    return True,api_call_type,Headers,Body,variables

def remove_users_from_group(outputFormat,sessionname,itemid,userids):
    r,j = StdAPIUtils.generic_api_call_handler(outputFormat,sessionname,get_group_remove_users_resources,{'itemid':itemid,'userids':userids},GroupsTransformers.GetAddOrRemoveUsersAsCsv,'groupUpdate')
    print(r)

def add_users_to_group(outputFormat,sessionname,itemid,userids):
    r,j = StdAPIUtils.generic_api_call_handler(outputFormat,sessionname,get_group_add_users_resources,{'itemid':itemid,'userids':userids},GroupsTransformers.GetAddOrRemoveUsersAsCsv,'groupUpdate')
    print(r)

def item_show(outputFormat,sessionname,itemid):
    r,j = StdAPIUtils.generic_api_call_handler(outputFormat,sessionname,get_group_show_resources,{'itemid':itemid},GroupsTransformers.GetShowAsCsv,"group")
    print(r)
def item_list(outputFormat,sessionname):
    r,j = StdAPIUtils.generic_api_call_handler(outputFormat,sessionname,get_group_list_resources,{},GroupsTransformers.GetListAsCsv,'groups')
    print(r)