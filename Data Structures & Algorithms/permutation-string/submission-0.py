class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize=len(s1)
        toPerm={}
        winPerm={}
        l=0

        for i, ch in enumerate(s1):
            toPerm[ch]=1+toPerm.get(ch,0)
        
        for r, ch in enumerate(s2):
            
            if ((r-l+1)>windowSize):
                winPerm[s2[l]]-=1
                if winPerm[s2[l]] == 0:
                    del winPerm[s2[l]]
                l=l+1
                
            winPerm[ch]=1+winPerm.get(ch,0)

            if(winPerm==toPerm):
                return True

        return False

                
        




        