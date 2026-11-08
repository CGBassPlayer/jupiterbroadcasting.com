+++
title = "Chris Goes to MeetBSD"
date = 2018-10-23T09:00:00-07:00
description = "MeetBSD 2018 took place at the sprawling Intel Santa Clara campus. The venue itself felt more like an olive branch than a simple friendly gesture by Intel. In truth it felt like a bit of an..."
show = "linux-unplugged"
authors = ["chris"]
tags = ["meetbsd", "ixsystems", "freebsd", "netbsd", "intel", "speakers", "report"]
header_image = "/images/blog/meetbsd2018/898474181f.jpg"
original_url = "https://linuxunplugged.com/articles/meetbsd2018"
+++

![IntelEntry](/images/blog/meetbsd2018/TzVt2vS.jpg)

MeetBSD 2018 took place at the sprawling Intel Santa Clara campus. The venue itself felt more like an olive branch than a simple friendly gesture by Intel. In truth it felt like a bit of an apology. You get the subtle sense they feel bad about how the BSD's were treated with the Meltdown and Specter flaws. In fact, you may be right to think they felt a bit sorry towards the entire open source community.

### MeetBSD 2018

At most massive venues the parking is the first concern, not so here - in fact that was rather straight forward. No, the real challenge is navigating the *buildings*. Luckily I had help from navigator extraordinaire, Hadea, who located the correct building, SC12 quickly. Finding the entrance took a moment or two though. The lobby itself was converted by iXsystems efficiently into the MeetBSD expo hall, clean, efficient and roomy with registration, some seating, and an extra conference room for on-on-one sessions. On day two sponsor booths were also setup. All who showed up on day one were warmly greeted with badges, lanyards and goodies by Denise and her friendly team.

![IntelLoby](/images/blog/meetbsd2018/U0oKvRf.png)

Like every great BSD event, plenty of food was made available. And as always they make it look effortless. These events showcase iXsystem's inherent generosity toward its community; with breakfast items in the back of the main auditorium room in the morning, boxed lunches, fruit and cookies at lunch time, and snacks for the rest of the day. But just in case your still hungry, there is a pizza meetup in another Intel room after day one and two.

MeetBSD leverages it's realistically small crowd size on day one. The morning starts off with introductions of the entire group, the mic is passed around the room.

The group is a good mix of pros in the industry (such as Juniper, Intel, Ebay, Groupon, Cisco, etc), iX staff, and a few enthusiast. Lots of people with a focus or passion for networking. And, of course, some friendly Linux bashing went down for good measure, always followed by a good natured chuckle.

### The Kick Off

![Allan gets Ready](/images/blog/meetbsd2018/y9lGxok.jpg)

At 10am Kris Moore takes the stage to layout how TrueOS can be used to bootstrap a FreeBSD based "distribution". There was some encouragement from Kris to his fellow developers to modernize some of their workflow. And underneath this all there is currently a debate underway about switching FreeBSD development to Git. Modernizing the tools and process that various members of the BSD community use feels like a growing area of focus.

![IntelSorry](/images/blog/meetbsd2018/WdNZTFy.jpg)

Second talk of the day was "Intel & FreeBSD: Better Together" by Ben Widawsky from Intel's open source area. He has a long history of development in the multimedia area, including extensive driver work on Linux. He's now focusing on "technology enabling" for FreeBSD. This being the second talk of the event seemed purposeful. Ben had something he wanted to get across.

He put a lot of effort into his presentation. He wanted to clearly communicate that Intel is a contributor to open source, and intends to do better. He also went out of his way to cover his area of expertise, actively soliciting input and help from the audience at hand.

There was a lot of top level attention on this event from Intel. The long-ish negotiation process the organizers went through to get Intel to ratchet down security is a bit of context for this talk too. But also noteworthy was that Widawsky's talk was closely scrutinized by Intel legal, with what seem to be special emphasis taken on their statement on their "Security First Pledge".

### After Lunch Glow

![AfterLunch](/images/blog/meetbsd2018/SfO4KCx.jpg)

Andrew Fengler gave a detailed talk about what to monitor, and what *NOT* to monitor under FreeBSD. He used data from his production systems to show us the signs of a failing disk.

