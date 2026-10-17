class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #local: skip dots - if hit + end
        #domain - everything is unique
        uniqueEmail = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.split("+")[0].replace(".", "")
            final = local_name + "@" + domain_name
            uniqueEmail.add(final)

        return len(uniqueEmail)
        
