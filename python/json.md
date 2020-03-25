
json으로 데이터를 주고받는 사례가 점점 많아지고 있다.   
그만큼 가볍고 쓰기 쉽다는 것을 증명.   
또한, python과 json의 호환이 좋아 사용하기 쉽다. (dictionary와 같음.)     

load와 loads로 Json file을 읽을 수 있으며, encoding의 종류에 따라 오류가 발생한다.   
   
또한, multiple dictionary를 가지고 있는 json file을 읽을 수가 없어 조치가 필요하다. (원래는 데이터를 생성하는 단계에서 multiple dictionary를 [] 에 넣는게 맞음.)   
   
  
아래 코드는 json 파일에 dictionary 한개만 저장되어 있지않고 multiple dictionary가 저장되어 있을때 읽는 방법.   
<pre>
   <code>
      import json 
      
      with open('파일이름.json', 'r') as json_file:
         tweets = [json.loads(line) for line in json_file]
         
   </code>
</pre>
