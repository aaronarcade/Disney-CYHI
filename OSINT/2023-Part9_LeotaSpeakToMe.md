# Disney-CYHI - OSINT
Notes from Disney's Global Information Security Can You Hack It Events

## Part 9: Leota, Speak to Me
### Prompt
None
### Process
* Send another email to 'dear.sweet.madam.leota@gmail.com' with the subject line "Leota, speak to me" and you'll get back an automated email
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/b9d38ada-bc9d-4710-ae59-d0c28012795e)
* The Base64 can be decoded in CyberChef aHR0cHM6Ly9zZWFuY2UuY2lyY2xlLmhhdW50ZWRtYW5zaW9uLmJvby9maUoyaGEybXVxdWVpMWhlaVg0L2hleC5kLnppcAoKCgoKCgoKCg==
* Leads to a link: [https://seance.circle.hauntedmansion.boo/ohzeix4jietei9S/hexmoji.zip](https://seance.circle.hauntedmansion.boo/fiJ2ha2muquei1heiX4/hex.d.zip)
* Once unzipped, you'll find a file (Hex.d.zip) that contains a hex encoded file. You'll need to decode the file from hex and change the header from '8950 4e47' (?PNG) to '6769 6D70' (gimp)
* If you open in a gimp editor (https://fixthephoto.com/online-gimp-editor.html), you'll find that the flag is hidden out of view on layer 4: Q1lISXtub193aW5kb3dzX2FuZF9ub19kb29yc30K
* Red Herring is located on layer 2: Q1lISXtZRUFIIFJJR0hUIERJRCBZT1UgUkVBTExZIFRISU5LIElUIFdPVUxEIEJFIFRIQVQgRUFTWT8/Pz8/fQ== -- CYHI{YEAH RIGHT DID YOU REALLY THINK IT WOULD BE THAT EASY?????}
### Flag
CYHI{no_windows_and_no_doors}
