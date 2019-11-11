# Scrapy
### Scrapy란?
- 웹사이트를 크롤링하고 구조화된 데이터를 추출하기 위한 애플리케이션 프레임워크
- Scrapy는 원래  web scraping을 위해 설계되었지만 API를 사용하거나 범용 웹 크롤러로 데이터를 추출하는데 사용될 수도 있다. 

### 크롤링 방법
1. Scrapy : 크롤링 속도 조절가능, 웹 크롤링 프레임워크
2. BeautifulSoup :  배우기 쉽다, 빠른개발 가능, urllib,requset 등 다른 패키지 필요
- 두가지 방법 중 본인의 상황에 맞는 것을 사용하면 될 것 같다.

:eyes: 더 자세한 사항은 [Scrapy at a glance](https://docs.scrapy.org/en/latest/intro/overview.html) 참고!

## Scrapy project 생성
- `conda-forge` 패키지 설치
```
conda install -c conda-forge scrapy
```
- Scarpy 설치
```
pip install Scrapy
```
- Scrapy projecrt 생성
- `newsbot`을 프로젝트명으로 지정
- 아래와 같이 성공적으로 spider가 생성된 것을 확인할 수 있다.
```
> scrapy startproject newsbot

You can start your first spider with:
    cd newsbot
    scrapy genspider example example.com
```

- 프로젝트를 설치한 경로를 따라 들어가면 Scrapy의 구조를 확인할 수 있다.


<img src="./image/structure.png" width="180px" height="200px" alt="structure"></img>


- spiders 폴더 아래에 있는 `.py` 파일들은 무엇일까? 

1) `items.py`
-  데이터를 크롤링 할 때 해당 데이터를 클래스(class) 형태로 만든다.
- 뉴스 기사의 경우 기사의 제목(title), 내용(content), 해당기사의 링크(link)의 세 가지 항목을 가져오고 싶을 때, `items.py`에 **scrapy.Field()** 로 정의해주면 된다.

2) `middlewares.py`
- engine에서 다른 모듈로 request와 response 정보가 교환될 때 지나가는 중간 통로

3) `pipelines.py`
- 크롤링해 온 데이터를 처리해줄 때 사용
- 중복체크, 필터링, 데이터베이스 입력 후 처리해주려는 목적

4) `settings.py`
- 프로젝트 모듈간 연결 및 설정을 정의해주는 파일

## Scrapy Selectors
- Scrapy Selectors라고 불리는 XPath 또는 CSS에 기반한 메커니즘을 사용한다.

- XPath와 CSS로 작업하기 위해, Scrapy는 Selector 클래스를 제공하고 response로부터 무엇을 선택할 것인지에 대한 편리한 단축키를 제공한다.

- Xpath 간단한 예시
    - /html/head/title : HTML문서의 <head>요소를 선택
    - /html/head/title/text() : 앞에서 언급한 <title> 내부의 텍스트를 선택
    - //td : 모든 <td> 요소 선택
    - //div[@class='name'] : class='name' 속성을 포함한 모든 div 요소를 선택
(Scrapy로 크롤링을 하면서 더 자세한 문법을 다룰 예정!)

- Selectors는 4가지 기본 메서드를 가지고 있디.
    - xpath() : 인수로 주어진 XPath에서 선택된 각 노드를 대표하는 selectors 리스트를 돌려준다.
    - css() : 인수로 주어진 CSS에서 각 선택된 각 노드를 대표하는  selectprs 리스트를 돌려준다.
    - extract() : 선택된 데이터와 함께 유니코드 string을 돌려준다.
    - re() : 인수로 주어진 정규표현식을 적용해서 추출한 유니코드 string을 돌려준다.



