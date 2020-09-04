# import string
# def create_cipher(msg, shift):
#   cipher = ''
#   string = list(string.ascii_lowercase[:14])
#   upside_down = string.reverse()
#   for letter in msg:
#     if upside_down in letter
  
# #   msg.each do |letter|
# #     if upside_down.include?(letter.downcase)
# #       shift.times {letter = letter.next}
# #     end
# #       cipher += letter[-1]
# #    end
# #    return cipher
# # end

# print("Por favor insira a mensagem: ")
# msg = gets.chomp.split(//)

# print("Por favor insira o número de troca: ")
# shift = gets.chomp.to_i

# puts create_cipher(msg, shift)

#A python program to illustrate Caesar Cipher Technique 
def encrypt(text,s): 
  result = "" 
  # traverse text 
  for i in range(len(text)): 
    char = text[i] 
    # Encrypt uppercase characters 
    if (char.isupper()): 
      result += chr((ord(char) + s-65) % 26 + 65) 
    # Encrypt lowercase characters 
    else: 
      result += chr((ord(char) + s - 97) % 26 + 97) 
  return result 

#check the above function 
text = str(input('Digite o texto que deseja encriptar: '))
s = int(input('Digite um número de 1 e 25 para a troca: ' ))

while s == 0 or s > 25:
  print('Por favor digite un número válido.')
  s = int(input('Digite um número de 1 e 25 para a troca: ' ))
  if s > 0 and s < 25:
    print ('Texto  : ',text) 
    print ('Troca : ',str(s))
    print ('Cifra: ',encrypt(text,s))