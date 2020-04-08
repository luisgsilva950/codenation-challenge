import string


class AlphabetManager:
    def __init__(self):
        self.ALPHABET = string.ascii_lowercase[:]

    def getIndexLetter(self, letter):
        cont = 0
        for alphabetLetter in self.ALPHABET:
            if alphabetLetter != letter:
                cont = cont + 1
            else:
                return cont
        return cont
    def getAlphabetLetter(self, index):
        return self.ALPHABET[index]
    def notIsNumber(self, char):
        try:
            int(char)
            return False
        except:
            return True