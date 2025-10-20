# Тестовое задание

Пакет `external_odometry`, содержит ROS2-узел, который публикует данные визуальной одометрии в симуляцию ArduPilot через топики MAVROS.
Для выполнения использовалась Ubuntu 24.04.3 в виртуальной машине и ROS2 Jazzy.

## Установка

1.  Копировать репозиторий в папку `src` ROS2 workspace.
2.  Установить зависимости:
    ```bash
    rosdep install -i --from-path src --rosdistro jazzy -y
    ```
3.  Собрать пакет:
    ```bash
    colcon build --packages-select external_odometry
    ```

## Запуск

Каждая команда выполняется в отдельном терминале


2.  **Запуск ArduPilot SITL:**
    ```bash
    ardupilot/ArduCopter/sim_vehicle.py -v copter --console --map
    ```

3.  **Запуск MAVROS:**
    ```bash
    ros2 launch mavros apm.launch fcu_url:=udp://:14550@127.0.0.1:14555
    ```

4.  **Запуск паблишера одометрии:**
    ```bash
    ros2 run external_odometry odom_pub
    ```

## Демонстрация

Видео с демонстрацией работы не является частью пакета, но для удобства также загружено сюда (файл `Демонстрация.mp4`)