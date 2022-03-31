# Generator

제네레이터는 제네레이터 함수가 호출될 때 반환되는 iterator(이터레이터)의 일종이다. 제네레이터 함수는 일반적인 함수와 비슷하게 생겼지만 yield 구문을 사용해 데이터를 원하는 시점에 반환하고 처리를 다시 시작할 수 있다. 일반적인 함수는 진입점이 하나라면 제네레이터는 진입점이 여러 개라고 생각할 수 있다. 이러한 특성 때문에 제네레이터를 사용하면 원하는 시점에 원하는 데이터를 받을 수 있게 된다.

__ex)__

```python
>>> def generator():
...     yield 1
...     yield 'string'
...     yield True

>>> gen = generator()
>>> gen
<generator object generator at 0x10a47c678>
>>> next(gen)
1
>>> next(gen)
'string'
>>> next(gen)
True
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

## 동작

1. yield 문이 포함된 제네ㄹ레이터 함수를 실행하면 제네레이터 객체가 반환되는데 이 때는 함수의 내용이 실행되지 않는다.
2. next()라는 빌트인 메서드를 통해 제네레이터를 실행시킬 수 있으며 next() 메서드 내부적으로 iterator를 인자로 받아 이터레이터의 `__next__()`  메서드를 실행시킨다.
3. 처음 `__next__()` 메서드를 호출하면 함수의 내용을 실행하다 yield 문을 만났을 때 처리를 중단한다.
4. 이 때 모든 local state는 유지되는데 변수의 상태, 명령어 포인터, 내부 스택, 예외 처리 상태를 포함한다.
5. 그 후 제어권을 상위 컨텍스트로 양보(yield)하고 또 `__next__()` 가 호출되면 제네레이터는 중단된 시점부터 다시 시작한다.

yield 문의 값은 어떤 메서드를 통해 제네레이터가 다시 동작했는지에 따라 다르다. `__next()__` 를 사용하면 None이고 send()를 사용하면 메서드로 전달된 값을 갖게되어 외부에서 데이터를 입력받을 수 있게 된다.



## 이점

List, Set, Dict 표현식은 iterable하기에 for 표현식 등에서 유용하게 쓰일 수 있다. 이터러블 객체는 유용한 한편 모든 값을 메모리에 담고 있어야 하기 때문에 큰 값을 다룰 때는 별로 좋지 않다. 제네레이터를 사용하면 yield를 통해 그때 그때 필요한 값만을 받아쓰기 때문에 모든 값을 메모리에 들고 있을 필요가 없게 된다.



range() 함수는 Python 2.x에서 리스트를 반환하고 Python 3.x에선 range 객체를 반환한다. 이 range 객체는 제네레이터, 이터레이터가 아니다. 실제로 next(range(1))를 호출해보면 TypeError: 'range' object is not an iterator 오류가 발생한다. 그렇지만 내부 구현상 제네레이터를 사용한 것처럼 메모리 사용에 있어 이점이 있다.

```python
>>> import sys
>>> a = [i for i in range(100000)]
>>> sys.getsizeof(a)
824464
>>> b = (i for i in range(100000))
>>> sys.getsizeof(b)
88
```

다만 제네레이터는 호출할 때마다 필요한 값을 던져주고 기억하지 않기 때문에 리스트가 여러 번 사용되는데 반해 제네레이터는 한 번 사용된 후 소진된다. 이는 모든 이터레이터에 적용되는데 List, Set은 이터러블 하지만 이터레이터는 아니기에 소진되지 않는다.

![687474703a2f2f6e7669652e636f6d2f696d672f72656c6174696f6e73686970732e706e67](README.assets/687474703a2f2f6e7669652e636f6d2f696d672f72656c6174696f6e73686970732e706e67.png)



# 클래스를 상속했을 때 메서드 실행 방식

인스턴스의 메서드를 실행한다고 가정할 때 `__getattribute__()` 로 bound 된 메서드를 가져온 후 메서드를 실행한다. 메서드를 가져오는 순서는 `__mro__` 에 따른다. MRO(method resolution order)는 메서드를 확인하는 순서로 파이썬 2.3 이후 C3 알고리즘이 도입되어 지금까지 사용되고 있다. 단일 상속 혹은 다중 상속일 때 어떤 순서로 메서드에 접근할지는 해당 클래스의 `__mro__` 에 저장되는데 왼쪽에 있을 수록 우선 순위가 높다. B, C를 다중 상속받은 D 클래스가 있고, B와 C는 각각 A를 상속 받았을 때(다이아몬드 상속) D의 mro를 조회하면 볼 수 있듯이 부모클래스는 반드시 자식클래스 이후에 위치해있다. 최상위 object 클래스까지 확인했는데도 적절한 메서드가 없으면 `AttributeError`를 발생시킨다.

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

>>> D.__mro__
(__main__.D, __main__.B, __main__.C, __main__.A, object)
```

