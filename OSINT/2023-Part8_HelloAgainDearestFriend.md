# Disney-CYHI - OSINT
Notes from Disney's Global Information Security Can You Hack It Events

## Part 8: Hello Again, Dearest Friend
### Prompt
None
### Process
* Send another email to 'dear.sweet.madam.leota@gmail.com' with the subject line "Hello Again, Dearest Friend" and you'll get back an automated email
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/d49d34b8-9666-4959-88fa-886aaefaafe9)
* The Base64 can be decoded in CyberChef aHR0cHM6Ly9zZWFuY2UuY2lyY2xlLmhhdW50ZWRtYW5zaW9uLmJvby9vem9vY29oQzFLYWdoOUdpZTRQYWkvdmFsbGV5LnppcAo=
* Leads to a link: [https://seance.circle.hauntedmansion.boo/ohzeix4jietei9S/hexmoji.zip](https://seance.circle.hauntedmansion.boo/ozoocohC1Kagh9Gie4Pai/valley.zip)
* The file contains an audio file with a bunch of characters read off at the end: 435948497b72656d61696e5f736166656c795f7365617465645f776974685f796f75725f68616e64735f61726d735f666565745f616e645f6c6567735f696e736964657d
* Decoding from hex gives you the flag
### Flag
CYHI{remain_safely_seated_with_your_hands_arms_feet_and_legs_inside}
