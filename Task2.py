from PIL import Image
import os


ENCRYPTION_KEY = 50

def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    encrypted_img = img.copy()
    pixels = encrypted_img.load()

    for i in range(encrypted_img.size[0]):  
        for j in range(encrypted_img.size[1]):  
            r, g, b = pixels[i, j]
            
            pixels[i, j] = (
                (r + ENCRYPTION_KEY) % 256,
                (g + ENCRYPTION_KEY) % 256,
                (b + ENCRYPTION_KEY) % 256
            )
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path):
    img = Image.open(input_path)
    decrypted_img = img.copy()
    pixels = decrypted_img.load()

    for i in range(decrypted_img.size[0]): 
        for j in range(decrypted_img.size[1]):  
            r, g, b = pixels[i, j]
            
            pixels[i, j] = (
                (r - ENCRYPTION_KEY) % 256,
                (g - ENCRYPTION_KEY) % 256,
                (b - ENCRYPTION_KEY) % 256
            )
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")


if __name__ == "__main__":
    original = "https://www.google.com/imgres?q=images&imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F414612%2Fpexels-photo-414612.jpeg%3Fcs%3Dsrgb%26dl%3Dpexels-souvenirpixels-414612.jpg%26fm%3Djpg&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fbeautiful%2F&docid=B51x0PBR9KNzvM&tbnid=oXTudgfT3pqXSM&vet=12ahUKEwjhl_z4hK-NAxWYa_UHHcY1GFEQM3oECGUQAA..i&w=5306&h=3770&hcb=2&ved=2ahUKEwjhl_z4hK-NAxWYa_UHHcY1GFEQM3oECGUQAA"
    encrypted = "https://pngtree.com/so/encryption"
    decrypted = "https://www.freepik.com/icons/decrypt"

    
    encrypt_image(original, encrypted)

   
    decrypt_image(encrypted, decrypted)