Python 2.3 이후 위 이미지와 같은 상속을 시도하면 `TypeError: Cannot create a consistent method resolution` 오류가 발생한다.



# GIL(Global Interpreter Lock)

GIL 은 스레드에서 사용되는 Lock을 인터프리터 레벨로 확장한 개념인데 여러 스레드가 동시에 실행되는 것을 방지한다. 어느 시점이든 하나의 Bytecode 만이 실행되도록 강제한다. 각 스레드는 다른 스레드에 의해 GIL 이 해제되길 기다린 후에야 실행될 수 있다. 즉 멀티 스레드로 구현을 하여도 본질적으로 싱글 스레드로 동작한다. 이 lock 이 필요한 이유는 CPython이 메모리를 관리하는 방법이 thread-safeness 하기 때문이다.

__ex)__

```python
import threading 

x = 0 # A shared value

def foo(): 
    global x 
    for i in range(100000000): 
        x += 1 
def bar(): 
    global x 
    for i in range(100000000): 
        x -= 1 
t1 = threading.Thread(target=foo) 
t2 = threading.Thread(target=bar) 
t1.start() 
t2.start() 
t1.join() 
t2.join() # Wait for completion

print(x)
# 첫 번째 결과 2016172
# 두 번째 결과 -1511425
```

여기서 결과 값이 0이 나와야 정상적으로 작동한 것을 생각이 된다. 실제로는 값이 201672, -1511425와 같이 전혀 이상한 숫자가 나오게 된다. 이는 두 개의 thread가 동시에 접근해서 각자의 작업을 하는데 어느 한 쪽의 작업 결과가 반영이 되지 않기 때문. (race condition)



GIL 때문에 성능 문제가 대두되는 경우는 압축, 정렬, 인코딩 등 수행시간에 CPU의 영향이 큰 작업(CPU bound)을 멀티 스레드로 수행하도록 한 경우이다. 이 땐 GIL 때문에 멀티 스레드로 작업을 수행해도 싱글 스레드일 때와 별반 차이가 나지 않는다. 이를 해결하기 위해서 멀티 스레드는 파일, 네트워크 IO 같은 IO bound 프로그램에 사용하고 멀티 프로세스를 활용해야 한다.

## GIL의 장점

GIL을 활용한 멀티 스레드가 그렇지 않은 멀티 스레드보다 구현이 쉬우며, 레퍼런스 카운팅을 사용하는 메모리 관리 방식에서 GIL 덕분에 오버헤드가 적어 싱글 스레드일 때 fine grained lock 방식보다 성능이 우월하다. 또한 C extension을 활용할 때 GIL은 해제되므로 C library를 사용하는 CPU bound 프로그램을 멀티 스레드로 실행하는 경우 더 빠를 수 있다.



__fine grained lock__: critical section마다 lock을 걸어서 제한하는 것





# GC 작동 방식

