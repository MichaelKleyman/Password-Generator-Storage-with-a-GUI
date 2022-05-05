alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, direction_value):
  end_text = ""
  if direction_value == "decode":
    shift_amount *= -1
  if direction_value == "encode":
    shift_amount *= 1
  for char in start_text:
      if char in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
          end_text += char

 print(f"The {direction_value}d is {end_text}.")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    caesar(start_text=text, shift_amount=shift, direction_value=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if restart == "no":
        print("Goodbye.")
        should_continue = False






