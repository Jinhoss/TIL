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





