class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified = []
        words = path.split("/")
        for i in range (len(words)):
            if simplified and words[i] == ".." and simplified[-1]!="/":
                simplified.pop()
                continue
            elif words[i] == "" or words[i] == "." or words[i]=="..":
                continue
            else:
                    simplified.append(words[i])
        s_path = "/".join(simplified)
        return "/"+s_path
        
            
        