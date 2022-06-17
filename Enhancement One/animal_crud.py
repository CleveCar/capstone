from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import loads, dumps
import pprint
import json

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    
# This creates the interface for connecting to the database
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/AAC' % (username, password) )
        self.database = self.client['AAC']

# This creates the method to implement the C in CRUD.
    def create(self, data):
        if data is not None:        
            self.database.animals.insert(data)  
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            

# This creates the method to implement the R in CRUD. 

    def read(self, data):
        if data is not None:
            result = self.database.animals.find(data,{'_id':False})
            return result
        else:
            raise Exception(" Nothing to find, because lookup parameter is empty.")
            return Exception

        
# This creates the method to implement the U in CRUD  

    def update(self, modify,  key1, value1, key2, value2 ):
        if modify is not None:
            update_query1 = {'key1':'value1'}
            update_alter = {'key2': 'value2'}           
            update_update = self.database.animals.update_one(update_query1, {'$set': update_alter})
            update_query2 = {'key1':'value1'}
            update_find = self.database.animals.find_one(update_query2)
            
           
       
            
  # Return data in json format          
            update_json = json.dumps([update_find])
            return update_json
            
        
        else:
            raise Exception(" Nothing to find, because modify parameter is empty.")
            return Exception

 # This creates the  method to implement the D in CRUD        
            
    def delete(self, remove):
        if remove is not None:
            del_query = {'key1': 'value1'}
            del_remove = self.database.animals.delete_one(del_query)
            
            return True
        
        else:
            raise Exception(" Nothing to find, because remove parameter is empty.")
            return Exception

                         
                         
            
        
            








