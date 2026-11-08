+++
title = "Build your own desktop in the terminal"
date = 2020-01-17T13:00:00-08:00
description = "For the longest time, I would connect remotely vis ssh into a computer located at home to handle a lot of my daily tasks. Including todo lists, chatting, RSS, monitoring connections, and a slew of..."
show = "linux-unplugged"
authors = ["chzbacon"]
tags = ["terminal", "linux", "tmux", "tty-clock", "calcurse", "links2", "bmon", "wavemon", "rtv", "weechat", "mc", "midnight commander", "nnn", "bitlbee", "newsbeuter", "hn", "cortex", "bandwich", "ctw", "screen", "irssi"]
header_image = "/images/blog/build-your-own-desktop-in-the-terminal/f3eccee01d.jpg"
original_url = "https://linuxunplugged.com/articles/build-your-own-desktop-in-the-terminal"
+++

{{< youtube bBHVlqCK96w >}}

For the longest time, I would connect remotely vis ssh into a computer located at home to handle a lot of my daily tasks. Including todo lists, chatting, RSS, monitoring connections, and a slew of others. I used dyndns and port forwarding to connect to a raspberry pi located next to my home router. This was a perfect solution for me at the time and really helped me learn the Linux terminal.

That being said, it wasn't always the best solution. Mainly because my home connection and power wasn't super reliable. I found myself calling my wife (when she was at home) to either reboot my raspberry pi or power cycle the router. So keep that in mind as your mileage may vary using this configuration. Since then I've moved over to hosting this setup on an inexpensive ($5/mo.) VPS.

Throughout the years I've gone through several apps. Starting with [screen](https://www.gnu.org/software/screen/) as my terminal multiplexer and [irssi](https://irssi.org/) as my IRC client, both of which are still viable options and applications that you may want to consider for your setup. Below are a few of the applications that I've compiled over the years. If you take a moment to watch the accompanying video and have other applications that you use, please leave us a comment. We would love to see which applications you're using. If we get enough quality feedback we might even do a part two.

---

## Handy Applications for a terminal based workflow

### General use CLI applications

[tmux](https://github.com/tmux/tmux) - tmux is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen. tmux may be detached from a screen and continue running in the background, then later reattach.

### Basic tmux commands

- tmux (launches the tmux application)
- tmux new -s session-name (create a new tmux session and name it)
- tmux a (reattach to the last tmux session)
- tmux attach -t session-name (reattach to a specific session)
- ctrl+b c (creates a new window)
- ctrl+b d (detach from tmux session)
- ctrl+b % (split the terminal vertically)
- ctrl+b " (split the terminal horizontally)
- ctrl+b spacebar (auto rearrange panes)
- ctrl+b n (next tmux window)
- ctrl+b arrow key (while holding down control you can use the arrow keys to resize a pane)
- ctrl+b z (make a pane go full screen. use ctrl+b z again to return it to it's normal size.
- ctrl+b , (rename the current window)
- [calcurse](https://calcurse.org/) - calcurse is a calendar and scheduling application for the command line. It helps keep track of events, appointments and everyday tasks. A configurable notification system reminds user of upcoming deadlines, the curses based interface can be customized to suit user needs and a very powerful set of command line options can be used to filter and format appointments, making it suitable for use in scripts.
- [ctw - cursetheweather](https://github.com/dcardamo/cursetheweather) - CurseTheWeather is a curses application which displays the weather in a terminal. It can give the current weather as well as forecast weather for up to 10 days.
- [tty-clock](https://github.com/xorg62/tty-clock) - displays a simply digital clock in the terminal

### Traffic monitoring applications

- [bandwich](https://github.com/imsnif/bandwhich) - This is a CLI utility for displaying current network utilization by process, connection and remote IP/hostname
- [bmon](https://github.com/tgraf/bmon) - bmon is a monitoring and debugging tool to capture networking related statistics and prepare them visually in a human friendly way. It features various output methods including an interactive curses user interface and a programmable text output for scripting.
- [wavemon](https://github.com/uoaerg/wavemon) - wavemon is a wireless device monitoring application that allows you to watch signal and noise levels, packet statistics, device configuration and network parameters of your wireless network hardware. It should work (though with varying features) with all devices supported by the Linux kernel.

### Chat applications

- [BitlBee](https://www.bitlbee.org/main.php/news.r.html) - BitlBee brings IM (instant messaging) to IRC clients. It's a great solution for people who have an IRC client running all the time and don't want to run an additional MSN/AIM/whatever client. BitlBee currently supports the following IM networks/protocols: XMPP/Jabber (including Google Talk and Hipchat), MSN/Skype, Yahoo! Messenger, AIM and ICQ, the Twitter microblogging network (plus all other Twitter API compatible services like status.net)
- [weechat](https://weechat.org/) - Full-featured IRC plugin: multi-servers, proxy support, IPv6, SASL authentication, nicklist, DCC, and many other features.

### Web browsing & other related applications

- [cortex](https://github.com/GGLucas/cortex) - Cortex is a simple application to keep track and browse through reddit article lists where one would usually need to open a web browser and possibly use a mouse to navigate.
- [hn](https://github.com/andrewstuart/hn) - A Hacker News ncurses CLI reader written in Go.
- [links2](http://links.twibright.com/) - Links2 is a graphics and text mode WWW browser, similar to Lynx. It displays tables, frames, downloads on background, uses HTTP/1.1 keepalive connections. In graphics mode it displays PNG, JPEG, GIF, TIFF, and XBM pictures, runs external bindings on other types, and features anti-aliased font, smooth image zooming, 48-bit dithering, and gamma and aspect ratio correction.
- [newsbeuter](https://github.com/akrennmair/newsbeuter) - Newsbeuter is an RSS feed reader for the text console. Zed Shaw called it "The Mutt of Feed Readers". It is designed to run on Unix-like operating systems such as GNU/Linux and FreeBSD. NetBSD is currently not supported, due to technical limitations.
- [rtv](https://github.com/michael-lazar/rtv) - A text-based interface (TUI) to view and interact with Reddit from your terminal.

### File managers

- [mc](https://midnight-commander.org/) - Midnight Commander is an orthodox (two-pane) file manager, supporting standard file operations, virtual filesystems, panelizing of external commands, and user menus. It also includes an internal viewer, editor, and visual diff tool.
- [nnn](https://github.com/jarun/nnn) - nnn is a full-featured terminal file manager. It's tiny and nearly 0-config with an incredible performance.

Obviously there are a ton of other great applications you can run on the terminal these are just a few of my personal favorites. I would encourage you to comment on the YouTube video above with your favorite applications. Until then stay cool and keep Linux'n.
