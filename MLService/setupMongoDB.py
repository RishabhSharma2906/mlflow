from pymongo import MongoClient
import logging
import os

client_URL = os.environ.get('DB')

def findConnection():
    #client_URL = os.environ.get('DB')
    client = MongoClient(client_URL)
    logging.info('List of databases :' + str(client.list_database_names()))
    client.close()

def createDatabase():
    logging.info('Creating Database')
    #client_URL = os.environ.get('DB')
    client = MongoClient(client_URL)
    db = client['MLService']
    posts = db.posts
    post_data = {
        'first':'Rishabh',
    }
    result = posts.insert_one(post_data)
    dblist = client.list_database_names()
    print(posts.find_one({'first' : 'Rishabh'}))
    print(dblist)
    if "MLService" in dblist:
        logging.info('Inserted Database')
        print('Inserted Database')
    client.close()

def insertRecordsModels():
    client = MongoClient(client_URL)
    client.drop_database('MLService')
    db = client['MLService']
    modelListCol = db['ModelList']

    first_model = { 'model_id' : 'NB_001',
    'model_type' : 'naive_bayes',
    'created_on' : '20/June/2015',
    'deployed_from' : '26/June/2015',
    'deployed_till' : '31/July/2015',
    'production_accuracy' : 75,
    'training_accuracy' : 80,
    'testing_accuracy' : 77,
    'deployed' : False,
    'model_details' : 'This is a basic naive bayes model'}
        
    second_model = { 'model_id' : 'NN_RNN_001',
    'model_type' : 'RNN',
    'created_on' : '20/Apr/2016',
    'deployed_from' : '11/May/2015',
    'deployed_till' : 'Currently deployed',
    'production_accuracy' : 89,
    'training_accuracy' : 99,
    'testing_accuracy' : 98,
    'deployed' : True,
    'model_details' : 'This is a RNN'}
    
    x = modelListCol.insert_many([first_model, second_model])
    cursor = modelListCol.find()
    list_of_models = []
    for d in cursor:
        list_of_models.append(d)
    return list_of_models

def listAllModels():
    client = MongoClient(client_URL)
