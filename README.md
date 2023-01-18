# SYN_flood_python

SYN flood is a kind of DDoS attacking. Its theory is TCP has 3-ways-handshaking. When a device wants to connect to other device using TCP protocol, it will send a packet that its SYN flag is 1 to other device. After receiving it, the device will return a packet that its SYN and ACK flags are 1 to the device which wants to connect. Because of this, we can advantage this theory to attack a server or the other related devices. Following these steps:


1. Generate a "fake" ip address

2. Make a packet and set its source ip the "fake" ip address generated in step 2.

3. Set the packet's distination ip the ip address and the port you want to attack.

4. Send it.

After the device receiving your packet, it will send the packet that its SYN and ACK flags are 1. Because the source IP is fake, it can not receive the response. And the device will resend the packet again and again.
