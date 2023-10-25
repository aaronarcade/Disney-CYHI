# Disney-CYHI - OSINT
Notes from Disney's Global Information Security Can You Hack It Events

## Part 10: Oogies and Boogies, Come to Me Now
### Prompt
None
### Process
* Send another email to 'dear.sweet.madam.leota@gmail.com' with the subject line "Oogies and Boogies, Come to Me Now" and you'll get back an automated email
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/2a57fd15-5d53-4d99-9529-b8088fc3ebbc)
* The Base64 can be decoded in CyberChef aHR0cHM6Ly9zZWFuY2UuY2lyY2xlLmhhdW50ZWRtYW5zaW9uLmJvby9laXRlaTVvdmVlWi9mcm9nX2FuZF9waWcuemlwCg==
* Leads to a link: https://seance.circle.hauntedmansion.boo/eitei5oveeZ/frog_and_pig.zip
* Once unzipped, you'll find an image of Kermit and Ms. Piggie
* If you use exiftool (or open the file in a text editor), you'll find a comment of 'Not Easy Being Green'
* Use steghide to extract a file that is a reversed, hexed, zip archive (green.txt)
* Password for zip archive is the comment 'Not Easy being Green'
### Flag
CYHI{no_1_2_compare_with_moi}
