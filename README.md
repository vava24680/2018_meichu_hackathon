---
tags: 黑克松
lang: zh-tw
---
新竹x梅竹黑客松 2018
===
[TOC]

## DialogFlow
### Intent 
Some Natural Query for 

- On-Off Control
- Set Value
- Ask for Value


### Entity 分類
4 分類
action, location, status, object
action: 各式動作
location: 地點
status: 尋求溫度等等非動作之狀態請求 (GET)
object: 動作後的受詞 (POST)

- action_on-off
    - On
    - Off
- location_school
    - Second Restaurant
    - First Restaurant
    - Girl's Second Restuarant
    - ED202
    - MIRC311
- status_school
    - Temperature
- object_311onoff
    - Little Fan
    - Big Fan
    - Central Curtain
    - Right Curtain
    - Left Curtain
    - Ceiling Light
    - Wall Light
    - Projection Light
- object_school
    - AC
    - Controller

### Usage
For Beta Version:
We have to tell Google Assistant 'Talk to Hackathon IoT set AC in ED202 to 26' or 'Ask Hackathon IoT what is the temperature of ED202' 


May add select specific id for selecting device in multiple devices
