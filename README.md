# ImageConverter

<h2>Simple commandline image patch converter and thumbnail maker that uses settings file and commandline arguments for extra functionality.</h2>

<p>Can make Thumb, S/M/L file versions and change image filetype</p>

<p>Also provides thumbnail, medium and large file size conservions, which are especially useful for platforms like WordPress</p>

<p>Can either use console parameters or a json settings file to provide default values / extra functionality that is desired</p>

<table>
	<tr>
		<td>-t | --thumb</td><td>Generates thumbnail file (default 300x300) with suffix _thumb</td>
		<td>-s | --small</td><td>Generates Small file (default 300x300) with suffix _s</td>
		<td>-m | --medium</td><td>Generates Medium file (default 300x300) with suffix _m</td>
		<td>-l | --large</td><td>Generates Large file (default 1024x1024) with suffix _l</td>
		<td>st:'%size%'</td><td>Define custom square size for thumbnail file</td>
		<td>ss:'%size%'</td><td>Define custom square size for small file</td>
		<td>sm:'%size%'</td><td>Define custom square size for medium file</td>
		<td>sl:'%size%'</td><td>Define custom square size for large file</td>
		<td>to:'%file_type%'</td><td>Converts files from the requested type e.g.: from:'.jpg'</td>
		<td>from:'%file_type%'</td><td>Converts files to the requested type e.g.: to:'.png'</td>
		<td>f:'%directory_path%'</td><td>Allow you to define the path to the directory where you want to convert</td>
	</tr>
</table>
</ul>
