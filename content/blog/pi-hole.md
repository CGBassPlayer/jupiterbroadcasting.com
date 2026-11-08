+++
title = "Playing with Pi-hole"
date = 2019-02-05T12:00:00-08:00
description = "Pi-hole is an appliance for network-wide ad-blocking and sinkholing."
show = "linux-unplugged"
authors = ["wes"]
tags = ["pi-hole", "pihole", "raspberry pi", "dns", "dnsmasq", "ftl", "ads", "malware", "advertising", "adblocking", "dhcp"]
original_url = "https://linuxunplugged.com/articles/pi-hole"
+++

### Pi-hole

Pi-hole is an appliance for network-wide ad-blocking and sinkholing.

#### How It Works

Pi-hole replaces your DNS server with a modified DNSmasq system. Normally this is done by adding a DHCP option that directs clients to use the pi-hole ip as their DNS server. You can also manually make this change on a per-client basis.

Unlike browser-based ad-blockers, pi-hole uses hostname and ip blocklists to block ads at a DNS level. This has upsides and downsides. The biggest upside is that you can easily deploy this at a network wide level, so clients without access to a browser basesd blocker, guests, etc, can all benefit. It also seems to evade some types of ad-blocking detector scripts.

One of the more notificable downsides, is that because ads are blocked at the DNS level, their is often still html space for them on the page. The ad doesn't load, but you end up with some awkward blank space. Many browser-based blockers simple remove the element. This can go both ways depending on site design. Because browser-based blockers are local, they are also more easily disabled.

![](/images/blog/pi-hole/giphy.gif)

#### Compared to /etc/hosts

Very similar, but on a network-wide level. You can also take advantage of their pleasant GUI to update and modify settings.

Also, because it is DNSMasq-based, it can be your DHCP server as well. If you have a stock consumer router and don't already have a system like this, I would reccomend it. The UI is easy to use, and well integrated. Plus you get nice stats about all your dns requests and how many are blocked.

If you are already a larger system like pfsense, pi-hole probably doens't make sense for you.

#### The Pi Factor

Obviously based on the name, the Raspberry Pi is a major taget for Pi-hole. However pi-hole is not like many other raspberry pi focused projects. They don't provide sd-card images, but rather a list of supported operating systems. This list includes popular distros in both amd64 and arm architectures. Once you've installed a supported OS, they provide an automated installer that will get everything up and running.

Raspbian: Jessie / Stretch  
Ubuntu: 16.04 / 16.10  
Fedora: 27 / 28  
Debian: 8 / 9  
CentOS: 7 (not ARM)

What is everything? A forked version of DNSMasq, some management scripts and cron jobs, and an api and web server.

Because of this simple architecture, you can easily run it on your desktop, in a VM, or a container. To that point, they also provide a ready made Docker image. Just tweak and ENV variables and away you go.

Overall the documentation is excellent, and their are guides for many different scenarios, including setting up pi-hole and openvpn on a VPS for mobile ad-blocking. Replace openvpn w/ wireguard and that sounds pretty nice!

#### Blocklists and Whitelists

![Pi-hole Log](/images/blog/pi-hole/E1TQ9NXR.png)

This can be a bit of a rabbit hole, but is important for operations. By managing your whitelist and various blocklists, you can determine how many ads and other potentially privacy invading hosts are blocked. Of course, the farther you go down this road, the more likey you will end up blocking services you, or another on your network, may wish to use.

Example: There are community blocklists that attempt to block any and all facebook hostnames and ips. In an office setting, this might be great for productivity, but considering the deep integrations FB has, it may break integrations downstream. It's also probably not realistic on a shared home network.

The default blocklists are fairly conservative, but will block the most egregious offenders. The wider-community has many published blocklists for all kinds of things, and the pi-hole project provides documentation for converting many of them. I suggest trying the defaults and maybe a few of the more popular options for a while before spending too much time configuring.

If necessary you can also whitelist any domains you know you wish to allow. This might be useful for work, or for the occasional service you still need to use.

They make it easy to export and import configuration and blocklists, so its easy reinstall or reimage as needed. You can start with a spare raspberry pi, and move to a server later. You can run it on a VPS or run it on your laptop.

Overall a robust and actively developed project. Not necessarily unique functionality, but well packaged and pleasant to use. I will keep mine running on the network for the foreseeable future, but also won't be getting rid of my regular ad-blockers anytime soon.

Example command

```
docker run --name pihole1                                 \
           --cap-add=NET_ADMIN                            \
           --restart=unless-stopped                       \
           --dns=127.0.0.1                                \
           --dns=1.0.0.1                                  \
           -e ServerIP=<Public IP of host running Docker> \
           -e DNS1=1.0.0.1                                \
           -e DNS2=8.8.4.4                                \
           -p 80:80                                       \
           -p 53:53/tcp                                   \
           -p 53:53/udp                                   \
           pihole/pihole
```

Pi-hole Dockerfile (amd64)  
<https://github.com/pi-hole/docker-pi-hole/blob/master/Dockerfile_amd64>

How do I add additional blocklists?  
<https://discourse.pi-hole.net/t/how-do-i-add-additional-block-lists-to-pi-hole/259>

Blocklist Collection Â¦ Firebog  
<https://firebog.net/>

Pi-hole installer  
<https://github.com/pi-hole/pi-hole/#one-step-automated-install>

pi-hole/FTL: The Pi-hole FTL engine (DNSMasq fork)  
<https://github.com/pi-hole/FTL>