파이썬에선 기본적으로 garbage collection(가비지 컬렉션)과 reference counting(레퍼런스 카운팅)을 통해 할당된 메모리를 관리한다. 기본적으로 참조 횟수가 0 이된 객체를 메모리에서 해제하는 레퍼런스 카운팅 방식을 사용하지만, 참조 횟수가 0 은 아니지만 도달할 수 없는 상태인 reference cycles(순환 참조)가 발생했을 때는 가비지 컬렉션으로 그 상황을 해결한다.



엄밀히 말하면 레퍼런스 카운팅 방식을 통해 객체를 메모리에서 해제하는 행위가 가비지 컬렉션의 한 형태지만 여기서는 순환 참조가 발생했을 때 cyclic garbage collector를 통한 가비지 컬렉션과 레퍼런스 카운팅을 통한 가비지 컬렉션을 구분하였다.



__레퍼런스 카운팅__

모든 객체는 참조당할 때 레퍼런스 카운터를 증가시키고 참조가 없어질 때 카운터를 감소시킨다. 이 카운터가 0 이 되면 객체가 메모리에서 해제한다. 어떤 객체의 레퍼런스 카운트를 보고 싶다면 sys.getrefcount()로 확인할 수 있다.

=> Py_INCREF()와 Py_DECREF()를 통한 카운터 증감



__순환 참조__

순환 참조의 예를 하나 들면 자기 자신을 참조하는 객체

```python
>>> l = []
>>> l.append(l)
>>> del l
```

l 의 참조 횟수는 1 이지만 이 객체는 더이상 접근할 수 없으며 레퍼런스 카운팅 방식으로는 메모리에서 해제될 수 없다.

또 다른 예로는 서로를 참조하는 객체

```python
>>> a = Foo()  # 0x60
>>> b = Foo()  # 0xa8
>>> a.x = b  # 0x60의 x는 0xa8를 가리킨다.
>>> b.x = a  # 0xa8의 x는 0x60를 가리킨다.
# 이 시점에서 0x60의 레퍼런스 카운터는 a와 b.x로 2
# 0xa8의 레퍼런스 카운터는 b와 a.x로 2다.
>>> del a  # 0x60은 1로 감소한다. 0xa8은 b와 0x60.x로 2다.
>>> del b  # 0xa8도 1로 감소한다.
```

이 상태에서 0x60.x와 0xa8.x가 서로를 참조하고 있기 때문에 레퍼런스 카운트는 둘 다 1 이지만 도달할 수 없는 가비지가 된다.



__가비지 컬렉터__

파이썬의 gc 모듈을 통해 가비지 컬렉터를 직접 제어할 수 있다. gc 모듈은 cyclic garbage collection을 지원하는데 이를 통해 reference cycles(순환 참조)를 해결할 수 있다. gc 모듈은 오로지 순환 참조를 탐지하고 해결하기 위해 존재한다. gc 파이썬 공식 문서에서도 순환 참조를 만들지 않는다고 확신할 수 있으면 gc.disable()을 통해 garbage collector를 비활성화 시켜도 된다고 언급하고 있다.



## 가비지 컬렉션의 작동 방식

순환 참조 상태도 해결할 수 있는 cyclic garbage collection이 어떤 방식으로 동작하는지는 결국 어떤 기준으로 가비지 컬렉션이 발생하고 어떻게 순환 참조를 감지하는지에 관한 내용이다ㅣ.



__가비지 컬렉션이 일어나는 기준__

가비지 컬렉터는 내부적으로 generation과 threshold로 가비지 컬렉션 주기와 객체를 관리한다. 세대는 0세대, 1세대, 2세대로 구분되는데 최근에 생성된 객체는 0 세대에 들어가고, 오래된 객체일수록 2 세대에 존재한다. 더불어 한 객체는 단 하나의 세대에만 속한다. 가비지 컬렉터는 0 세대일수록 더 자주 가비지 컬렉션을 하도록 설계되었는데 이는 generational hypothesis에 근거한다.



