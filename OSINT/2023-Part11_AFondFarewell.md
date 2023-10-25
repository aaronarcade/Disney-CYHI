# Disney-CYHI - OSINT
Notes from Disney's Global Information Security Can You Hack It Events

## Part 11: A Fond Farewell, Goodbye Friend
### Prompt
None
### Process
* Send another email to 'dear.sweet.madam.leota@gmail.com' with the subject line "A Fond Farewell, Goodbye Friend" and you'll get back an automated email
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/86482fd8-2881-41b5-867d-d128b505dcac)
* The Base64 can be decoded in CyberChef aHR0cHM6Ly9zZWFuY2UuY2lyY2xlLmhhdW50ZWRtYW5zaW9uLmJvby9VbG9vbmVpemlpcXU4ZWVmZWVjaG9vZmFldC85OTlfSGFwcHlfSGF1bnRzLnppcA==
* Leads to a link: [https://seance.circle.hauntedmansion.boo/Ulooneiziiqu8eefeechoofaet/999_Happy_Haunts.zip](https://seance.circle.hauntedmansion.boo/Ulooneiziiqu8eefeechoofaet/999_Happy_Haunts.zip)
* Note: I didn't get this far in the challenge, so I do not have the file. 
* The archive contains 999 randomized images, one of which contains a b64 encoded flag
* Flag is a b64 string on image ghost_820.jpg: Q1lISXt3ZWxjb21lX2hvbWVfZ2hvc3RfI18xMDAwIX0=
### Flag
CYHI{welcome_home_ghost_#_1000!}
