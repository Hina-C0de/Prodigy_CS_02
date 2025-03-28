import cv2
import numpy as np

def swap_pixels(image, key):
    np.random.seed(key)
    indices = np.arange(image.size // image.shape[2])
    np.random.shuffle(indices)
    
    flat_image = image.reshape(-1, image.shape[2])
    shuffled_image = flat_image[indices].reshape(image.shape)
    return shuffled_image, indices

def restore_pixels(image, key, indices):
    np.random.seed(key)
    original_indices = np.argsort(indices)
    flat_image = image.reshape(-1, image.shape[2])
    restored_image = flat_image[original_indices].reshape(image.shape)
    return restored_image

def encrypt_image(image_path, key, output_path):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        raise ValueError("Could not open or find the image")
    
    np.random.seed(key)
    random_mask = np.random.randint(0, 256, image.shape, dtype=np.uint8)
    encrypted_image = cv2.bitwise_xor(image, random_mask)
    encrypted_image, indices = swap_pixels(encrypted_image, key)
    
    np.save(output_path + ".npy", indices)  # Save pixel order for decryption
    np.save(output_path + "_mask.npy", random_mask)  # Save mask for decryption
    cv2.imwrite(output_path, encrypted_image)
    print(f"Encrypted image saved to {output_path} and keys saved.")

def decrypt_image(encrypted_path, key, indices_path, mask_path, output_path):
    encrypted_image = cv2.imread(encrypted_path, cv2.IMREAD_UNCHANGED)
    if encrypted_image is None:
        raise ValueError("Could not open or find the encrypted image")
    
    indices = np.load(indices_path)
    random_mask = np.load(mask_path)
    decrypted_image = restore_pixels(encrypted_image, key, indices)
    decrypted_image = cv2.bitwise_xor(decrypted_image, random_mask)
    
    cv2.imwrite(output_path, decrypted_image)
    print(f"Decrypted image saved to {output_path}")

if __name__ == "__main__":
    mode = input("Enter mode (encrypt/decrypt): ")
    input_path = input("Enter input image path: ")
    key = int(input("Enter encryption key (integer): "))
    output_path = input("Enter output image path: ")
    
    if mode == "encrypt":
        encrypt_image(input_path, key, output_path)
    elif mode == "decrypt":
        indices_path = input("Enter path to the saved indices file (.npy): ")
        mask_path = input("Enter path to the saved mask file (.npy): ")
        decrypt_image(input_path, key, indices_path, mask_path, output_path)
    else:
        print("Invalid mode. Choose 'encrypt' or 'decrypt'.")
