
#!/usr/bin/env python3
"""
vowel_counter.py 
"""

__author__ = "Katie Sam"
__version__ = "2023-01-17"

class PalindromeChecker:
    def __init__(self):
        self.strict_mode = False

    def setStrictMode(self, m):
        self.strict_m= m

    def isPalindrome(self, phrase):
        if self.strict_m:
            return self.sanitize(phrase) == self.sanitize(phrase)[::-1]
        else:
            return phrase.lower() == phrase.lower()[::-1]

    def sanitize(self, phrase):
        return ''.join(c for c in phrase.lower() if c.isalnum())

def main():
    print("Palindrome Checker!")
    choice = input("Do you want strict mode 1) on, or 2) off? --> ")
    checker = PalindromeChecker()
    if choice == "2":
        checker.setStrictMode(False)
    elif choice== "1":
        checker.setStrictMode(True)
    else:
        print("Whoops!")
        return
        
    phrase = input("Phrase: ")
    if checker.isPalindrome(phrase):
        print("Is a palindrome.")
    else:
        print("Not a palindrome.")

if __name__ == "__main__":
    main()