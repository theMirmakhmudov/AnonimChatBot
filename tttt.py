import base64

# 1. Matnni base64 formatiga kodlash
input_text = input("Kirit: ")
encoded_text = base64.b64encode(input_text.encode('utf-8')).decode('utf-8')
print("Base64 kodlangan matn:", encoded_text)

# 2. Base64 formatidan matnni dekodlash
decoded_text = base64.b64decode(encoded_text).decode('utf-8')
print("Dekodlangan matn:", decoded_text)