import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='CS361')
channel.basic_publish(exchange='', routing_key='CS361', body=(8).to_bytes(2, byteorder='big'))
def callback(ch, method, properties, body):
    print("Password =", body.decode('utf-8'))
channel.queue_declare(queue='CS361r')
channel.basic_consume(queue='CS361r', on_message_callback=callback, auto_ack=True)
print("Waiting for password")
channel.start_consuming()

connection.close()
