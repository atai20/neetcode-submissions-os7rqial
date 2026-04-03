class Solution:

    # ["a","b"] encode function will give "a#b"

    '''
    encode:
        loop through array;
            add character from array to string;
            add special dividing character;
        return the string;

    decode:
        resulting array = empty array
        word = empty string
        loop through string;
            if character not is special:
                add character to a word
            else:
                append word to resulting array
                word = emtpy string
        return resulting array
    
    '''


    ''' 
    encode(["Hello","World"])
        encoded_word = ""
        "Hello"
        "Hello🚀"
        "Hello🚀World🚀"

    decode("Hello🚀World🚀")
        resulting_array = []
        decode_word = ""
        decode_word = "Hello"
        resulting_array = ["Hello"]
        decode_word = ""
        decode_word = "World"
        resulting_array = ["Hello", "World"]
        decode_word = ""
    
    '''
    def encode(self, strs: List[str]) -> str:
        encoded_word = ""
        for word in strs:
            encoded_word += word
            encoded_word += '🚀'
        return encoded_word


    def decode(self, s: str) -> List[str]:
        resulting_array = []
        decode_word = ""
        for letter in s:
            if letter != '🚀':
                decode_word += letter
            else:
                resulting_array.append(decode_word)
                decode_word = ""
        return resulting_array