__generational hypothesis__ 의 두 가지 가설

- 대부분의 객체는 금방 도달할 수 없는 상태가 된다.
- 오래된 객체에서 젊은 객체로의 참조는 아주 적게 존재한다.

주기는 threshold 와 관련있는데 gc.get_threshold() 로 확인해볼 수 있다.

ex)

```python
>>> gc.get_threshold()
(700, 10, 10)
```

각각 threshold 0, threshold 1, threshold 2 를 의미하는데 n 세대에 객체를 할당한 횟수가 threshold n 을 초과하면 가비지 컬렉션이 수행되며 이 값은 변경될 수 있다.



0세대의 경우 메모리에 객체가 할당된 횟수에서 해제된 횟수를 뺀 값, 즉 개체 수가 threshold 0 을 초과하면 실행된다. 다만 그 이후 세대부터는 조금 다른데 0 세대 가비지 컬렉션이 일어난 후 0 세대 객체를 1 세대로 이동시킨 후 카운터를 1 증가시킨다. 이 1 세대 카운터가 threshold 1을 초과하면 그 때 1세대 가비지 컬렉션이 일어난다. 러프하게 말하자면 0 세대 가비지 컬렉션이 객체 생성 700 번만에 일어난다면 1 세대는 7000번, 2 세대는 70000 번만에 일어난다는 뜻이다.



__라이프 사이클__

새로운 객체가 만들어질 때 파이썬은 객체를 메모리와 0 세대에 할당한다. 만약 0 세대의 객체 수가 threshold 0 보다 크면 collect_generations() 를 실행한다.

새로운 객체가 만들어질 때 파이썬은 `_PyObject_GC_Alloc()` 을 호출한다. 이 메서드는 객체를 메모리에 할당하고, 가비지 컬렉터의 0 세대의 카운터를 증가시킨다. 그 다음 0 세대의 객체 수가 threshold 0 보다 큰지, gc.enabled가 true인지, threshold 0 이 0이 아닌지, 가비지 컬렉션 중이 아닌지 확인하고, 모든 조건을 만족하면 collect_generations() 를 실행한다.

```python
_PyObject_GC_Alloc() {
    // ...

    gc.generations[0].count++; /* 0세대 카운터 증가 */
    if (gc.generations[0].count > gc.generations[0].threshold && /* 임계값을 초과하며 */
        gc.enabled &&  /* 사용가능하며 */
        gc.generations[0].threshold &&  /* 임계값이 0이 아니고 */
        !gc.collecting)  /* 컬렉션 중이 아니면 */
    {
        gc.collecting = 1;
        collect_generations();
        gc.collecting = 0;
    }
    // ...
}
```

cf. gc를 끄고 싶다면 gc.disable() 보단 gc.set_threshold(0)가 더 확실하다. disable()의 경우 서드 파티 라이브러리에서 enable() 하는 경우가 있다.



collect() 메서드는 순환 참조 탐지 알고리즘을 수행하고 특정 세대에서 도달할 수 있는 객체와 도달할 수 없는 객체를 구분하고 도달할 수 없는 객체 집합을 찾는다. 도달할 수 있는 객체 집합은 다음 상위 세대로 합쳐지고(0 세대에서 수행되었으면 1 세대로 이동), 도달할 수 없는 객체 집합은 콜백을 수행한 후 메모리에서 해체된다.



__어떻게 순환 참조를 감지하는가__

먼저 순환 참조는 컨테이너 객체(tuple, list, set, dict, class, ...)에 의해서만 발생할 수 있다. 컨테이너 객체는 다른 객체에 대한 참조를 보유할 수 있다. 그러므로 정수, 문자열은 무시한채 관심사를 컨테이너 객체에만 집중할 수 있다.



