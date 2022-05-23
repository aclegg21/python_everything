import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('week15_project')

with open("testone.json") as json_file:
    Franchises = json.load(json_file)
    for franchise in Franchises:
        Name_of_Game = franchise['Name_of_Game']
        Console = franchise['Console']

        print("Adding franchise:", Name_of_Game, Console)

        table.put_item(
           Item={
               'Name_of_Game': Name_of_Game,
               'Console': Console,
            }
        )
