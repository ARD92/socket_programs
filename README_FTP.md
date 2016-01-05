# socket_programs
This is a server client file transfer program using python

The server holds a list of clients for which it accepts the incoming file. once the file is received , it displays the 
time taken for the file to be received.

The client program prompts for the path of the file to be transmitted. once the path is entered it calculates the file size 
and proceeds by checking if it is a valid client( i.e. if the client is present in the list that the server can accept files 
from. if yes it prompts if we wish to transmit the file, by agreeing we transmit the file from the client to the server.
client also displays the time taken for the file to get transmitted.
