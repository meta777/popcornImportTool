import json
import os
import time

# D Carter / Metatek Limited - http://metatek.io

print("Houdini -> PopcornFX import tool")
print("--------------------------------")

start_time = time.time()

dir_path = os.path.dirname(os.path.realpath(__file__))
jsonExt = ('.json')

idDict1 = {'scope':'public','type':'numeric','name':'Id','options':{'type':{'type':'string','value':'nonarithmetic_integer'}}}
idDict2 = {'size':1,'storage':'int32','defaults':{'size':1,'storage':'int64','values':[-1]}}


for filename in os.listdir(dir_path):
    extension = os.path.splitext(filename)[-1].lower()  
    if extension == jsonExt:
        with open(filename) as json_file:            
            idDict3 = {'values':{'size':1,'storage':'int32','arrays':[]}}           
            try:
                data = json.load(json_file)
            except:
                print ('No JSON or errors in ' + filename)
            finally:
                pointcount = data[5]                                                # get total points in file
                idDict3['values']['arrays'].append(list(range(0, pointcount + 1)))  # append key 'arrays' with list of ints, 0 -> pointcount
                data.extend([idDict1.copy(),idDict2.copy(),idDict3.copy()])         # append Id data to existing JSON                                      
                json.dumps(data)                                                    # write & close
    else:
        print ('End of JSON files')
            
print("JSON prepared in %s seconds" % (time.time() - start_time))
