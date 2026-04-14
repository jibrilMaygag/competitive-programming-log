from collections import defaultdict
def subdomainVisits(self, cpdomains):
        result=defaultdict(int)
        for full_domain in cpdomains:
            count,domains=full_domain.split(' ')
            count=int(count)
            domains=domains.split('.')
            for i in range(len(domains)):
                result[".".join(domains[i:])]+=count
        return [f"{value} {key}" for key,value in result.items()]