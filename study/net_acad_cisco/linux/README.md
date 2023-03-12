command [options] [arguments]
ls -l ~/Documents # will print the long list of files and folders in the current directory

~ # will point the home directory
/ # will point the root directory

drwxr-x--- 2 // the first letter states this is a direcotry
Symbol File Type Description
d directory A file used to store other files.

-     regular file	Includes readable files, images files, binary files, and compressed files.
  l symbolic link Points to another file.
  s socket Allows for communication between processes.
  p pipe Allows for communication between processes.
  b block file Used to communicate with hardware.
  c character file Used to communicate with hardware.
  drwxr-x--- 2 // the last 2 indicates how many hard links point to this file

-rw-r----- 1 syslog adm 106 Oct 2 19:57 kern.log # syslog is the owner name of this file who created it
-rw-r----- 1 syslog adm 106 Oct 2 19:57 kern.log # adm represent the group which owns this file

-rw-r----- 1 syslog adm 19573 Oct 2 22:57 syslog # 19573 is the file size for dirs that might show in kb
Directories and larger files may be shown in kilobytes since displaying their size in bytes would present a very large number. Therefore, in the case of a directory, it might actually be a multiple of the block size used for the file system. Block size is the size of a series of data stored in the filesystem.

-rw-r----- 1 syslog adm 19573 Oct 2 22:57 syslog # time stamp the file last modified - Oct 2 22:57

-rw-r----- 1 syslog adm 19573 Oct 2 22:57 syslog # syslog is the name of the file

In the case of symbolic links, a file that points to another file, the link name will be displayed along with an arrow and the pathname of the original file.
lrwxrwxrwx. 1 root root 22 Nov 6 2012 /etc/grub.conf -> ../boot/grub/grub.conf

The -t option will sort the files by timestamp while using with ls also -S will option will sort using file size

The -r option will reverse the order of any type of sort
ls -lSr /var/log

The su command allows you to temporarily act as a different user. By default, if a user account is not specified, the su command will open a new shell as the root user
