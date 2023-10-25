# Disney-CYHI - OSINT
Notes from Disney's Global Information Security Can You Hack It Events

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
