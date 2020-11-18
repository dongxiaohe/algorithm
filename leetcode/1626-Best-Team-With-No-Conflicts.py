class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = []
        for i in range(len(scores)):
            players.append((ages[i], scores[i]))
        players.sort(reverse = True)
        ans = 0
        dp = [0 for _ in range(len(players))]
        for i in range(len(players)):
            dp[i] = players[i][1]
            for j in range(i):
                if players[j][1] >= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
            ans = max(ans, dp[i])
        return ans
