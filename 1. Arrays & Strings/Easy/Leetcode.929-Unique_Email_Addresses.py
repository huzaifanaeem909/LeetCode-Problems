"""
LeetCode-929: https://leetcode.com/problems/unique-email-addresses/
"""

# Time Complexity: O(n)
# Space Complexity: O(n)


# Method-1 (using Buildin Functions)


def numUniqueEmails(emails):
    # Initialize an empty set to store unique email addresses
    hashSet = set()

    # Iterate through each email in the provided list
    for e in emails:
        # Split the email into local and domain parts using the '@' character
        localName, domainName = e.split("@")

        # Remove everything after a '+' in the local name, as it's considered a comment
        localName = localName.split("+")[0]

        # Replace all '.' characters in the local name with an empty string
        localName = localName.replace(".", "")

        # Add the email address to the set, which automatically handles duplicates
        hashSet.add(localName + "@" + domainName)

    # Return the number of unique email addresses
    return len(hashSet)


emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com",
]

print(numUniqueEmails(emails))


# Method-2 (without using Buildin Functions)


def numUniqueEmails(emails):
    hashSet = set()

    for e in emails:
        i, localName = 0, ""

        while e[i] not in ["@", "+"]:
            if e[i] != ".":
                localName += e[i]
            i += 1

        while e[i] != "@":
            i += 1

        domainName = e[i + 1 :]
        hashSet.add((localName, domainName))

    return len(hashSet)


emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com",
    "a@leetcode.com",
    "b@leetcode.com",
    "c@leetcode.com",
]

print(numUniqueEmails(emails))
