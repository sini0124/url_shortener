# url_shortener
url_shortener is a url shortener to reduce a long link.


## **Better Structure with Application Factories and Blueprint**



**Application Factories의 개념과 목적**

- Flask application이 function 외부에서 초기화되면 모듈을 import한 후엔 변경할 수 없음(그리고 이전에도, global과 local의 차이와 비슷). function 내에서 플라스크 응용 프로그램이 초기화된다면면 **커스텀화**할 수 있음. Flask application을 만드는 이 function을 application factory라고 함.
- 테스팅을 위해. `app`의 다른 인스턴스들을 생성.
- 한 프로세스에서 여러 인스턴스가 실행됨.
- `from app import app` -> circular imports 방지.

**Blueprint의 개념과 목적**

- 일반 프로젝트에서는 뷰, 템플릿, 모델 및 양식 등이 늘어남. 그것들을 분 할 수는 있지만 관련된 뷰, 템플릿, 모델 및 폼을 **그룹화**하는 것이 좋음. Blueprint는 Flask application을 모듈식으로 구성할 수있는 좋은 방법으로, 프로젝트 확장에 도움이 됨.
- prefix/subdomain parameter는 Blueprint의 모든 view function에서 공통적인 view argument(기본값 포함)가 될 수 있음.
- multiple times, different URL rules.
- applications or view functions을 implement하지 않아도 됨.

### url_shortener application의 기본적인 skeleton

    .
    ├── app
    │   ├── __init__.py
    │   ├── link
    │   │   ├── __init__.py
    │   │   ├── views.py
    │   ├── static
    │   └── templates
    │       ├── link
    │       └── index.html
    ├── run.py
    └── models.py

app 폴더는 웹 페이지의 소스코드입니다. 
git 