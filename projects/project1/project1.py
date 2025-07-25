from collections import Counter
import string

ciphertext = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi 
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx 
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr 
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk 
lmird jk xjubt trmui jx ibndt 
wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi 
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m 
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd 
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr 
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii 
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh 
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb 
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd 
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr 
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""

# letter_frequency Function to compute the letters  frequency
def letter_frequency(text):
    text = text.replace(" ", "").replace("\n", "")
    frequency = Counter(text)
    total_letters = sum(frequency.values())  
    return {char: round(count / total_letters, 4) for char, count in frequency.items()}

cipher_freq = letter_frequency(ciphertext)

english_freq_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

print("\nCiphertext letter frequencies:")
for k, v in sorted(cipher_freq.items(), key=lambda x: -x[1]):
    print(f"{k}: {v}")


def decrypt_with_mapping(text, mapping):
    result = ''
    for char in text:
        if char.upper() in mapping:
            result += mapping[char.upper()].lower() if char.islower() else mapping[char.upper()]
        else:
            result += char
    return result






Frequency_mapping  = { # for manually substituiton based on frequency results # each ones with a comment is a correct substitution
    'R': 'E', # correct
    'B': 'T', # correct
    'M': 'A', # correct 
    'K': 'O',
    'J': 'I',
    'W': 'N',
    'I': 'S',
    'P': 'H', # correct
    'Z': 'Z',
    'U': 'R', # correct
    'D': 'D',
    'H': 'L',
    'V': 'C', # correct
    'X': 'U',
    'Y': 'M', # correct
    'N': 'W',
    'S': 'F',
    'T': 'G',
    'L': 'Y',
    'Q': 'P',
    'O': 'B',
    'E': 'V',
    'A': 'K',
    'C': 'J',
    'F': 'X',
    'G': 'Q'
}

refined_mapping = {
    'R': 'E', #
    'M': 'A', #
    'V': 'C', #
    'P': 'H', #
    'B': 'T', #
    'Y': 'M', #
    'I': 'S', #
    'H': 'L', #
    'U': 'R', #
    'D': 'D', # K was D, Seems D was correct
    'K': 'N', # N was O
    'J': 'O', # O was I 
    'W': 'I', # I was N 
    'X': 'F', # W was U, F was W
    'N': 'U', # U was W
    'S': 'P', # P was F
    'T': 'Y', # Y was G
    'L': 'B', # B was Y
    'Q': 'K', # K was P, 
    'O': 'G', # G was B
    'E': 'V', # correct
    'A': 'X', # X was K
    'C': 'W', # W was J
    'F': 'Q', # Q was X
    'G': 'Z' # Z was Q
}

{'J', 'X',}





# Decrypt the message using the frequency mapping
print("\nDecrypted Message:")
decrypted_text = decrypt_with_mapping(ciphertext, refined_mapping)
print(decrypted_text)

# ignore this print ("\nPlease don't take this as a perfect decryption, it's based on frequency analysis and manual substitution.") 
print("\nAfter manual substitution, the decrypted message was found ")