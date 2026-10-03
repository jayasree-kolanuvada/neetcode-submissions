class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # to get optimal solution we need to try and pair the heaviest person with the lightest person, if that falls in the limit, good move both pointers closer , else heavier person takes boat by himself 
        l = 0
        h = len(people)-1
        boat = 0
        while l <= h:
            if l!=h:
                wt = people[l]+people[h]
            else:
                wt = people[l]
            if wt <= limit:
                boat+=1
                l+=1
                h-=1
            else:
                boat+=1
                h-=1
        return boat

        [1,2,2,3,3] , 3 , 1,1,