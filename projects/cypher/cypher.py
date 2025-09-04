# Coded Correspondence: Cryptography Project

import string

print("=== CODED CORRESPONDENCE PROJECT ===")
print("Decoding and encoding messages with Caesar and Vigenère ciphers")
print()

# TASK 1: Decode Vishal's first Caesar cipher message
print("=== TASK 1: DECODING FIRST CAESAR CIPHER ===")

def caesar_decode(message, offset):
    """Decode a message using Caesar cipher with given offset"""
    decoded = ""
    for char in message:
        if char.isalpha():
            # Get the position in alphabet (a=0, b=1, etc.)
            char_pos = ord(char.lower()) - ord('a')
            # Shift by offset (add for decoding since encoding subtracts)
            new_pos = (char_pos + offset) % 26
            # Convert back to character
            new_char = chr(new_pos + ord('a'))
            decoded += new_char
        else:
            # Keep non-alphabetic characters unchanged
            decoded += char
    return decoded

def caesar_encode(message, offset):
    """Encode a message using Caesar cipher with given offset"""
    encoded = ""
    for char in message:
        if char.isalpha():
            # Get the position in alphabet (a=0, b=1, etc.)
            char_pos = ord(char.lower()) - ord('a')
            # Shift by offset (subtract for encoding)
            new_pos = (char_pos - offset) % 26
            # Convert back to character
            new_char = chr(new_pos + ord('a'))
            encoded += new_char
        else:
            # Keep non-alphabetic characters unchanged
            encoded += char
    return encoded

# Vishal's first encoded message
first_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
offset_1 = 10

decoded_message_1 = caesar_decode(first_message, offset_1)
print(f"Encoded message: {first_message}")
print(f"Offset: {offset_1}")
print(f"Decoded message: {decoded_message_1}")
print()

# TASK 2: Send a message back to Vishal
print("=== TASK 2: ENCODING A REPLY MESSAGE ===")

my_message = "hello vishal! this cipher is really cool. i love cryptography and cant wait to learn more!"
encoded_reply = caesar_encode(my_message, offset_1)

print(f"My message: {my_message}")
print(f"Encoded reply: {encoded_reply}")
print(f"Verification (decoding my encoded message): {caesar_decode(encoded_reply, offset_1)}")
print()

# TASK 3: Decode Vishal's two new messages
print("=== TASK 3: DECODING TWO NEW MESSAGES ===")

# First message (offset 10)
second_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
decoded_message_2 = caesar_decode(second_message, 10)

print(f"Second message: {second_message}")
print(f"Decoded: {decoded_message_2}")
print()

# Second message (offset from first message's hint)
third_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
offset_3 = 14  # "fourteen" from the decoded hint
decoded_message_3 = caesar_decode(third_message, offset_3)

print(f"Third message: {third_message}")
print(f"Offset from hint: {offset_3}")
print(f"Decoded: {decoded_message_3}")
print()

# TASK 4: Brute force decode without knowing the offset
print("=== TASK 4: BRUTE FORCE DECODING ===")

def brute_force_caesar(message):
    """Try all possible offsets to decode a Caesar cipher"""
    print("Trying all possible offsets:")
    for offset in range(26):
        decoded = caesar_decode(message, offset)
        print(f"Offset {offset:2d}: {decoded}")
        # Look for common English words to identify correct decoding
        if 'the' in decoded and 'and' in decoded:
            return decoded, offset
    return None, None

mystery_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

print(f"Mystery message: {mystery_message}")
print()
decoded_mystery, correct_offset = brute_force_caesar(mystery_message)

print(f"\nMost likely decoding (offset {correct_offset}): {decoded_mystery}")
print()

# TASK 5: Implement Vigenère cipher decoder
print("=== TASK 5: VIGENÈRE CIPHER DECODING ===")

