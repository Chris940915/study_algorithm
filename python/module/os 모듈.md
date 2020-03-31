
파이썬으로 데이터 파싱을 많이 진행하다보니 데이터를 읽거나 경로를 지정할 일이 많다.     
매번 까먹어서 찾아보는 시간이 아까워 한번 정리해보려고 한당.      
    
파이썬은 파일 경로 또는 디렉토리에 관한 코드가 많이 필요하다.     
리눅스 운영체제의 스크립트 언어에서 따와서 시작점이 없어서 if __name__ == '__main__' 으로 확인하는 것과 연관이 있다고 봐도 무방.      
      
그렇다면 파일 및 디렉토리 경로에 관한 함수를 정의한 os 모듈을 사용해보자.     
      
### 현재 작업 폴더 얻기     
    
**os.getcwd()** 를 사용하여 얻는다. (get current working directory)     
    
### 디렉토리 변경     
**os.chdir(path)** 를 사용한다. (path는 무조건 문자열)      
<pre>
  <code>
    os.chdir('/users')
    print(os.getcwd())
  </code>
    -> /users
</pre>
    
### 특정 경로에 대해 절대 경로 얻기    
**os.path.abspath(path)**   
    
### 현재 디렉토리 얻기    
**os.curdir()**

### 파일 상대경로를 절대 경로로 바꾸기     
**os.path.abspath(filenae)**    
    
### 디렉토리 안의 파일/서브 디렉토리 리스트      
**os.listdir(path)** path 하위에 있는 파일, 디렉토리 리스트를 보여준다.    

### 파일명만 추출
**os.path.basename(filename)**    
    
### 디렉토리 경로 추출    
**os.path.dirname(filenmae)**     
    
    
### 응용    
__file__ 를 사용.    
__file__ 은 현재 수행중인 코드를 담고 있는 파일의 위치한 path를 알려준다.    
따라서 __file__ 에는 현재 수행중인 코드의 위치가 담긴다.    

<pre>
  <code>
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  </code>
    1. __file__ 에 파일의 위치한 경로가 설정.
    2. abspath() 가 파일의 경로를 절대 경로화 해준다.
    3. dirname() 가 절대 경로에서 파일의 디렉토리 경로 추출.
 
</pre>


REF. https://itmining.tistory.com/122
     https://docs.python.org/ko/3/library/os.html
