# ambient-temperature-with-dht11-broker-and-Android-APP

temperature in real time raspberry pub e android sub

•	Ideia Geral: Implementar um sistema distribuído usando o protocolo MQTT como broker de mensagens. O sistema tem um publisher (raspberry pi 3 + dht11) e um subscriber (celular). O broker de mensagem é o CloudMQTT.

•	Operação: O publisher irá mandar uma mensagem contendo a temperatura e umidade do ambiente a partir do sensor dht11 ao subscriber, tornando possivel ver a temperatura e umidade em tempo real.

•	Contexto de utilização: Monitoramento de temperatura e umidade em ambientes de medicamentos. O sistema é composto de hardware e software que realizam medições locais e as envia para um broker na nuvem e depois para um software android. 
Messagens são enviados para a aplicação em tempo real permitindo o monitoramento e com isso evita que medicamentos possam ser perdidos, caso a temperatura e humidade fuja de padrões pré-estabelecidos. O custo de implantação e manutenção do sistema é consideravelmente menor que os custos com funcionários. 
