object Solution {
    def maximumWealth(accounts: Array[Array[Int]]): Int = {
        accounts.maxBy(l => l.sum).sum
    }
}