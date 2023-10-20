# Disney-CYHI - OSINT
Notes from Disney's Global Information Security Can You Hack It Events

## 2023
## Part 1: Find Me and Read Me
### Prompt
Hint is the instagram url (www.instagram.com/random_disney_fan_96)
### Process
* Look through the Instagram photos until you see one that looks suspicious with a comment
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/e9b39a82-80c1-4de7-8147-56de77d258c7)
* Use Lunapic to unswirl the photo https://www4.lunapic.com/editor/?action=swirl
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/98d52ef9-58cb-4a74-b823-9249d365e804)
* Mirror the image to get Reddit username /u/leota_thomas
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/0acc94c0-a728-48df-8edc-d5fd5df2771e)
* Navigate to Reddit profile and decode bio from Base64 in CyberChef
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/d179d71b-76c9-4876-87a3-5b155afc16ae)
### Flag
CYHI{let_the_game_begin}


## Part 2: The Clock is Ticking
### Prompt
None
### Process
* Reddit profile has a TikTok QR code as the profile picture
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/a14b2061-cbb8-494f-ad42-15968cd4fcc1)
* Profile is deleted by the time of publishing this, but profile bio contained Base64 code: Q1lISXtmaW5kX2Ffd2F5X291dCF9Cg== and throw it into CyberChef
### Flag
CYHI{find_a_way_out!}


## Part 3: Do You Like Music
### Prompt
None
### Process
* Reddit profile has a Spotify link : https://open.spotify.com/something_here_is_missing/01yjawQ2Ewq4XJxx03wnDo?si=6a14f728f097428a
* The link doesn't work though, because you need to put "playlist" in instead of "something_here_is_missing"
* The flag is spelled out by the first letter of each song
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/0ea9b06a-6e84-49b4-ba28-af0ba587465c)
### Flag
CYHI{GHOSTS_LIKE_MUSIC}


## Part 4: Spinning Makes Me Dizzy
### Prompt
None
### Process
* Playlist image is a QR code that has been flipped horizontal and vertical
* I was able to scan this just fine with my phone's camera without these steps to pull up a flag on my phone
### Flag
CYHI{Horntoads_and_lizards_fiddle_and_strum}


## Part 5: Digging Deeper
### Prompt
None
### Process
* If you click on Leota Thomas's profile through the playlist, you'll notice that the account has one follower - hatbox g'host
* Click into hatbox g'host's playlist hatbox_tunez to see some encoded text in Base58: 5xdqbAE6G6JDPCy4gTcJk3MR5TnAHbmespV826difg5ix5gFMGjh6NfRu6mWMYMrhnKdorJbvvnc1ymPXGs8SaUo64ggUc4JG7KF6qf
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/e6ba20a2-6f43-4b7e-b252-7e2242551619)
* It appears to be Braille
![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/0ae13b2c-5883-416c-8701-a93e826afacc)
* Decode the Braille to find the flag:

![image](https://github.com/vbyerley/Disney-CYHI/assets/54579088/352e6ced-17c3-46b1-b8f8-5ff0b3824f20)
### Flag
CYHI{YOU_FOUND_THE_GHOST!}


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
