<h2><a href="https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/"><div id="big-omega-company-tags"><div id="big-omega-topbar"><div class="companyTagsContainer" style="overflow-x: scroll; flex-wrap: nowrap;"><div class="companyTagsContainer--tag">No companies found for this problem</div></div><div class="companyTagsContainer--chevron"><div><svg version="1.1" id="icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" fill="#4087F1" xml:space="preserve" style="width: 20px;"><polygon points="16,22 6,12 7.4,10.6 16,19.2 24.6,10.6 26,12 "></polygon><rect id="_x3C_Transparent_Rectangle_x3E_" class="st0" fill="none" width="32" height="32"></rect></svg></div></div></div></div>2556. Disconnect Path in a Binary Matrix by at Most One Flip</a></h2><h3>Medium</h3><hr><div><p>You are given a <strong>0-indexed</strong> <code>m x n</code> <strong>binary</strong> matrix <code>grid</code>. You can move from a cell <code>(row, col)</code> to any of the cells <code>(row + 1, col)</code> or <code>(row, col + 1)</code> that has the value <code>1</code>.&nbsp;The matrix is <strong>disconnected</strong> if there is no path from <code>(0, 0)</code> to <code>(m - 1, n - 1)</code>.</p>

<p>You can flip the value of <strong>at most one</strong> (possibly none) cell. You <strong>cannot flip</strong> the cells <code>(0, 0)</code> and <code>(m - 1, n - 1)</code>.</p>

<p>Return <code>true</code> <em>if it is possible to make the matrix disconnect or </em><code>false</code><em> otherwise</em>.</p>

<p><strong>Note</strong> that flipping a cell changes its value from <code>0</code> to <code>1</code> or from <code>1</code> to <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/12/07/yetgrid2drawio.png" style="width: 441px; height: 151px;">
<pre><strong>Input:</strong> grid = [[1,1,1],[1,0,0],[1,1,1]]
<strong>Output:</strong> true
<strong>Explanation:</strong> We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/12/07/yetgrid3drawio.png">
<pre><strong>Input:</strong> grid = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li><code>grid[0][0] == grid[m - 1][n - 1] == 1</code></li>
</ul>
</div>