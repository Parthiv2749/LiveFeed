
import socket, cv2, pickle
import cv2

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = '192.168.89.126' # server IP
print('Server IP:',server_ip)
port = 9999

socket_address = (server_ip,port)

def start_video_stream():

	
	camera = True
	if camera == True:
		vid = cv2.VideoCapture(0)
	
	else:
		vid = cv2.VideoCapture('videos/boat.mp4')
  

	print('CLIENT {} CONNECTED!'.format(server_ip))
	
	while(vid.isOpened()):
				
				img,frame = vid.read()
				cv2.imshow('my pic', frame)
				ret, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY),30])
				a = pickle.dumps(buffer)
				server_socket.sendto( a, socket_address)
			    
				if cv2.waitKey(10) == 13: 
					server_socket.close()
					break


while True:
	start_video_stream()


