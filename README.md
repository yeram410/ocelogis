# KPMG Ideathon 2021 : Ocelot Logistics
Hello! We are Yae Ram Kim, Hyeon Su Kim, Ju Myeong Park, Tae Ha Lim from Ocelot Logistics. Our team is composed of four members majoring in Business/Computer Science. This project is related to KPMG Ideathon with ideas in logistics industry.
안녕하세요! Ocelot Logistics의 김예람, 김현수, 박주명, 임태하입니다. 저희 팀은 한동대학교에서 Business/Computer Science를 전공하는 네명의 팀원으로 구성되어있으며, 현재 물류산업 관련 아이디어로 KPMG 아이디어톤에 참여하고 있습니다.

# Introduction
Our application is a scheduling management service for freight forwarders and drivers which multi-processor task-scheduling algorithm is applied to. Our goal for upcoming 2021 KPMG Ideathon demonstration is 1) to build a prototype of UI/UX design for freight forwarder use and driver use and 2) to derive an optimized route using our main algorithm on a map data.
멀티 프로세서의 태스크 스케줄링 알고리즘을 적용한 화물 운송사 및 기사를 위한 스케줄링 어플리케이션입니다. 이번 2021 KPMG Ideathon 시연 목표는 1. 운송사용 2. 차주용 각각의 어플리케이션의 프로토타입 UI/UX 디자인, 주요 기능인 알고리즘을 개발하여 map data에 적용해 최적 경로를 도출해내는 것입니다.

## Background
The importance of land transportation and delivery services has increased due to the recent growth of the online market and the uprising non-face-to-face culture by the coronavirus. The change in online shopping industry of South Korea after COVID-19 shows the proportion of online shopping transactions out of retail sales form 22% before the outbreak of COVID-19 increased to 28.3% after the outbreak of COVID-19. Especially, the transaction size in food service, food, and household goods increased significantly; Online shopping is now more becoming a crucial aspect of living a life in the untact era. As such, in line with the current consumption trend in the newly advent of the untact era, numerous companies are advocating specialized services and sales strategies for online shopping. As a result, the demand and workload for land transportation and delivery have increased. However, many  
최근 온라인 시장의 성장과 코로나로 인한 비대면 문화의 확산으로 인해 배송 및 배달 서비스의 중요도가 높아졌습니다. 우리나라의 코로나 19로 인한 온라인쇼핑 변화를 살펴보면 코로나19 발생전 22%대였던 소매판매액 중 온라인쇼핑 거 래액의 비중이 코로나19 발생후 28.3%까지 증가하였습니다. 이중 특히 음식서비스, 식품, 생활용품 등의 거래액이 크 게 증가하며 온라인 쇼핑이 언택트 시대에 점점 더 중요한 부분으로 자리잡아가는 것을 확인할 수 있었습니다. 이렇듯 새롭게 도래한 언택트 시대의 소비추세에 발맞춰 다양한 기업들이 온라인쇼핑에 특화된 서비스 및 판매전략을 내세우 고 있습니다. 이로인해 배달, 배송업무의 수요와 업무량은 늘어났지만, 일을 효율적으로 수행할 수 있는 시스템이 잘 구비되어 있지 않아 배송 지연, 배달원 부족 현상과 같은 문제가 발생하고 있습니다.

## What is the Problem
이동시간이 많이 소요되는 물류 배달 업종, 방문 수리 업종에서는 효율적으로 이동경로를 설정하는 일이 매우 중요합니다. 물류산업은 디지털화 되어 있었지만, 이동경로 설정방법에는 당일 아침마다 물류 기사가 직접 수기로 경로를 설정해야하는 아날로그적 경로설정 방법이 지배적입니다. 이는 비효율적이고, 중간에 예약이 변경되거나 취소되는 경우 따로 대처방법이 존재하지 않아 재구성이 어렵고, 그에 따라 발생하는 문제가 화물 기사 개인의 책임 혹은 피해로 전가되기도 합니다.

## Solving Approach
저희는 멀티 프로세서의 태스크 스케줄링 알고리즘을 개발하여 효율적인 물류 배송을 위한 시스템을 개발하고자 합니다. 먼저 배달원은 프로세서에, 배달원이 처리해야할 업무는 태스크에, 배달원의 이동시간은 프로세서가 태스크를 처리하기 위해 생기는 커뮤니케이션 시간에 각각 대입하고, 이를 바탕으로 배송 업무에 관한 그래프를 그린 후 가지고 있는 자원을 활용해 최대한 효율적으로 문제를 해결할수있는 방법을 찾을수있도록 합니다. 이때 그래프에 들어가는 값 들은 실제 도로 정보를 바탕으로 입력됩니다.

# Code Explanation

## [Working Environment](https://github.com/yeram410/ocelogis/tree/main/Working_Environment)
Code | Explanation | Used Library
-----|------|---------------
[dataHan.py](https://github.com/yeram410/ocelogis/tree/main/Working_Environment/dataHan.py) | 지도 데이터 | pandas <br> 2 <br> 3

<br>
<br>


# Web
