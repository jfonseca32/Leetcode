<h2><a href="https://leetcode.com/problems/integer-to-roman/">12. Integer to Roman</a></h2>
<h3>Medium</h3>
<hr>
<div>
<p>Seven different symbols represent Roman numerals with the following values:</p>

<table>
    <thead>
        <tr>
            <th>Symbol</th>
            <th>Value</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><code>I</code></td><td>1</td></tr>
        <tr><td><code>V</code></td><td>5</td></tr>
        <tr><td><code>X</code></td><td>10</td></tr>
        <tr><td><code>L</code></td><td>50</td></tr>
        <tr><td><code>C</code></td><td>100</td></tr>
        <tr><td><code>D</code></td><td>500</td></tr>
        <tr><td><code>M</code></td><td>1000</td></tr>
    </tbody>
</table>

<p>Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:</p>

<ul>
    <li>If the value does not start with <code>4</code> or <code>9</code>, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and continue converting the remainder.</li>
    <li>If the value starts with <code>4</code> or <code>9</code>, use the <strong>subtractive form</strong>, representing one symbol subtracted from the following symbol. For example, <code>4</code> is <code>IV</code> and <code>9</code> is <code>IX</code>. The only subtractive forms are <code>IV</code>, <code>IX</code>, <code>XL</code>, <code>XC</code>, <code>CD</code>, and <code>CM</code>.</li>
    <li>Only powers of <code>10</code> (<code>I</code>, <code>X</code>, <code>C</code>, <code>M</code>) can be appended consecutively at most three times. Symbols representing <code>5</code>, <code>50</code>, and <code>500</code> (<code>V</code>, <code>L</code>, <code>D</code>) cannot be appended multiple times.</li>
</ul>

<p>Given an integer <code>num</code>, convert it to a Roman numeral.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num = 3749
<strong>Output:</strong> "MMMDCCXLIX"

<strong>Explanation:</strong>
3000 = MMM
700 = DCC
40 = XL
9 = IX </pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num = 58
<strong>Output:</strong> "LVIII"

<strong>Explanation:</strong>
50 = L
8 = VIII </pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> num = 1994
<strong>Output:</strong> "MCMXCIV"

<strong>Explanation:</strong>
1000 = M
900 = CM
90 = XC
4 = IV </pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= num &lt;= 3999</code></li>
</ul>
</div>
