# Image(Patch)Converter

<p>Simple commandline image patch converter and thumbnail maker that uses settings file and commandline arguments for extra functionality that I made to prepare a website's image gallery images quickly to the right format and to make all the required thumbnails and differently sized versions for lazy-loading/bandwith saving/different sized GUI elements</p>

<p>It can easily make separate Thumb, S/M/L file versions and change image filetype for all files in a folder non-destructively working with copies of the original</p>

<p>Also provides thumbnail, medium and large file size conservions, which are especially useful for platforms like WordPress</p>

<p>You can either use the following console parameters or the provided settings.json file to provide default values / extra functionality(custom non square resolutions) that are desired</p>

<p>This tiny program uses python's <a href="https://g.co/kgs/sX17oL">PIL (python image library)</a>, for the conversion and supports all the image formats it supports.</p>

<p> in the table below the | means you can use either command, and %name% syntax means you need to fill in this part by yourself with the appropriate number/text/path </p>
<table>
	<tr><td><code>-t | --thumb</code></td><td>Generates thumbnail file (default 150x150) with suffix _thumb</td></tr>
	<tr><td><code>-s | --small</code></td><td>Generates Small file (default 150x150) with suffix _s</td></tr>
	<tr><td><code>-m | --medium</code></td><td>Generates Medium file (default 300x300) with suffix _m</td></tr>
	<tr><td><code>-l | --large</code></td><td>Generates Large file (default 1024x1024) with suffix _l</td></tr>
	<tr><td><code>st:'%size%'</code></td><td>Define custom square size for thumbnail file</td></tr>
	<tr><td><code>ss:'%size%'</code></td><td>Define custom square size for small file</td></tr>
	<tr><td><code>sm:'%size%'</code></td><td>Define custom square size for medium file</td></tr>
	<tr><td><code>sl:'%size%'</code></td><td>Define custom square size for large file</td></tr>
	<tr><td><code>to:'%file_type%'</code></td><td>Converts files from the requested type e.g.: from:'.jpg'</td></tr>
	<tr><td><code>from:'%file_type%'</code></td><td>Converts files to the requested type e.g.: to:'.png'</td></tr>
	<tr><td><code>f:'%directory_path%'</code></td><td>Allow you to define the path to the directory where you want to convert</td></tr>
</table>
<h3>Example:</h3>
<code>imageconvert -t -s -m -l st:'100' ss:'150' sm:'250' sl:'500' from:'.png' to:'.jpg' f:'C:\temp'</code>
<p>The above would path all png files at C:\temp and create a jpg version of it, additionally it would also create
	<ul>
		<li>a {filename}_thumb of max 100x100</li>
		<li>a {filename}_s of max 150x150</li>
		<li>a {filename}_m of max 250x250</li>
		<li>a {filename}_l of max 500x500</li>
	</ul>
<p>
<p>ps. this might be useful for creating portraits for games like baldur's gate as well, however it doesn't ofc crop them</p>
