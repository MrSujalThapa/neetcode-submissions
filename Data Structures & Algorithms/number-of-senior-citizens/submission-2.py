class Solution:
    def countSeniors(self, details: List[str]) -> int:
        eligible = 0
        for detail in details:
            if (int(detail[11] + detail[12]) > 60):
                eligble += 1
        
        return eligible