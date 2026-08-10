<h2><a href="https://leetcode.com/problems/container-with-most-water/">11. Container With Most Water</a></h2>
<h3>Medium</h3>
<hr>
<div>
<p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p>Return the maximum amount of water a container can store.</p>

<p>Notice that you may not slant the container.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The maximum area is formed between the lines at indices 1 and 8.
The width is 7 and the limiting height is 7, giving an area of 7 × 7 = 49.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
    <li><code>n == height.length</code></li>
    <li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
    <li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>