순환 참조를 해결하기 위한 아이디어로 모든 컨테이너 객체를 추적한다. 여러 방법이 있지만 객체 내부의 링크 필드에 더블 링크드 리스트를 사용하는 방법이 가장 좋다. 이렇게 하면 추가적은 메모리 할당 없이도 컨테이너 객체 집합에서 객체를 빠르게 추가하고 제거할 수 있다. 컨테이너 객체가 생성될 때 이 집합에 추가되고 제거될 때 집합에서 삭제한다.



순환 참조를 찾는 과정은 다음과 같다.

1. 객체에 gc_refs 필드를 레퍼런스 카운트와 같게 설정한다.
2. 각 객체에서 참조하고 있는 다른 컨테이너 객체를 찾고, 참조되는 컨테이너의 gc_refs 를 감소시킨다.
3. gc_refs가 0이면 그 객체는 컨테이너 집합 내부에서 자기들끼리 참조하고 있다는 뜻이다.
4. 도달할 수 없는 객체로 표시한 뒤 메모리에서 해제한다.



예시

```python
a = [1]
# Set: a:[1]
b = ['a']
# Set: a:[1] <-> b:['a']
c = [a, b]
# Set: a:[1] <-> b:['a'] <-> c:[a, b]
d = c
# Set: a:[1] <-> b:['a'] <-> c,d:[a, b]
# 컨테이너 객체가 생성되지 않았기에 레퍼런스 카운트만 늘어난다.
e = Foo(0)
# Set: a:[1] <-> b:['a'] <-> c,d:[a, b] <-> e:Foo(0)
f = Foo(1)
# Set: a:[1] <-> b:['a'] <-> c,d:[a, b] <-> e:Foo(0) <-> f:Foo(1)
e.x = f
# Set: a:[1] <-> b:['a'] <-> c,d:[a, b] <-> e:Foo(0) <-> f,Foo(0).x:Foo(1)
f.x = e
# Set: a:[1] <-> b:['a'] <-> c,d:[a, b] <-> e,Foo(1).x:Foo(0) <-> f,Foo(0).x:Foo(1)
del e
# Set: a:[1] <-> b:['a'] <-> c,d:[a, b] <-> Foo(1).x:Foo(0) <-> f,Foo(0).x:Foo(1)
del f
# Set: a:[1] <-> b:['a'] <-> c,d:[a, b] <-> Foo(1).x:Foo(0) <-> Foo(0).x:Foo(1)
```



위 상황에서 각 컨테이너 객체의 레퍼런스 카운트는 다음과 같다.

```
# ref count
[1]     <- a,c      = 2
['a']   <- b,c      = 2
[a, b]  <- c,d      = 2
Foo(0)  <- Foo(1).x = 1
Foo(1)  <- Foo(0).x = 1
```

1번 과정에서 각 컨테이너 객체의 gc_refs가 설정된다.

```
# gc_refs
[1]    = 2
['a']  = 2
[a, b] = 2
Foo(0) = 1
Foo(1) = 1
```

2번 과정에서 컨테이너 집합을 순회하며 gc_refs을 감소시킨다.

```
[1]     = 1  # [a, b]에 의해 참조당하므로 1 감소
['a']   = 1  # [a, b]에 의해 참조당하므로 1 감소
[a, b]  = 2  # 참조당하지 않으므로 그대로
Foo(0)  = 0  # Foo(1)에 의해 참조당하므로 1 감소
Foo(1)  = 0  # Foo(0)에 의해 참조당하므로 1 감소
```

3번 과정을 통해 gc_refs가 0인 순환 참조 객체를 unreachable 집합에 옮긴다

```
 unreachable |  reachable
             |    [1] = 1
 Foo(0) = 0  |  ['a'] = 1
 Foo(1) = 0  | [a, b] = 2
```

마지막으로 Foo(0)와 Foo(1)을 메모리에서 해제하면 가비지 컬렉션이 끝난다.



## ++

