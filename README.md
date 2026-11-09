# Instrukcja instalacji i uruchomienia projektu FOSSBot

Poniższe polecenia przygotują środowisko operacyjne, pobiorą repozytoria, zainstalują zależności ROS 2, skompilują projekt i uruchomią symulację na czystym systemie Ubuntu 26.04 LTS. 

Wklejaj poniższe bloki komend kolejno do terminala:

### 1. Przygotowanie systemu i kluczy ROS 2
```bash
sudo apt update && sudo apt install -y locales software-properties-common curl gnupg git
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
sudo add-apt-repository universe -y

sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu resolute main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### 2. Instalacja ROS 2, Gazebo i bibliotek
```bash
sudo apt update
sudo apt install -y ros-lyrical-desktop python3-colcon-common-extensions python3-rosdep python3-opencv python3-numpy ros-lyrical-xacro ros-lyrical-ros-gz
```

### 3. Inicjalizacja narzędzia rosdep
```bash
sudo rosdep init
rosdep update
```

### 4. Pobranie przestrzeni roboczej (Workspace)
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

git clone https://github.com/LRMPUT/FOSSBotEduSim.git
git clone https://github.com/DOMPUR/test.git fossbot_interface
```

### 5. Instalacja zależności paczek, kompilacja i uruchomienie
```bash
cd ~/ros2_ws

# Aktywacja bazowego ROS 2
source /opt/ros/lyrical/setup.bash

# Instalacja brakujących zależności z poziomu paczek
rosdep install --from-paths src --ignore-src -r -y

# Kompilacja całości
colcon build

# Aktywacja środowiska i uruchomienie projektu
source install/setup.bash
ros2 launch fossbot_interface fossbot.launch.py
```
