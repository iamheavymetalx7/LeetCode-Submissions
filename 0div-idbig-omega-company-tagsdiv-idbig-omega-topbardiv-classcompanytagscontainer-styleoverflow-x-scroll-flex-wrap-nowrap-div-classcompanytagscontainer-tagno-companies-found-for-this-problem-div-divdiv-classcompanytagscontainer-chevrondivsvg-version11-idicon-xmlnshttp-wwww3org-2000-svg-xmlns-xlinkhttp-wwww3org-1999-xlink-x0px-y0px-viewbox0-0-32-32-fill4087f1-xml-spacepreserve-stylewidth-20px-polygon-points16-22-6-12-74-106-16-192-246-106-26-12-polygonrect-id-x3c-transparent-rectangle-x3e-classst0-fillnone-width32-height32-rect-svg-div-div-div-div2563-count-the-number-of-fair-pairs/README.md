<h2><a href="https://leetcode.com/problems/count-the-number-of-fair-pairs/"><div id="big-omega-company-tags"><div id="big-omega-topbar"><div class="companyTagsContainer" style="overflow-x: scroll; flex-wrap: nowrap;"><div class="companyTagsContainer--tag">No companies found for this problem</div></div><div class="companyTagsContainer--chevron"><div><svg version="1.1" id="icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" fill="#4087F1" xml:space="preserve" style="width: 20px;"><polygon points="16,22 6,12 7.4,10.6 16,19.2 24.6,10.6 26,12 "></polygon><rect id="_x3C_Transparent_Rectangle_x3E_" class="st0" fill="none" width="32" height="32"></rect></svg></div></div></div></div>2563. Count the Number of Fair Pairs</a></h2><h3>Medium</h3><hr><div><p>Given a <strong>0-indexed</strong> integer array <code>nums</code> of size <code>n</code> and two integers <code>lower</code> and <code>upper</code>, return <em>the number of fair pairs</em>.</p>

<p>A pair <code>(i, j)</code> is <b>fair </b>if:</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; n</code>, and</li>
	<li><code>lower &lt;= nums[i] + nums[j] &lt;= upper</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,7,4,4,5], lower = 3, upper = 6
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,7,9,2,5], lower = 11, upper = 11
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is a single fair pair: (2,3).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums.length == n</code></li>
	<li><code><font face="monospace">-10<sup>9</sup></font>&nbsp;&lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code><font face="monospace">-10<sup>9</sup>&nbsp;&lt;= lower &lt;= upper &lt;= 10<sup>9</sup></font></code></li>
</ul>
</div>