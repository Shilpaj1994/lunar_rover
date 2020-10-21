# Py3Gazebo

Their hasn't been an activity of this parent class so this fork provides the following changes,
* Python3 support
* AsyncIO support
* Gazebo v9,v11 support

# Example 

```python
import asyncio
import pygazebo
import pygazebo.msg.v11.poses_stamped_pb2

class GazeboMessageSubscriber: 

    def __init__(self, host, port, timeout=30):
        self.host = host
        self.port = port
        self.loop = asyncio.get_event_loop()
        self.running = False
        self.timeout = timeout

    async def connect(self):
        connected = False
        for i in range(self.timeout):
            try:
                self.manager = await pygazebo.connect((self.host, self.port))
                connected = True
                break
            except Exception as e:
                pass
            await asyncio.sleep(1)

        if connected: 
            self.poses_subscriber = self.manager.subscribe('/gazebo/default/pose/info', 'gazebo.msgs.PosesStamped', self.poses_callback)

            await self.poses_subscriber.wait_for_connection()
            self.running = True
            while self.running:
                await asyncio.sleep(0.1)
        else:
            raise Exception("Timeout connecting to Gazebo.")

    def poses_callback(self, data):
        self.poses_stamped = pygazebo.msg.v11.poses_stamped_pb2.PosesStamped()
        self.poses_stamped.ParseFromString(data)
        ... 
        Do stuff
```

# Updating Proto Messages
If the message interface to Gazebo changes the messages in msg/ directory must be recreated.
Run this command from the parent directory,

```
GAZEBO_HOME=
protoc --proto_path=$GAZEBO_HOME/gazebo/msgs --python_out=pygazebo/pygazebo/msg $GAZEBO_HOME/gazebo/msgs/*proto 
```

To migrate to Python3 use the 2to3 tool from the directory where all of the generated Python messages are found.
The 'w' flag will write the changes back to the file. If this flag is not present it will just output a diff of the changes.

```
2to3 -w *.py
```

