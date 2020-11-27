import pymongo
from Command import Command


command = Command()
mongo_client = pymongo.MongoClient(host="localhost:27017")

work = True

while work:
    
    print('comand:\n ', command.list_command)
    run_command = input()
    command.execute_command(run_command, mongo_client)

    if run_command == 'stop':
        work = False