Before the group could get into another ZFS discussion (this time the official one on the schedule) the attention turned to [the Bloomberg story](https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies) about SuperMicro (and others but SuperMicro is an important player in the BSD world) systems being bugged by Chinese intelligence. The discussion focused around Apple and their servers. A strong note of skepticism was in the room, but many were open to the idea some of the story might have been possible. The discussion got the mic going around the room again, and was eventually punted to a impromptu dedicated talk.

![ZFSPan](/images/blog/meetbsd2018/942psSg.png)

One of the first slips in the schedule, the ZFS panel discussion started a few minutes late on the first day. The panel of distinguished ZFS experts assembled casually on the stage, and start immediately taking questions from the audience.

Questions ranged from solving specific issues for sysadmins, to what the future of ZFS on Windows means for FreeBSD.

### The Second Day Hangover

![mLucas](/images/blog/meetbsd2018/ZgK6P4V.png)

Day two started with the crowd a bit smaller. The late night geeky conversations wore the herd a bit thin, with a few of them trickling in during [Michael Lucas's](https://mwl.io/) "Why BSD?" talk.

His talk reminded me a lot of my early days in IT, working in an environment where the new hot Linux distro of the month would get deployed into production... Because how else could you *really* test something? It was a hit the ground running kind of way of learning operating systems, and I enjoyed hearing his similar journey. The irony is that experience led me to use Linux even more. But his experience drive him to BSD.

While Lucas' talk was great, the star talk of the event was one that did not even make it on the set schedule. So the majority of the attendees did not even know it would be coming. It was one of those down to the wire booking situations. Jury duty eventually strikes all of us, and it gives no consideration to BSD events of any kind. No matter how historically important the guest might be.

But the legal system stars aligned, and MeetBSD's special guest was able to attend on the second day, easily filling the space booked for a batch of 5-minute lighting talks.

![AwardTime](/images/blog/meetbsd2018/TP24VAl.png)

Before our special guest could take the stage, the iXsystems staff planned surprise thank you for [Denise Ebery](https://twitter.com/denisee88) the planner (of this event and many others) and feeder of the herd. She worked hard to secure everything from each individual speaker to each and every bite of food provided, and the room was feeling the appreciation. It was really a genuinely sweet moment, and the groups tightness was palatable. I can easily say I've never been tempted to tear up at an event like this before, but this one got to me. There is a true affections and history that many of the attendees have for each other and the recognition of hard work well done resonated. This alone made the second day special for me, but I think the day's special guest was the highlight for most.

This type of community is by nature virtual 90% of the time, and when communities like this finally get together in person the appreciation for each other and excitement to collaborate is noticeable.

![Kirk](/images/blog/meetbsd2018/32jCOtg.png)

[Kirk McKusick](https://en.wikipedia.org/wiki/Marshall_Kirk_McKusick) who is a computer scientist, known for his extensive work on BSD UNIX, from the 1980s to FreeBSD in the present day.

If the BSD's really are the royal heritage of Unix (as they put it) then Dr. Kirk McKusick is one of their cherished Sovereigns. He gave his first-hand history of the very early stages of the FreeBSD project - a talk he has clearly given before, and one many in the audience has heard many times before. But as I looked around the room Dr. McKusick managed to hold the groups attention and solicit a few hardy laughs at the appropriate moments.

The rest of the day was filled with talks meant to help out the working sysadmin and developers out there. Topics ranges from using DTrace in production, wrangling virtual machines, and even why one curmudgeon refuses to use those new fancy languages like Go and Rust.

![MeetBSDSign](/images/blog/meetbsd2018/nP7SqTX.png)

### MeetBSD Gives me The Feels

I find that I am subtly unnerved at this venue, and at lunch I saw it clearly. I have always had a strong geek radar, allowing me to navigate a new area (like Berkeley for MeetBSD of 2016, or even SCALE earlier this year in Pasadena), and in a glance I can see who is from my conference and who isn't. This means it is easy, nearly effortless to know who to greet with a smile and a wave. These are MY people. Here at the Intel campus though it is different. The drive in alone reveals behemoth complexes all with well known tech names prominently displayed. This is Silicon Valley, and all of these people look like MY people. So much for knowing who's from my conference. Thank goodness for those infamous BSD horns. None-the-less I am struck by how massive these tech giants are. And Intel is one of the largest of those giants, and see the physical reminders of this fact brought home the significance that they had opened their doors, wifi, and bathrooms to the BSD community.
