"""Unit 3 - Q1: String Operations and String Methods"""

sentence = input("Enter a sentence: ")

print("\n1. Length of string       :", len(sentence))
print("2. Uppercase              :", sentence.upper())
print("   Lowercase              :", sentence.lower())
print("3. After strip()          :", repr(sentence.strip()))

old = input("\nEnter the word to replace: ")
new = input("Enter the new word: ")
print("4. After replace          :", sentence.replace(old, new))

ch = input("\nEnter a character to count: ")
print(f"5. Occurrences of '{ch}'    :", sentence.count(ch))

start = input("\nEnter a substring to check at the start: ")
end = input("Enter a substring to check at the end: ")
print(f"6. Starts with '{start}'  :", sentence.strip().startswith(start))
print(f"   Ends with '{end}'      :", sentence.strip().endswith(end))

print("\n7. Concatenation, repetition and membership")
s1, s2 = "Hello", "Python"
print("   Concatenation :", s1 + " " + s2)
print("   Repetition    :", s1 * 3)
print(f"   'Py' in '{s2}'      :", "Py" in s2)
print(f"   'Java' not in '{s2}':", "Java" not in s2)
print(f"   '{old}' in your sentence:", old in sentence)
