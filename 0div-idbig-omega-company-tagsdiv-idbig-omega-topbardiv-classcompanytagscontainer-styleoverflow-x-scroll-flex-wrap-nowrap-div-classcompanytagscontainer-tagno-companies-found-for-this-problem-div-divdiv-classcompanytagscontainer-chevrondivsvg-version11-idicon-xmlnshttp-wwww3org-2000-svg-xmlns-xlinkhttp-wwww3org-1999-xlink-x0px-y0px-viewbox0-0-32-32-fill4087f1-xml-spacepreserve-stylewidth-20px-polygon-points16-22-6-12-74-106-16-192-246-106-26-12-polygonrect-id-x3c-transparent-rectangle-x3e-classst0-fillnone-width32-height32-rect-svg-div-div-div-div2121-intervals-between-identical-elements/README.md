<h2><a href="https://leetcode.com/problems/intervals-between-identical-elements/"><div id="big-omega-company-tags"><div id="big-omega-topbar"><div class="companyTagsContainer" style="overflow-x: scroll; flex-wrap: nowrap;"><div class="companyTagsContainer--tag">No companies found for this problem</div></div><div class="companyTagsContainer--chevron"><div><svg version="1.1" id="icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" fill="#4087F1" xml:space="preserve" style="width: 20px;"><polygon points="16,22 6,12 7.4,10.6 16,19.2 24.6,10.6 26,12 "></polygon><rect id="_x3C_Transparent_Rectangle_x3E_" class="st0" fill="none" width="32" height="32"></rect></svg></div></div></div></div>2121. Intervals Between Identical Elements</a></h2><h3>Medium</h3><hr><div><p>You are given a <strong>0-indexed</strong> array of <code>n</code> integers <code>arr</code>.</p>

<p>The <strong>interval</strong> between two elements in <code>arr</code> is defined as the <strong>absolute difference</strong> between their indices. More formally, the <strong>interval</strong> between <code>arr[i]</code> and <code>arr[j]</code> is <code>|i - j|</code>.</p>

<p>Return <em>an array</em> <code>intervals</code> <em>of length</em> <code>n</code> <em>where</em> <code>intervals[i]</code> <em>is <strong>the sum of intervals</strong> between </em><code>arr[i]</code><em> and each element in </em><code>arr</code><em> with the same value as </em><code>arr[i]</code><em>.</em></p>

<p><strong>Note:</strong> <code>|x|</code> is the absolute value of <code>x</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [2,1,3,1,2,3,3]
<strong>Output:</strong> [4,2,7,2,4,4,5]
<strong>Explanation:</strong>
- Index 0: Another 2 is found at index 4. |0 - 4| = 4
- Index 1: Another 1 is found at index 3. |1 - 3| = 2
- Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7
- Index 3: Another 1 is found at index 1. |3 - 1| = 2
- Index 4: Another 2 is found at index 0. |4 - 0| = 4
- Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4
- Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [10,5,10,10]
<strong>Output:</strong> [5,0,3,4]
<strong>Explanation:</strong>
- Index 0: Two more 10s are found at indices 2 and 3. |0 - 2| + |0 - 3| = 5
- Index 1: There is only one 5 in the array, so its sum of intervals to identical elements is 0.
- Index 2: Two more 10s are found at indices 0 and 3. |2 - 0| + |2 - 3| = 3
- Index 3: Two more 10s are found at indices 0 and 2. |3 - 0| + |3 - 2| = 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == arr.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>