class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # to get optimal solution we need to try and pair the heaviest person with the lightest person, if that falls in the limit, good move both pointers closer , else heavier person takes boat by himself 
        l = 0
        h = len(people)-1
        boat = 0
        while l <= h:
            remain = limit - people[h]
            boat+=1
            h-=1
            if l<=h and people[l]<=remain:
                l+=1
        return boat

        [1,2,2,3,3] , 3 , 1,1,