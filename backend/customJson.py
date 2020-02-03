from flask.json import JSONEncoder
import datetime

class Custom_Jsonify(JSONEncoder):
    def default(self, obj):
        #if it is an object of time change to this format
        #HH:MM:SS 
        if isinstance( obj, datetime.time):
            return obj.strftime("%H:%M:%S")
        #if it is an object of time change to this format
        #HH:MM:SS 
        elif isinstance( obj, datetime.datetime):
            return obj.strftime("%H:%M:%S")
        #if it is an object of time change to this format
        #HH:MM:SS 
        elif isinstance( obj, datetime.date):
            return obj.strftime("%H:%M:%S")        
        return JSONEncoder.default(self,obj)    
