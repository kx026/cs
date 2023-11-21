import string
import random


import pika
def generate_pass(length):

    password = ''.join(random.choices(string.ascii_lowercase+string.digits, k=length))

    return password

while True:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='CS361')
    def callback(ch, method, properties, body):

        password1 = generate_pass(int.from_bytes(body, 'big'))
        channel.queue_declare(queue='CS361r')
        channel.basic_publish(exchange='', routing_key='CS361r', body=str.encode(password1))
        connection.close()


    channel.basic_consume(queue='CS361', on_message_callback=callback, auto_ack=True)
    print("Waiting for requests")
    channel.start_consuming()






