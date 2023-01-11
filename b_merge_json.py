import json
import os
_json_file='Ram_Setu_2022_Hindi_Full_Movie_CAMRip_(FilmyZilla.vin) (1).mp4.map.json'
with open(_json_file,'r') as jsn_read:
	_json_data=json.load(jsn_read)
# files created /generated
# for _ in _json_data['split_file']:
# 	print(_)
for _i in range (0,_json_data['number_of_split_file_created']):
	print(' Finding and merging file number {} ---> {}'.format((_i),_json_data['file']+'.part.'+str(_i)))
	if _json_data['split_file'][_i] ==_json_data['file']+'.part.'+str(_i):
		if  os.path.exists(_json_data['destination_directory']+'/'+_json_data['file']+'.part.'+str(_i)):
			with open(_json_data['file'],'ab') as write_bin:
				with open(_json_data['destination_directory']+'/'+_json_data['file']+'.part.'+str(_i),'rb') as read_bin:
					_data=read_bin.read()
					for _d in _data:
						write_bin.write(_d.to_bytes(1, byteorder='big'))
		else :
			print(' file does not exists ,stopping the process {} '.format(json_data['destination_directory']+'/'+_json_data['file']+'.part.'+str(_i)))
			break	
	else:
		print(' Map file does not exists or matches {}'.format(_json_data['split_file'][_i]))
		break



