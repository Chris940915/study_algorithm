

[재귀 호출 문제](#재귀-호출-문제)   
[ - 이진 검색](#이진-검색)   
[ - 문자열 순열](#문자열-순열)   
[ - 문자열 조합](#문자열-조합)   
[ - 전화 단어](#전화-단어)   


# 재귀 호출 문제

## 이진 검색
<pre>
  정렬된 정수 배열에 대해 이진 검색을 수행하여 주어진 정수의 인덱스를 찾아내는 함수를 구현하라.   
  다음과 같은 메소드 선언을 사용하라.   
  int binarySearch( int[] array, int lower, int upper, int target );
  이 검색 방법의 효율을 따져보고 다른 검색 방법과 비교해 보라.   
</pre>
   
이진 검색에서는 찾고자 하는 아이템과 정렬된 검색 공간의 **가운데에 있는 원소**를 비교한다.   
3가지 경우의 수가 존재.   
  1) 가운데 원소가 찾고자 하는 값보다 작은면 검색 공간의 앞쪽 절반을 제외.   
  2) 가운데 원소가 찾고자 하는 값보다 크면 검색 공간의 뒤쪽 절반을 제외.   
  3) 가운데 원소가 찾고자 하는 값과 같은 경우 검색을 중단.   
      
이진 검색은 검색 공간에서 검색해야 할 부분을 점점 줄여가면서 대상을 찾아내는 방법이기 때문에 재귀적인 구현을 하기에 적합.   
*검색할 배열, 검색 범위, 찾아야 할 원소*가 메소드의 인자로 전달.   
*검색 공간의 크기*는 상한(upper)에서 하한(lower)을 배면 알 수 있고, 그 크기를 2로 나눈 값을 하한값에 더하면 중앙에 있는 원소의 인덱스를 알 수 있다.   
그런 후 그 원소를 검색할 원소와 비교한다.   
*둘이 같으면* 인덱스를 반환하고, *검색할 원소가 더 작으면* 상한을 중안원소의 인덱스에서 1을 뺀 값으로, *검색할 원소가 더 크면* 하한을 중앙 원소의 인덱스에 1을 더한 값으로 하여 재귀 호출을 한다.   
원하는 원소를 찾을 때까지 이런 재귀 호출을 반복하면 된다.   
   
코딩을 시작하기 전에 어떤 오류 상황을 처리해야 하는지 생각해보자.   
오류 상황을 따져보는 방법 가운데 하나로, 주어진 데이터에 대해 어던 가정을 하고 있는지 생각해보고 그러 가정이 어떻게 위배될 수 있는지 따져보는 것을 들 수 있다.   
   
* 문제에서 직접적으로 주어진 가정으로, 정렬된 배열만 검색할 수 있기 때문에, 배열이 정렬되지 않았는지 파악해야 할 필요가 있다.   
   
* 또 한가지 가정은 검색할 원소가 배열에 들어있다는 가정이다.   
  원소를 찾을 때까지 재귀 호출을 종결시키지 않으면 배열에 그 원소가 없을 경우, 재귀 호출이 무한히 반복되게 된다.   
  상한과 하한이 같을때, 그 위치에 있는 원소가 찾고자 하는 원소가 아닌 경우에는 오류 코드를 반환하면 이 문제를 해결할 수 있다.   
  
* 마지막으로 하한이 반드시 상한 이하라는 가정도 갈려있다.   
   
<pre>
  <code>
    const int NOT_IN_ARRAY = -1;
    const int ARRAY_UNORDERED = -2;
    const int LIMITS_REVERSED = -3;
    
    int binarySearch( int[] array, int lower, int upper, int target ) {
      int center, range;
      range = upper - lower;
      
      // 예외처리. 하한이 반드시 상한 이하.
      if (range < 0) {
        return LIMITS_REVERSED;
      // 예외처리. 검색할 원소가 배열에 들어있냐. 
      }else if( range == 0 && array[lower] != target) {
        return NOT_IN_ARRAY;
      }
      // 예외처리. 배열이 정렬되어있냐.
      if( array[lower] > array[upper] )
        return ARRAY_UNORDERED;
        
      center = ((range)/2) + lower;
      
      if (target == array[center]){
        return center;
      } else if (target > array[center]{
        binarySearch(array, center+1, upper, target);
      } else {
        binarySearch(array, lower, center-1, target);
      }
    }
  </code>
</pre>
   
위의 풀이의 재귀 호출은 검색 범위를 변경시키는 역할만 한다.   
하지만, 반복문을 써서 매번 반복문이 돌아갈 때마다 검색 범위를 바꾸는 식으로 고치면 재귀 호출에 의한 오버헤드를 피할 수 있다.   
반복문으로 구현하여 효율을 향상시키면 다음과 같다.   
   
<pre>
  <code>
    int iterBinarySearch( int[] array, int lower, int upper, int target ) {
      int center, range;
      
      if (lower > upper)
        return LIMITS_REVERSED;
        
      while(true){
        range = upper - lower;
        if (range === 0 && array[lower] != target)
          return NOT_IN_ARRAY;
        
        if (array[lower] > array[upper])
          return ARRAY_UNORDERED;
        
        center = ((range)/2) + lower;
        
        if(target == array[center]){
          return center;
        }else if(target < array[center]) {
          upper = center-1;
        }else{
          lower = center+1;
        }
      }
    }
        
  </code>
</pre>
   
이진 검색에서는 매 단계를 반복할 때마다 검색 공간을 절반씩 떨궈내기 때문에 O(log(n))알고리즘이다.   
따라서 모든 원소를 무작정 검색하는 O(n) 알고리즘에 비해 더 빠르다.   
하지만 이진 검색을 하려면 배열이 정렬되어 있어야 하며, 이미 정렬된 배열이 아닌 이상 O(nlog(n)) 시간을 투자해서 정렬을 해야 한다는 단점이 있다.   
   
   
## 문자열 순열
   
<pre>
  어떤 문자열에 있는 문자들을 나열하는 모든 가능한 순서를 출력하는 루틴을 구현하라.   
  원본 문자열에 있는 모든 문자들을 사용하는 모든 순열을 출력하면 된다.   
  예를 들어, "hat"이라는 문자열이 주어진다면 "tha", "aht", "tah", "ath", "hta", "hat"이라는 문자열을 출력해야 한다.   
  같은 문자가 여러 개 들어있어도 서로 다른 문자로 간주한다.   
  "aaa"라는 문자열이 주어진다면 "aaa"를 여섯 번 출력해야 한다.   
  순열을 출력하는 순서는 마음대로 정해도 된다.
</pre>
   
순열을 늘어놓은 목록에서 패턴을 찾아보자.   
첫번째(가장 왼쪽) 위치에 들어갈 문자를 선택하면 그 문자를 변경하기 전에 나머지 문자들로 만들 수 있는 모든 순열을 출력해야 한다.   
이 과정을 계속 반복한다.   
바꿔 말하면 순열을 만들어내는 절차는 주어진 위치에 들어갈 문자를 하나 고르고, 방금 선택한 문자를 바꾸기 전에 다음 위치부터 시작해서 오른쪽으로 가면서 순열을 만들어내는 절차를 반복하는 것으로 생각할 수 있다.   
   
재귀적으로 정의를 해보자.   
n 위치에서 시작하는 모든 순열을 찾아내기 위해서는 n 위치에 들어갈 수 있는 모든 문자를 순서대로 집어넣고, n 위치에 들어가는 각 글자별로 n+1 위치부터 시작하는 모든 순열을 찾아내면 된다(재귀 케이스).   
n 이 입력 문자열에 있는 문자의 개수보다 많으면 순열이 종결된 것이므로 결과를 출력하고, n보다 작은 위치에서 글자를 바꾸는 단계로 돌아간다(기본 케이스).   
   
   
   
자바로 구현해보면 다음과 같다.

플래그와 입력 문자열을 저장하기 위한 두 개의 배열을 할당.   
출력 문자열을 만들기 위한 StringBuffer 객체를 만드는 permute라는 wrapper(래퍼) 메소드를 사용.   
문자는 StringBuffer 객체에 추가시키며, 재귀 호출이 반환되면 버퍼의 길이를 줄이는 방법으로 마지막 문자를 떨궈낸다.   



<pre>
  <code>
    void permute( String str ) {
      int           length = str.length();
      boolean[]     used   = new boolean[length];
      StringBuffer  out    = new StringBuffer();
      char[]        in     = str.toCharArray();
      doPermute( in, out, used, length, 0); 
    }
  </code>
</pre>
<pre>
  <code>
    void doPermute(char[] in, StringBuffer out, boolean[] used, int length, int level){
        if(level == length){
          System.out.println( out.toString() );
          return;
        }
       for (int i=0; {
          if( used[i]) continue;
          out.append(used[i]);
          used[i] = True;
          doPermute(in, out, used, length, level+1);
          used[i] = False;
          # Python 의 pop과 동일.
          out.setLength( out.length() - 1);
        }
      } 
  </code>
</pre>
   
  

## 문자열 조합
   
<pre>
  문자열에 있는 문자들의 모든 가능한 조합을 출력하는 함수를 구현하라.   
  조합의 길이는 1이상이고 문자열 길이 이하이다.   
  문자의 배치 순서만 다를 뿐 같은 문자들이 들어가 있는 조합은 같은 조합으로 간주한다.   
  즉. "123"이라는 문자열이 입력됐을 때 "12"와 "23"은 서로 다른 조합이지만 "21"은 "12"와 같다.   
</pre>
   
앞에 나온 문자열 순열 문제와 쌍을 이루는 문제.   
   
알고리즘을 정리해보도록 하자.

<pre>
  입력 시작 위치부터 입력 문자열 끝까지의 각 글자에 대해
    출력 문자열의 현재 위치에 그 글자를 선택
    글자들을 출력 문자열로 출력
    현재 글자가 입력 문자열의 마지막 글자가 아니면 
      방금 선택한 글자 다음 글자에서 반복을 시작하여 다음 위치부터 시작하는 나머지 조합 생성
</pre>

이 알고리즘을 C#으로 코딩해보면 다음과 같다.
   
   
<pre>
  <code>
    void combine( string str ){
      int       length = str.Length;
      char[]    instr  = str.ToCharArray();
      StringBuilder outstr = new StringBuilder();
      
      doCombine( instr, outstr, length, 0, 0);
    }
    
    void doCombine(char[] instr, StringBuilder outstr, int length, int level, int start){
      for (int i = start; i++ ){
        outstr.Append(instr[i]);
        Console.WriteLine(outstr);
        
        if( i < length - 1 ) {
          doCombine(instr, outstr, length, level+1, i+1);
        }
        outstr.Length = oustr.Length - 1; 
      }
    }
  </code>
</pre>
   
## 전화 단어   
   
<pre>
  전화번호를 알려줄 때 일곱자리 번호를 나타내는 단어로 알려주는 경우가 종종 있다.
  예를 들어, 전화번호가 866-2665 라면 외우기 힘든 일곱자리 숫자보다는 "TOOCOOL"이라는 단어를 알려주는 편이 낫다.   
  하지만 866-26665라는 번호는 이 외에도 여러 대응되는 단어들을 만들어낼 수 있다.   
  일곱자리 전화번호를 입력받아서 주어진 수를 표현할 수 있는 모든 가능한 "단어" 또는 글자 조합을 출력하는 루틴을 작성하라.   
  0과 1에는 글자가 할당되어 있지 않기 때문에 2~9만 글자로 바꿀 수 있다.   
  전화 버튼 번호(0~9)와 위치를 나타내는 번호(1,2,or3 숫자 하나당 알파벳 3개가 할당)를 인자로 받아서 주어진 버튼의 주어진 위치에 대응되는 글자를 반환하는 다음과 같은 보조 루틴을 쓸 수 있다.   
  <code>   
    char getCharKey( int telephoneKey, int place )
  </code>   
  예를 들어, getCharKey(3, 2)를 호출하면 3번 버튼에 있는 "DEF" 글자 중 두번째 'E'가 반환된다.   
</pre>
   
우선 일곱자리 숫자를 가지고 몇 개의 단어를 만들 수 있는지 수학적으로 계산하는 것을 보여주자.
숫자가 하나씩 늘어날 때마다 경우의 수가 세배로 늘어난다.   
따라서 일곱자리 전화번호의 경우에는 3^7개의 단어를 만들 수 있고, 길이가 n인 전화번호라면 3^n개의 단어를 만들 수 있다.   
   
이제 이런 단어들을 출력하는 알고리즘을 찾아내야 한다.   
   
이 문제는 두가지 경로를 통해 풀 수 있다.   
*첫번째 글자부터 시작해서 오른쪽에 있는 글자에 영향을 미치도록 하거나 아니면 마지막 글자부터 시작해서 왼쪽에 있는 글자에 영향을 미치도록 하거나*   
둘 중 한가지 방법을 택할 수 있다.   
   
이제 정확하게 무엇을 해야하는지 따져본다.   
어떤 글자가 바뀌면 그 바로 오른쪽에 있는 글자가 모든 가능한 값을 한 바퀴 돌아야만 그 글자가 다시 바뀔 수 있다는 결과를 바탕으로 문제를 풀려고 한다.   
i 위치에 있는 글자를 바꾸면 i+1 위치에 있는 글자가 한 바퀴 돌아서 원래 값으로 돌아온다.   
i 번째 요소와 i+1번째 요소가 서로 어떤 식으로 상호작용하는지를 바탕으로 알고리즘을 작성하면 재귀 호출과 관련된 문제일 가능성이 높으므로, 여기에서도 재귀적인 알고리즘을 만들어보자.    
마지막 글자를 바꾸고 나면 다른 것은 돌릴 수 없으므로 재귀 호출을 종결시킬 수 있는 훌륭한 기본 케이스가 된다.   
정리해보면 다음과 같다.   
   
<pre>
  현재 숫자가 마지막 숫자를 지나버리면
    마지막이므로 단어 출력
  그렇지 않으면
    현재 숫자를 나타낼 수 있는 세 글자에 대해 낮은 글자, 가운데 글자, 큰 글자 순으로 그라자 현재 자리를 나타내도록 한다.   
      다음자리로 넘어가서 재귀 호출   
      현재 자리가 0이나 1이면 반환   
  
  코드는 다음과 같다.   
   
  <code>
    static final int PHONE_NUMBER_LENGTH = 7;
  
    void printTelephoneWords( int[] phoneNum ) {
      char[] result = new char[ PHONE_NUMBER_LENGTH ];
       
      doPrintTelephoneWords( phoneNum, 0, result);
    }
    
    void doPrintTelephoneWords( int[] phoneNum, int curDigit, char[] result ) {
      if( curDigit == PHONE_NUMBER_LENGTH ){
        System.out.println( new String( result ) );
        return;
      }
      
      for( int i = 1; i <= 3; i++ ){
        result[ curDigit ] = getCharKey( phoneNum[curDigit], i);
        doPrintTelephoneWords( phoneNum, curDigit + 1, result);
        if( phoneNum[ curDigit ] == 0 || phoneNum[ curDigit ] == 1)
          return;
      }
    }
  
  </code>
</pre>
   
이 알고리즘의 실행시간은 어떻게 될까?   
약 3^n개의 단어를 출력해야 하기 때문에 정답이라면 O(3^n)보다 작을 수가 없다.   
   
   
<pre>
  재귀 호출을 쓰지 않고 printTelephoneWords를 다시 구현하라.
</pre>
   
이 상황에서는 재귀 알고리즘이 그다지 도움이 되지 않아 보인다.   
스택 기반의 자료구조를 쓰면 재귀 호출을 반복적인 구현으로 고칠 수 있지만, 이 문제에 대해서는 아예 다른 알고리즘을 사용하는 방법이 더 나을 것 같다.   


