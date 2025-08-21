class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = {}
        for email in emails:
            findA = email.find('@')
            email = email[:findA].replace('.', '') + email[findA:]
            findPlus = email.find('+')
            findA = email.find('@')
            if findPlus != -1 and findPlus < findA:
                email = email[:findPlus] + email[findA:]
            if email not in d:
                d[email] = 1
        return len(d)