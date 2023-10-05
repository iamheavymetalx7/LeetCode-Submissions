<h2><a href="https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/"><div id="big-omega-company-tags"><div id="big-omega-topbar"><div class="companyTagsContainer" style="overflow-x: scroll; flex-wrap: nowrap;"><div class="companyTagsContainer--tag">No companies found for this problem</div></div><div class="companyTagsContainer--chevron"><div><svg version="1.1" id="icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" fill="#4087F1" xml:space="preserve" style="width: 20px;"><polygon points="16,22 6,12 7.4,10.6 16,19.2 24.6,10.6 26,12 "></polygon><rect id="_x3C_Transparent_Rectangle_x3E_" class="st0" fill="none" width="32" height="32"></rect></svg></div></div></div></div>2131. Longest Palindrome by Concatenating Two Letter Words</a></h2><h3>Medium</h3><hr><div><p>You are given an array of strings <code>words</code>. Each element of <code>words</code> consists of <strong>two</strong> lowercase English letters.</p>

<p>Create the <strong>longest possible palindrome</strong> by selecting some elements from <code>words</code> and concatenating them in <strong>any order</strong>. Each element can be selected <strong>at most once</strong>.</p>

<p>Return <em>the <strong>length</strong> of the longest palindrome that you can create</em>. If it is impossible to create any palindrome, return <code>0</code>.</p>

<p>A <strong>palindrome</strong> is a string that reads the same forward and backward.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["lc","cl","gg"]
<strong>Output:</strong> 6
<strong>Explanation:</strong> One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["ab","ty","yt","lc","cl","ab"]
<strong>Output:</strong> 8
<strong>Explanation:</strong> One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> words = ["cc","ll","xx"]
<strong>Output:</strong> 2
<strong>Explanation:</strong> One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>5</sup></code></li>
	<li><code>words[i].length == 2</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>
</div>