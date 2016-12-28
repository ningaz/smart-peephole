# Smart peephole

It is study project for Internet-of-Things course. It works on [Intel Edison] board. For working You need Intel Edison board, any USB [UVC] webcam, button and buzzer (optional). When You are pushing button, system is taking a photo and sending it in [Slack].

## Dependencies

You need [python] with following modules:
* *[requests]*  
* *[slacker]*

And [mraa] library.


## Deploy

For install run from terminal ```make```. After that You should create config file like ```example.cfg```

### Configuration file

```python
[Section]  #Section contains set of parameters used in one module of system
par1 = value1
par2 = value2
...
```

Configuration file consist two sections:
* slack (token, botname, channel, etc.)
* main (path to JPEG image file)

[python]: <https://www.python.org>
[requests]: <http://docs.python-requests.org/en/master/>
[slacker]: <https://github.com/os/slacker>
[mraa]: <https://github.com/intel-iot-devkit/mraa>
[UVC]: <http://www.ideasonboard.org/uvc/>
[Slack]: <https://slack.com>
[Intel Edison]: <https://software.intel.com/en-us/iot/hardware/edison>
