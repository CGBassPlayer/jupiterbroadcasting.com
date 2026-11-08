+++
title = "Pinebook Pro Review"
date = 2019-11-21T14:00:00-08:00
description = "The Pinebook Pro is an ARM powered laptop created by Pine Microsystems, Inc. . This is Pine64's follow up to the original Pinebook which was released in November of 2016. The Pinebook Pro is a..."
show = "linux-unplugged"
authors = ["chzbacon"]
tags = ["pine64", "pinebook pro", "debian", "ubuntu", "manjaro", "mate", "kde", "xfce", "arm", "chrome", "chromium", "kali", "android", "lxde"]
header_image = "/images/blog/pinebook-pro-review/68f4d74f90.jpg"
original_url = "https://linuxunplugged.com/articles/pinebook-pro-review"
+++

![Pinebook-Pro-01](/images/blog/pinebook-pro-review/wfvcyR9D.jpg)

The Pinebook Pro is an ARM powered laptop created by [Pine Microsystems, Inc.](https://www.pine64.org/pinebook-pro/). This is Pine64's follow up to the original Pinebook which was released in November of 2016. The Pinebook Pro is a small 14" laptop that packs some pretty impressive specs, and best of all it comes in at only $199 ($232 shipped to the US). So what are the specs? Check'em out below.

- Rockchip RK3399 SOC with Mali T860 MP4 GPU
- 4GB LPDDR4 RAM
- 1080p IPS Panel
- Magnesium Alloy Shell body
- Bootable Micro SD Slot
- 64GB of eMMC (Upgradable)
- PCIe x4 to m.2 NVMe SSD Slot (requires optional adapter / Max 5W NVMe drives)
- 1x USB 2.0 Host, 1x USB 3.0 Host
- USB-C (Data, Power and Video out)
- Lithium Polymer Battery (10000mAH)
- Stereo Speakers
- WiFi 802.11 AC + Bluetooth 5.0
- 3.5mm Headphone Jack
- Microphone
- Front-Facing Camera (1080p)
- ISO & ANSI Keyboard Variants
- Privacy Switches for Camera, Microphones and BT/WiFi
- Barrel Power (5V 3A) Port

So is a $199 ARM powered laptop worth it? In my opinion yes, very much so. I'm actually writing this review at 30,000 feet. In the time where inexpensive Chromebooks are gaining so much popularity, I think the Pinebook Pro really fills a niche for a truly all Linux powered laptop. Most avid Linux users are sure to fall in love with this laptop, but that's not to say it doesn't have issues.

So what are those issues? Namely, it's just one right now, the trackpad. The palm rejection isn't that great and if you touch it while typing it halts keyboard input or causes you to jump back to some random place in your document. Pretty frustrating to say the least. To work around this I just disable the trackpad using FN+F7 and use a USB or Bluetooth mouse. ~~That being said, the firmware is currently being worked on to address the issue and will probably be available by the time this article goes live.~~ Update: ayufan and several others have been hard at work and have released the first [keyboard and trackpad firmware update](https://github.com/ayufan-rock64/pinebook-pro-keyboard-updater). A huge thank you goes out to the entire team for turning that around so quickly.

The default Debian install could also use a little more polish, but I really can't fault Pine64 on that. I realize they were trying to get this device out the door and in the hands of those who are going to port their favorite distribution to it. However, the default Debian 9 installation is using the 4.4 kernel and as one would expect with Debian, the repository is a bit lacking when it comes to desktop applications, especially for aarch64. The default installation isn't all bad though. The on-demand throttling mode seems to work really well. It is also pretty snappy. I was able to playback 1080p 60fps video with zero issues.

![Pinebook-Pro-02](/images/blog/pinebook-pro-review/Bn-9K08-.jpg)

Right now a ton of work is going on around this device by a lot different developers. Including Ubuntu, Manjaro, Kali, Chromium OS, Android, Armbian, \* BSD and several of others. I've currently tried a few of the builds, including Ubuntu (MATE), Ubuntu (LXDE), Manjaro (KDE/XFCE), Chromium OS, and of course the default Debian build.

The Ubuntu MATE image is wonderful, and rather usable, but does lack the aarch64 packages you might need. You can extend the available software on Ubuntu and Debian by installing the snapd package and using snap versions of applications which you might not find in the default repositories.

As an Ubuntu user you will feel right at home with this build. Just know you might struggle to find that one must-have desktop application. I'm confident that we'll have a lot of this software available as aarch64 becomes more popular. When 20.04 lands I would imagine this will be a pretty big part of that release.

Currently, Manjaro has KDE and XFCE preview builds available which use the 5.3 kernel, and as one would expect it has a ton of software available for the aarch64 architecture. It's also rather snappy, but at the time of writing has a few issues. The biggest of which include flaky wifi, no bluetooh, poor audio (which isn't great to begin with), issues with suspend, and a few others. Although that seems like a big deal, and to some extent it is, it's really just part of the development process. I personally think Manjaro will be one of the best builds for the Pinebook once these few issues get ironed out. Mainly because Manjaro, being based on Arch, is going to have the largest selection of aarch64 software for a bit until the other distributions get up to speed.

**Linux build links**  
[Pinebook Pro Software Releases](https://wiki.pine64.org/index.php/Pinebook_Pro_Software_Release)  
[Manjaro - Preview 3](https://forum.manjaro.org/t/manjaro-arm-preview3-for-pinebook-pro/111488)  
[ayufan's Linux build repository](https://github.com/ayufan-rock64/linux-build/releases/)  
[mrfixit2001's Debian build repository](https://github.com/mrfixit2001/debian_desktop/releases)

However, in my opinion the Chromium OS build is one of the best options for the Pinebook Pro right now. If anything it's a great image to flash to an SD card when your friend or even your kid wants to use the Pinebook Pro to do some browsing. Out of the box it supports 4k 60fps playback on Youtube with zero issues. In theory it should also support Netflix and other streaming services by simply logging in and pressing play. While I personally won't be installing Chromium OS on the eMMC module, I will always have a copy on an SD card, and I highly recommend you do the same. Just a great image to have in your go bag.

Overall I think the Pinebook Pro is a great on-the-go type of laptop. It's lightweight, durable, has a 6-8 hour battery life, and is powerful enough to get most of your daily tasks done. Need to compose an email, slack with teammates, edit some code, watch YouTube, listen to music, edit photos, or maybe even play a few retro games? The Pinebook Pro is perfect for that. Over time I'm confident the software will catch up and the Pinebook Pro will be a great everyday carry laptop.
