class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        def dictionary(words):
            order = {}
            for i in range(len(words)-1):
                j=0
                while j<min(len(words[i]),len(words[i+1])) and words[i][j]==words[i+1][j]:
                    j+=1
                if j==min(len(words[i]),len(words[i+1])):
                    continue
                if words[i][j] not in order:
                    order[words[i][j]] = [words[i+1][j]]
                else:
                    order[words[i][j]].append(words[i+1][j])
            return order
        
        def word_list(words):
            lst = []
            flag = True
            for x in words:
                if len(x)>1:
                    flag=False
                for l in x:
                    if l not in lst:
                        lst.append(l)
            return lst,flag
        lst,flag = word_list(words)
        adj  = dictionary(words)
        if len(lst)==1 and flag:
            return lst[0]
        if adj=={}:
            return ''
        for l in lst:
            if l not in adj:
                adj[l] = []
        ans = ''
        visited = set()
        for l in lst:
            stack = []
            if l not in visited:
                stack.append(l)
            while stack:
                node = stack.pop()
                if node not in visited:
                    ans = ans+node
                visited.add(node)
                for neigh in adj[node]:
                    if neigh not in visited:
                        stack.append(neigh)
        return ans

            
            
        