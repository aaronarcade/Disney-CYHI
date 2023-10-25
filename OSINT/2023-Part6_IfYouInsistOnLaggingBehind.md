# Disney-CYHI - OSINT
Notes from Disney's Global Information Security Can You Hack It Events

## Part 6: If You Insist on Lagging Behind, You May Not Need to Volunteer
### Prompt
None
### Process
* Go back to the encoded blurb in the Spotify playlist description: 6b 6b 6f 7c 90 7e 78 6b 6b 7a 90 60 6e 6a 6f 63 90 61 6a 61 7a 6f fe 6a 62 6f 67 62 90 6e 60 63 04 4d e7 45 46 75 7a 66 db 52 7d 6b 6f 62 e1 6e 67 67 62 62 cd 52 6c 61 63 6b e1 61 6e 7a 6b 7c c3 07
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/7bb41bf9-221f-41f9-8aa8-05210b7561e3)
* Use CyberChef to decode from hex and xor with the key 'from somewhere beyond'. Result is an email address and a flag
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/021dbb46-b060-4b9a-b55d-55fec4c9f647)
### Flag
CYHI{the_real_chills_come_later}
