<<<<<<< HEAD
# For movel.ai technical test
1. Clone this repository
```bash
$ git clone https://github.com/tyantyan/test.git -b master
```
2. Checkout to branch master
```bash
$ git checkout master
```
3. Build
```bash
$ catkin build
```
4. For technical test no.2
- launch simulation
```bash
$ roslaunch gazebo_navigation_rviz.launch
```
- load param
```bash
$ rosparam load /src/test/config/position.yaml
```
- run waypoint program
```bash
$ python3 src/test/scripts/move_base.py
```
5. For technical test no.3
- play bag file
```bash
$ rosbag play src/test/bag/path_test.bag
```
- run algorithmic test program
```bash
$ python3 src/test/scripts/algorithmic_test.py
```

## Technical Test no. 2 notes
- position can be adjust by edit the position.yaml file in config folder
=======
# test
>>>>>>> main
