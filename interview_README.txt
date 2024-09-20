Write a socket-server chat-server that accepts clients that connect to it over TCP. An example client would be netcat or telnet.

In order to start we will focus on creating an MVP version with the most basic functionality. As time permits we will have some follow-ups, so let's focus on getting the MVP running first:

Connect and disconnect with multiple client support and basic message forwarding:

The chat server should be capable of handling multiple clients connecting at the same time.
Disconnection should be handled in a clean way.
Should be able to receive and forward messages among clients (message is not echoed back to sender).
> yo
< whats up?
> Nothing much!!
< same here, hbu?
> same ol' same


Usernames and information

Now that we have a working chat server, let's make it more user-friendly.

Every client that connects should be prompted for a nickname, which will prefix their messages.
This nickname is case-sensitive and must be unique on the server.
If the nickname is already taken the server should ask the user to choose a new nickname.
The chat server should send a list of users connected to the new client as well as broadcast to everyone else that the new user has connected.
Upon disconnection the rest of the remaining clients should be notified.
< Welcome to my chat server! What is your nickname?
> Julia
< You are connected with 3 other users: [stan, prachi, mike]
< *Julia has joined the chat*
> Hey whats going on guys?
< <stan> Nothing much!!
< *Julia has left the chat* 
