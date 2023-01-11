import os
import json
import math
_file_source='Ram_Setu_2022_Hindi_Full_Movie_CAMRip_(FilmyZilla.vin) (1).mp4'
_size=os.path.getsize(_file_source)
print('Size of file {}   is  {}'.format(_file_source,_size))
chunk_size=5000000
#5000 kb; 5mb
_json_map=_file_source+'.'+'map.json'
print(' Files to be splitted in {}'.format(chunk_size))
_files_json=[]
_struct={}
_struct['file']=_file_source
_struct['file_size']=_size
_struct['split_size']=chunk_size
_number_of_files=math.ceil(_size/chunk_size)
_struct['split_number_of_files']=_number_of_files
print(' Number of split files to be made to accomodate is {}'.format(_number_of_files))
_ab=_file_source.split('.')	
_struct['destination_directory']=_ab[0]

with open(_file_source,'rb') as read_bin:
	_data=read_bin.read()
info = [_data[i:i+chunk_size] for i in range(0, len(_data), chunk_size)]
#print(len(info))
_ii=0 # file increment counter
_dir=_ab[0]
if not os.path.exists(_dir):
        os.mkdir(_dir)
        print("Directory " , _dir,  " Created ")
else:    
        print("Directory " , _dir,  " already exists")

_split_files=[]
for _i in info:
	print(' part number :'+str(_ii))
	_splitt=_file_source+'.part.'+str(_ii)
	_split_files.append(_splitt)
	with open(_dir+'/'+_splitt,'wb') as write_bin:
		for _ij in _i:
			write_bin.write(_ij.to_bytes(1, byteorder='big'))
		_ii+=1


_struct['number_of_split_file_created']=_ii
_struct['split_file']=_split_files
with open(_json_map,'w') as jsn_file:
	json.dump(_struct,jsn_file,indent=4)