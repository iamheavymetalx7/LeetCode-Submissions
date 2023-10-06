<h2><a href="https://leetcode.com/problems/longest-subsequence-repeated-k-times/"><div id="big-omega-company-tags"><div id="big-omega-topbar"><div class="companyTagsContainer" style="overflow-x: scroll; flex-wrap: nowrap;"><div class="companyTagsContainer--tag">No companies found for this problem</div></div><div class="companyTagsContainer--chevron"><div><svg version="1.1" id="icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" fill="#4087F1" xml:space="preserve" style="width: 20px;"><polygon points="16,22 6,12 7.4,10.6 16,19.2 24.6,10.6 26,12 "></polygon><rect id="_x3C_Transparent_Rectangle_x3E_" class="st0" fill="none" width="32" height="32"></rect></svg></div></div></div></div>2014. Longest Subsequence Repeated k Times</a></h2><h3>Hard</h3><hr><div><p>You are given a string <code>s</code> of length <code>n</code>, and an integer <code>k</code>. You are tasked to find the <strong>longest subsequence repeated</strong> <code>k</code> times in string <code>s</code>.</p>

<p>A <strong>subsequence</strong> is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.</p>

<p>A subsequence <code>seq</code> is <strong>repeated</strong> <code>k</code> times in the string <code>s</code> if <code>seq * k</code> is a subsequence of <code>s</code>, where <code>seq * k</code> represents a string constructed by concatenating <code>seq</code> <code>k</code> times.</p>

<ul>
	<li>For example, <code>"bba"</code> is repeated <code>2</code> times in the string <code>"bababcba"</code>, because the string <code>"bbabba"</code>, constructed by concatenating <code>"bba"</code> <code>2</code> times, is a subsequence of the string <code>"<strong><u>b</u></strong>a<strong><u>bab</u></strong>c<strong><u>ba</u></strong>"</code>.</li>
</ul>

<p>Return <em>the <strong>longest subsequence repeated</strong> </em><code>k</code><em> times in string </em><code>s</code><em>. If multiple such subsequences are found, return the <strong>lexicographically largest</strong> one. If there is no such subsequence, return an <strong>empty</strong> string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="example 1" src="https://assets.leetcode.com/uploads/2021/08/30/longest-subsequence-repeat-k-times.png" style="width: 457px; height: 99px;">
<pre><strong>Input:</strong> s = "letsleetcode", k = 2
<strong>Output:</strong> "let"
<strong>Explanation:</strong> There are two longest subsequences repeated 2 times: "let" and "ete".
"let" is the lexicographically largest one.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "bb", k = 2
<strong>Output:</strong> "b"
<strong>Explanation:</strong> The longest subsequence repeated 2 times is "b".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "ab", k = 2
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no subsequence repeated 2 times. Empty string is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == s.length</code></li>
	<li><code>2 &lt;= n, k &lt;= 2000</code></li>
	<li><code>2 &lt;= n &lt; k * 8</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>
</div>