# Scrap
This script will scrap the last posts from Ubuntu HandBook site

You need Python3 and bs4 library.

Output will be like this:
<pre>
[hossein@ArchLinux ~]$ ubuntuhandbook 

How to Install Linux Kernel 4.6 in Ubuntu 16.04


Install The Latest SMPlayer 16.4.0 in Ubuntu 16.04 via PPA


How to Install Twitter App Corebird 1.2.1 in Ubuntu 16.04


How to Install Ubuntu Tweak in Ubuntu 16.04


Customizing Your Notification Bubbles in Ubuntu 16.04

[hossein@ArchLinux ~]$ 
</pre>

# How It Works

First of all download scrap.py file and change it's name to ubuntuhandbook:

<pre>
mv scrap.py ubuntuhandbook
</pre>

Now let this file to be excuted:

<pre>
chmod +x ubuntuhandbook
</pre>

At last step move the file to /usr/bin:

<pre>
sudo mv ubuntuhandbook /usr/bin
</pre>

Now type ubuntuhandbook in your terminal:

<pre>
[hossein@ArchLinux ~]$ ubuntuhandbook 

How to Install Linux Kernel 4.6 in Ubuntu 16.04


Install The Latest SMPlayer 16.4.0 in Ubuntu 16.04 via PPA


How to Install Twitter App Corebird 1.2.1 in Ubuntu 16.04


How to Install Ubuntu Tweak in Ubuntu 16.04


Customizing Your Notification Bubbles in Ubuntu 16.04

[hossein@ArchLinux ~]$ 
</pre>


