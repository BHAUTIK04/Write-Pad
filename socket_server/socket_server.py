from websocket_server import WebsocketServer
from pymongo import MongoClient


# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	#server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def data_received(client, server, message):
	try:
		cl = MongoClient()
		db = cl["Writepad"]
		coll = db["pad"]
		print coll.update({"note_id":"sample"},{"$set":{"data":message}})
	except Exception as e:
		print "DataBase Unreachable....!!!"
	server.send_message_to_all(message)		
	print(client['id'], message)


PORT=8001
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(data_received)
server.run_forever()
