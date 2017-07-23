FROST: Frantic Room Organization SysTem
=======================================

We've all been there. We've put something somewhere and half a year
later desperately tried to find it. Only to realize it was exactly
where we expected it to be in the first place but it was a little
hidden. If only we were *sure* it was there and looked a bit harder...

This is exactly how *FROST* came to be.

I wanted to create a system that would store the information about my
possessions' placement and maybe some additional data about them. At
first I thought about using *SQLite* and creating some frontend for
this task but then I realized I already have a great tool for this
job...

...a filesystem!

"Places" would be represented by directories, "possessions" would be
represented by files. What would these files contain? Actually,
anything! For simple items the name would be all we need, so an empty
file will do. For items with some "properties" we can use a text file
or our favorite data serialization format. YML is pretty nice for this
purpose as it's both human-readable as a file and has a logical
structure. Note that now it is possible to not only find our
possessions but also to, for example, quickly check if we have a
pendrive with a given capacity that is not used for anything
important.

A directory tree is hierarchical, is as flexible as it gets and we
already have many great tools for querying and manipulating the data
in it. The synchronization of such "database" is also a breeze, we can
use any tool suited for file synchronization (Dropbox, Syncthing, Git,
etc.). By using a directory structure we get surprisingly many
features for free. We even get symbolic links that may be used to
reference some items without duplicating them. Personally I use
symlinks to represent the ports/cables in
my [KVM switch](https://en.wikipedia.org/wiki/KVM_switch) because they
tend to get confusing (more about this below).

For searching it is possible to use the generic tools like *grep(1)*,
*find(1)* or [*fzf(1)*](https://github.com/junegunn/fzf).

At this point *FROST* is no longer strictly a software project. It's
more of an idea or a loose specification with some optional helper
scripts (see: [utils.org](utils.org)).

Examples
--------

An example directory structure:

```
+---my-home/
|   +---my-room/
|   |   +---desk/
|   |   |   +---laptop.yml
|   |   |   +---left-closet/
|   |   |   |   +---red-pendrive.yml
|   |   |   |   +---blue-pendrive.yml
|   |   |   +---right-closet/
|   |   |       +---old-Kindle-case
|   |   |       +---powerbank.yml
|   |   |       +---nail-clipper
|   |   +---shelf-behind-the-door
|   +---bedroom/
|       +---phone-charger
+---backpack/
    +---phone-charger
    +---HDMI-DP-adapter
```

`laptop.yml` contains:

```
CPU: Intel i7
RAM: 16 GiB RAM
SSD: 256 GB
OS: Ubuntu 16.04
ports:
  - HDMI
  - USB x3
  - Mini DisplayPort
  - audio jack 3.5" (in & out)
```

`red-pendrive.yml` contains:

```
vendor: Kingston
model: DataTraveler
memory: 16 GB
state: probably broken
```

`powerbank.yml` contains:

```
vendor: Xiaomi
capacity: 10000 mAh
```

...and so on.

The actual data to put there depends on the user's needs. If you need
some data there, put it in. If you don't need it, just don't. It's
only a text file.

I mentioned documenting the ports of my KVM switch with symlinks. I do
it because the setup of all these cables can quickly get confusing and
I prefer to check it in *FROST* than follow the cables to check which
cable is which. This is how I do it:

```
+---kvm/
    +---devices/
    |   +---audio-in -> /dev/null
    |   +---audio-out -> ../../speakers.yml
    |   +---usb-1 -> ../../keyboard.yml
    |   +---usb-2 -> ../../mouse.yml
    |   +---video-out -> /dev/null
    +---pc-1/
    |   +---audio -> ../../laptop-dock.yml
    |   +---usb -> ../../laptop-dock.yml
    |   +---video-in -> /dev/null
    +---pc-2/
        +---audio -> ../../../desk/left-side/desktop-pc.yml
        +---usb -> ../../../desk/left-side/desktop-pc.yml
        +---video-in -> /dev/null
```


FAQ
---

**Q: Do I need to update the *FROST* database each time I take something from a shelf?**

*A: No! Update it only when you change the designated place of an
item. It's only a reference point, not a 100% true real-time
representation of reality.*

**Q: I don't like the way you do XYZ. Can I do it in a different way?**

*A: Absolutely! FROST enforces almost no rules, it's only a proposal,
a template. Use it however you like it best.*

**Q: You used both "GB" and "GiB" in your example. Cannot you make up your mind on one spelling?**

*A: [I did it on intentionally and it is correct.](https://en.wikipedia.org/wiki/Binary_prefix)*

**Q: Isn't it a bit silly to put a laptop in *FROST*? I know where it is at all times!**

*A: Yes, it looks silly. You can skip such things if you want. On the
other hand it's still worthwhile to keep them in FROST if you want to
write down their descriptions/properties.*
