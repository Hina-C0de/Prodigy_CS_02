 # **Pixel Manipulation for Image Encryption**

 This tool encrypts and decrypts images using a combination of bitwise XOR encryption and pixel swapping for enhanced security.
 ## Encrption process
 Bitwise XOR encryption: Each pixel value is modified using a random mask key generated from encryption key
 Pixel swapping: Pixels position swappend randomly based on encryption key
 Saving keys: Two files saved for decryption
           1.Pixel indices file (.npy) – Stores the pixel shuffle order.
           2.Mask file (_mask.npy) – Stores the XOR mask used in encryption.
## Decryption process
Restore pixel value and apply bitwise XOR operations

It ensures that without key and saved files, the image remains protected. 






