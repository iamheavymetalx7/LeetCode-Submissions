<h2><a href="https://leetcode.com/problems/find-the-divisibility-array-of-a-string/"><div id="big-omega-company-tags"><div id="big-omega-topbar"><div class="companyTagsContainer" style="overflow-x: scroll; flex-wrap: nowrap;"><div class="companyTagsContainer--tag">No companies found for this problem</div></div><div class="companyTagsContainer--chevron"><div><svg version="1.1" id="icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" fill="#4087F1" xml:space="preserve" style="width: 20px;"><polygon points="16,22 6,12 7.4,10.6 16,19.2 24.6,10.6 26,12 "></polygon><rect id="_x3C_Transparent_Rectangle_x3E_" class="st0" fill="none" width="32" height="32"></rect></svg></div></div></div></div>2575. Find the Divisibility Array of a String</a></h2><h3>Medium</h3><hr><div><p>You are given a <strong>0-indexed</strong> string <code>word</code> of length <code>n</code>&nbsp;consisting of digits, and a positive integer&nbsp;<code>m</code>.</p>

<p>The <strong>divisibility array</strong> <code>div</code> of <code>word</code> is an integer array of length <code>n</code> such that:</p>

<ul>
	<li><code>div[i] = 1</code> if the&nbsp;<strong>numeric value</strong>&nbsp;of&nbsp;<code>word[0,...,i]</code> is divisible by <code>m</code>, or</li>
	<li><code>div[i] = 0</code> otherwise.</li>
</ul>

<p>Return<em> the divisibility array of</em><em> </em><code>word</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> word = "998244353", m = 3
<strong>Output:</strong> [1,1,0,0,0,1,1,0,0]
<strong>Explanation:</strong> There are only 4 prefixes that are divisible by 3: "9", "99", "998244", and "9982443".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> word = "1010", m = 10
<strong>Output:</strong> [0,1,0,1]
<strong>Explanation:</strong> There are only 2 prefixes that are divisible by 10: "10", and "1010".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code><font face="monospace">word.length == n</font></code></li>
	<li><code><font face="monospace">word</font></code><font face="monospace"> consists of digits from <code>0</code>&nbsp;to <code>9</code></font></li>
	<li><code><font face="monospace">1 &lt;= m &lt;= 10<sup>9</sup></font></code></li>
</ul>
</div>