collect() 메서드는 현재 세대와 어린 세대를 합쳐 순환 참조를 검사한다. 이 합쳐진 세대를 young으로 이름 붙이고 다음의 과정을 거치며 최종적으로 도달할 수 없는 객체가 모인 unreachable 리스트를 메모리에서 해제하고 young에 남아있는 객체를 다음 세대에 할당한다.

```
update_refs(young)
subtract_refs(young)
gc_init_list(&unreachable)
move_unreachable(young, &unreachable)
```

update_refs()는 모든 객체의 레퍼런스 카운트 사본을 만든다. 이는 가비지 컬렉터가 실제 레퍼런스 카운트를 건드리지 않게하기 위함

subtract_refs()는 각 객체 i에 대해 i에 의해 참조되는 객체 j의 gc_refs를 감소시킨다. 이 과정이 끝나면 (young 세대에 남아있는 객체의 레퍼런스 카운터) - (남아있는 gc_refs) 값이 old 세대에서 young 세대를 참조하는 수와 같다.

move_unreachable() 메서드는 young 세대를 스캔하며 gc_refs가 0인 객체를 unreachable 리스트로 이동시키고 GC_TENTATIVELY_UNREACHABLE로 설정한다. 왜 완전히 unreachable이 아닌 임시로 설정하냐면 나중에 스캔될 객체로부터 도달할수도 있기 때문

```python
a, b = Foo(0), Foo(1)
a.x = b
b.x = a
c = b
d = Foo(2)
d.x = d
a.y = d
del d
del a
del b

# 위 상황을 요약하면 다음과 같다.
Foo(0).x = Foo(1)
Foo(1).x = Foo(0)
c = Foo(1)
Foo(0).y = Foo(2)
```

| young    | ref count | gc_refs | reachable |
| -------- | --------- | ------- | --------- |
| `Foo(0)` | 1         | 0       | `c.x`     |
| `Foo(1)` | 2         | 1       | `c`       |
| `Foo(2)` | 1         | 0       | `c.x.y`   |

이 상황에서 Foo(0)은 unreachable 리스트에 있다가 Foo(1)을 조사하며 다시 young 리스트의 맨 뒤로 돌아왔고, Foo(2)도 unreachable 리스트에 갔지만 곧 Foo(0)에 의해 참조될 수 있음을 알고 다시 young 리스트로 돌아온다.



# Celery

Celery는 메시지 패싱 방식의 분산 비동기 작업 큐다. 작업은 브로커를 통해 메시지로 워커에 전달되어 처리된다. 작업은 멀티프로세싱, eventlet, gevent를 사용해, 하나 혹은 그 이상의 워커에서 동시적으로 실행되며 백그라운드에서 비동기적으로 실행될 수 있다.



# PyPy 가 CPython 보다 빠른 이유

Cpython은 일반적인 인터프리터인데 반해 PyPy는 실행 추적 JIT(Just In Time) 컴파일을 제공하는 인터프리터기 때문이다. PyPy는 RPython으로 컴파일된 인터프리터인데, C로 작성된 RPython 툴체인으로 인터프리터 소스에 JIT 컴파일을 위한 힌트를 추가해 CPython 보다 빠른 실행 속도를 가질 수 있게 되었다.



## PyPy

PyPy는 파이썬으로 만들어진 파이썬 인터프리터. 일반적으로 파이썬 인터프리터를 다시 한 번 파이썬으로 구현한 것인데 CPython보다 빠르다.



## 실행 추적 JIT 컴파일

메서드 단위로 최적화하는 전통적인 JIT와 다르게 런타임에서 자주 실행되는 루프를 최적화한다.



## RPython(Restricted Python)

RPython은 이런 실행 추적 JIT 컴파일을 C로 구현해 툴체인을 포함한다. 그래서 RPython으로 인터프리터를 작성하고 툴체인으로 힌트를 추가하면 인터프리터에 실행추적 JIT 컴파일러를 빌드한다. PyPy 프로젝트 팀이 만든 일종의 인터프리터 제작 프레임워크이다. 동적 언어인 Python에서 표준 라이브러리와 문법에 제약을 가해 변수의 정적 컴파일이 가능하도록 RPython을 만들었으며, 동적 언어 인터프리터를 구현하는데 사용된다.

