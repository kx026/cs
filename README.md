# Requesting: Send data through RabbitMQ. The number in the parentheses after "body=" will be the length of the generated password and can be set to any integer.
``` channel.basic_publish(exchange='', routing_key='CS361', body=(8).to_bytes(2, byteorder='big'))```
# Receiving: Consume data from a different channel through RabbitMQ.
``` channel.basic_consume(queue='CS361r', on_message_callback=callback, auto_ack=True)```
[uml.pdf](https://github.com/kx026/cs361/files/13422189/uml.pdf)
