<h1>Riot Games Data Analysis</h1>

<p>This repository contains tools and scripts for analyzing data related to Riot Games, particularly game statistics for the years 2020 and 2024.</p>

<h2>Requirements</h2>

<ul>
    <li>Python 3.x</li>
    <li>Pandas</li>
    <li>Matplotlib</li>
    <li>Seaborn</li>
    <li>MySQL</li>
</ul>

<h2>Getting Started</h2>

<p>Before running any scripts, ensure you have the required Python libraries installed. You can install them using pip:</p>

<pre><code>pip install pandas matplotlib seaborn mysql-connector-python</code></pre>

<h2>Data Sources</h2>

<p>The data is sourced from two CSV files:</p>

<ul>
    <li><strong>gamestats_2020.csv</strong>: Game statistics for the year 2020</li>
    <li><strong>gamestats_2024.csv</strong>: Game statistics for the year 2024</li>
</ul>

<h2>Features</h2>

<h3>Data Cleaning</h3>

<p>Various data cleaning operations were performed:</p>

<ul>
    <li>Removing unwanted columns</li>
    <li>Handling missing values</li>
</ul>

<h3>Data Analysis</h3>

<p>Statistical analysis was performed to:</p>

<ul>
    <li>Calculate average values for each column</li>
    <li>Compare statistics between the years 2020 and 2024</li>
    <li>Visualize the comparison using bar plots</li>
</ul>

<h3>Database Operations</h3>

<p>Data was stored and retrieved from a MySQL database using Python.</p>

<h2>Usage</h2>

<p>Run the following scripts to perform the respective tasks:</p>

<pre><code>__main__.py</code></pre>

<h2>Contributing</h2>

<p>Feel free to contribute to this project by creating pull requests or opening issues.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
