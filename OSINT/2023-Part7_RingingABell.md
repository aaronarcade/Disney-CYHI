# Disney-CYHI - OSINT
Notes from Disney's Global Information Security Can You Hack It Events

## Part 7: Ringing a Bell
### Prompt
None
### Process
* Send an email to 'dear.sweet.madam.leota@gmail.com' with the subject line "Ringing a Bell" and you'll get back an automated email
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/869a52b6-e2f2-46ac-8bfb-91f68f67341a)
* The Base64 can be decoded in CyberChef aHR0cHM6Ly9zZWFuY2UuY2lyY2xlLmhhdW50ZWRtYW5zaW9uLmJvby9vaHplaXg0amlldGVpOVMvaGV4bW9qaS56aXAK
* Leads to a link: https://seance.circle.hauntedmansion.boo/ohzeix4jietei9S/hexmoji.zip
* Once unzipped, you'll find a file that has a bunch of hex code mixed with three emojis. Ghost = FF, Eyes = 00, Shocked Face = FE
* I first tried converting the existing hex to text and noticed that it looked like an image file but was missing some values in the header. I was able to quickly determine the Ghost and Eyes emoji hex values and then discovered the Shocked Face value by determining which hex value didn't exist in the file.
* Once converted from hex to text, you could save it as a JPG and open the file
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/d2f2628d-74a0-4631-9b45-3fac99cfef56)
### Flag
CYHI{spooky_scary_mojis}
