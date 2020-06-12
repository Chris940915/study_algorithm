

## Systemctl과 Systemd   

Kafka를 daemon에 실행시켜놓고 Python으로 Twitter Streaming api를 호출하던 중 계속 exception이 일어나는 상황을 직면했다.     
어떻게 할까... 고민하던 중 Systemctl과 Systemd를 이용하는 방법을 발견했다.   
    
Ubuntu, CentOS 이전 버전은 Systemd에 service를 등록하여 쉽게 실행을 할 수 있지만,    
최근 버전의 Systemctl Service 등록은 상당히 손이 많이 가는 작업이였다.    


### 명령어   
<pre>
  # service 파일 수정 후, daemon에 업데이트.    
  systemctl daemon-reload   
    
  # service 시작    
  systemctl start <service name>    
  
  # service 중지    
  systemctl stop <service name>   
  
  # service 상태보기    
  systemctl status <service name>
  
</pre>
    
명령어는 위와 같다.   
사실 제일 어려운 점은 service 파일 작성과 실행 파일 권한 부여이다.    

## systemd configuration file

<pre>
  아래 코드는 내가 구성한 streaming.service 파일의 content 이다.   
  
   <code>
    [Unit]
    Description=Twitter kafka Streaming python script
    #After=network.target

    [Service]
    Type=simple
    User=bigbase-2
    Group=bigbase-2

    ExecStart=/home/bigbase-2/start.sh
    WorkingDirectory=/home/bigbase-2/
    Restart=always
    RestartSec=3

    [Install]
    WantedBy=multi-user.target
 </code>
 
 여기서 주의할 점은... User와 Group이다.     
 처음에 아무것도 모르고 root를 줬더니 pip 에 설치된 module (tweetpy)를 못읽어오는 사태가 발생했다.     
 그래서 실행하고자하는 python 파일의 위치와 사용자 명, 그룹으로 설정해줬다.
  
 한가지 더.    
 Exception 이나 Dead가 되었을때를 위해서 설정으로 Restart=always 를 줬지만 만약에 다른 곳에서 오류가 발생하면 request를 엄청나게(?) 보내게 된다.    
 그래서, RestartSec=3 옵션은 어떻게 보면 필수적이라고 볼 수 있었다.      
 글을 쓰며 생각해보니 이제 오류가 안나니까 이 옵션은 없어도 될듯?    

</pre>
    
권한 같은 경우는 이해가 조금 안가서 좀 더 공부가 필요하다.    
OS를 그렇게 공부했는데도 권한이 헷갈린다.    
    
service로 등록하고 시작할때 permission deniend 예외가 계속 발생해서 어떻게 할까 고민하다가...   
service , shell , python 3개의 파일 모두 **chmod 755** 로 권한을 줘서 해결했다.    
권한 관련해서 추후에 정리하도록 하겠다.


* shell 파일의 상단에는 **#! /bin/bash**를 service 파일 상단에는 **## systemd configuration file** 를 꼭 적자!