이렇게 언어 사양과 구현을 분리함으로써 어떤 동적 언어에 대해서라도 자동으로 JIT(Just-in-Time) 컴파일러를 생성할 수 있게 되었다.



# 메모리 누수가 발생할 수 있는 경우

사용자의 부주의로 인해 발생하는 메모리 누수에 대해서만 취급

대표적으로 mutable 객체를 기본 인자값으로 사용하는 경우에 메모리 누수가 일어난다.

ex)

```python
def foo(a=[]):
    a.append(time.time())
    return a
```

위의 경우 foo()를 호출할 때마다 기본 인자값인 a에 타임스탬프 값이 추가된다. 이는 의도하지 않은 결과를 초래하므로 보통의 경우 a=None으로 두고 함수 내부에서 if a is None 구문으로 빈 리스트를 할당해준다.



다른 경우로 웹 애플리케이션에서 timeout이 없는 캐시 데이터를 생각해볼 수 있다. 요청이 들어올수록 캐시 데이터는 쌓여가는데 이를 해제할 루틴을 따로 만들어두지 않는다면 이도 메모리 누수를 초래한다. 

클래스 내 `__del__` 메서드를 재정의하는 행위도 메모리 누수를 일으킨다. 순환 참조 중 인 클래스가 `__del__` 메서드를 재정의하고 있다면 가비지 컬렉터로 해제되지 않는다.



# Duck Typing

덕 타이핑이란 동적 타입을 가지는 프로그래밍 언어에서 많이 사용되는 개념으로, 객체의 실제 타입보다는 객체의 변수와 메서드가 그 객체의 적합성을 결정하는 것을 의미한다. 파이썬은 메서드 호출이나 변수 접근시 타입 검사를 하지 않으므로 duck typing을 다양하게 활용할 수 있다.

ex)

```python
class Duck:
    def walk(self):
        print('뒤뚱뒤뚱')

    def quack(self):
        print('Quack!')

class Mallard:  # 청둥오리
    def walk(self):
        print('뒤뚱뒤뒤뚱뒤뚱')

    def quack(self):
        print('Quaaack!')

class Dog:
    def run(self):
        print('타다다다')

    def bark(self):
        print('왈왈')


def walk_and_quack(animal):
    animal.walk()
    animal.quack()


walk_and_quack(Duck())  # prints '뒤뚱뒤뚱', prints 'Quack!'
walk_and_quack(Mallard())  # prints '뒤뚱뒤뒤뚱뒤뚱', prints 'Quaaack!'
walk_and_quack(Dog())  # AttributeError : 'Dog' object has no attribute 'walk'
```



위 예시에서 Duck 과 Mallard는 둘 다 walk() quack()를 구현하고 있기 때문에 walk_and_quack() 이라는 함수의 인자로 적합하다. 그러나 Dog는 두 메서드 모두 구현되어 있지 않으므로 해당 함수의 인자로서 부적합하다. 즉 적절한 duck typing에 실패한 것



Python에서는 다양한 곳에서 duck typing을 활용한다. `__len()__` 을 구현하여 길이가 있는 무언가를 표현한다던지, 또는 `__iter__()` 와 `__getitem()__` 을 구현하여 iterable을 duck-typing한다. 굳이 Iterable(가명) 이라는 interface를 상속받지 않고 `__iter__()__`와 `__getitem__()`을 구현하기만 하면 for ... in 에서 바로 사용할 수 있다.

이와 같은 방식은 일반적으로 interface를 구현하거나 클래스를 상속하는 방식으로 인자나 변수의 적합성을 runtime 이전에 판단하는 정적 타입 언어들과 비교된다. 자바나 스칼라에서는 interface, c++는 template을 활용하여 타입의 적합성을 보장한다.
