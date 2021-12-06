## Integrated Snipe + ACL
This tool has the both the components integrated into it. Once in the root directory of the repo, just run -

$python3 integrated_snipe+ACL/main.py

Then you can either choose to snipe packets, or if thats already done, you can choose to run the ACL inference tool.
The options within the runtime are self explanatory. More details on the individual components can be found below.

## Inference with Wireshark Integration
This tool is designed to run in background, sniffing and analyzing MQTT related packets over the internet. 

The inputs needed by this program is just the time to sniff packets (in seconds). 

The result of this program will be the complete list of obtained username, paswords and the respective topics. (Only the successfully connected requests). 

## ACL Infer Tool
  This tool is designed to allow a user to determine what topics they have access to on an MQTT system. To do so, the user needs to supply the following inputs to the program:
  
  -i: Specify input file of topics. Each topic should be on a new line.
  
  -H : Specify MQTT hostname.
  
  -u : Specify MQTT username.
  
  -p : Specify MQTT password.
  
  The last two items can be obtained legitimately, or found as an attacker with the Wireshark integration discussed later. Of course, an attacker could also use other attacks to obtain a username and password.
  
  With these inputs, the tool will first check the supplied list of topics, then continue listening on all topics. The user can leave the program running for as long as desired to gather additional topics. When finished, use ctrl + c to exit the program. If you would like to save the output of the program, redirect it to the file of your choice. 

## ACL Information Flow/ACL checker
  This tool allows one to check access control rules based on a Biba-like, integrity focused policy. To use the tool, the user must edit the ACL file to include a permission of 'high' or 'low' after each user. Then, simple run the tool with the edited ACL file, and the tool will check for violations on all topics in the ACL. The only input is:
  
  -i: Specify input file, the edited ACL.
  
  The policy follows the "read up, write down" of Biba. If there is a topic with high and low users, the read/write permissions are checked. The low user cannot have the read or readwrite permissions, since these would constitute "write ups." This also covers the case of "read down"- if a low user writes to a topic and the high user reads, a read down has occured. Essentially, the allowed case is when a low user can read on a topic where a high user writes. This protects the integrity of the data, which is the goal of the model.
  