def vigenere_decode(message, keyword):
    """Decode a message using Vigenère cipher with given keyword"""
    decoded = ""
    keyword_repeated = ""
    
    # Create keyword phrase by repeating keyword to match message length
    keyword_index = 0
    for char in message:
        if char.isalpha():
            keyword_repeated += keyword[keyword_index % len(keyword)]
            keyword_index += 1
        else:
            keyword_repeated += char
    
    # Decode each character
    for i, char in enumerate(message):
        if char.isalpha():
            # Get positions in alphabet
            char_pos = ord(char.lower()) - ord('a')
            key_pos = ord(keyword_repeated[i].lower()) - ord('a')
            # Subtract keyword position for decoding
            new_pos = (char_pos - key_pos) % 26
            new_char = chr(new_pos + ord('a'))
            decoded += new_char
        else:
            decoded += char
    
    return decoded

def vigenere_encode(message, keyword):
    """Encode a message using Vigenère cipher with given keyword"""
    encoded = ""
    keyword_repeated = ""
    
    # Create keyword phrase by repeating keyword to match message length
    keyword_index = 0
    for char in message:
        if char.isalpha():
            keyword_repeated += keyword[keyword_index % len(keyword)]
            keyword_index += 1
        else:
            keyword_repeated += char
    
    # Encode each character
    for i, char in enumerate(message):
        if char.isalpha():
            # Get positions in alphabet
            char_pos = ord(char.lower()) - ord('a')
            key_pos = ord(keyword_repeated[i].lower()) - ord('a')
            # Add keyword position for encoding
            new_pos = (char_pos + key_pos) % 26
            new_char = chr(new_pos + ord('a'))
            encoded += new_char
        else:
            encoded += char
    
    return encoded

# Vishal's Vigenère encoded message
vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
keyword = "friends"

decoded_vigenere = vigenere_decode(vigenere_message, keyword)

print(f"Vigenère message: {vigenere_message}")
print(f"Keyword: {keyword}")
print(f"Decoded message: {decoded_vigenere}")
print()

# TASK 6: Create Vigenère encoder and send a message
print("=== TASK 6: ENCODING WITH VIGENÈRE CIPHER ===")

my_vigenere_message = "thanks for teaching me about ciphers vishal! this has been so much fun to learn!"
my_keyword = "python"

encoded_vigenere_message = vigenere_encode(my_vigenere_message, my_keyword)

print(f"My message: {my_vigenere_message}")
print(f"My keyword: {my_keyword}")
print(f"Encoded message: {encoded_vigenere_message}")

# Bonus: Verify by decoding
verification = vigenere_decode(encoded_vigenere_message, my_keyword)
print(f"Verification (decoding): {verification}")
print(f"Encoding/decoding successful: {verification == my_vigenere_message}")
print()

# TASK 7: Summary and demonstration
print("=== TASK 7: PROJECT SUMMARY ===")
print("Successfully completed cryptography project!")
print()
print("Skills demonstrated:")
print("✓ Caesar cipher decoding and encoding")
print("✓ Brute force cryptanalysis")
print("✓ Vigenère cipher implementation")
print("✓ String manipulation and character operations")
print("✓ Modular arithmetic for alphabet wrapping")
print()

# Additional demonstration: Show both ciphers working
print("=== CIPHER COMPARISON DEMONSTRATION ===")

test_message = "meet me at midnight"
caesar_offset = 5
vigenere_key = "secret"

print(f"Original message: '{test_message}'")
print()

# Caesar cipher
caesar_encoded = caesar_encode(test_message, caesar_offset)
caesar_decoded = caesar_decode(caesar_encoded, caesar_offset)
print(f"Caesar cipher (offset {caesar_offset}):")
print(f"  Encoded: '{caesar_encoded}'")
print(f"  Decoded: '{caesar_decoded}'")
print()

# Vigenère cipher
vigenere_encoded = vigenere_encode(test_message, vigenere_key)
vigenere_decoded = vigenere_decode(vigenere_encoded, vigenere_key)
print(f"Vigenère cipher (keyword '{vigenere_key}'):")
print(f"  Encoded: '{vigenere_encoded}'")
print(f"  Decoded: '{vigenere_decoded}'")
print()

print("Both ciphers successfully implemented and verified!")
print("The Vigenère cipher is more secure because it uses different shifts for each letter.")
print("Project complete!")
