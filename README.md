#  1주차 수업 내용 정리
## 1. 웹 브라우저 원리
브라우저는 도메인값을 사용자가 입력하고 요청하는 순간 어떠한 컴퓨터에 요청을 보내고 요청받은 내용을 그 컴퓨터에서 가져와서 보여주는 것이 브라우저의 역할

사용자가 보는 웹 페이지는 모두 서버에서 미리 준비해 두었던 것을 받아서 브라우저에서 우리가 볼 수 있도록 그려주는 역할을 수행함

▶ 브라우저는 요청을 보내고, 요청의 답으로 받은 HTML 파일을 그려주는 일을 함

브라우저가 요청을 보내는 곳은?

▶ 서버가 만들어 놓은 API라는 창구에 미리 정해진 약속대로 요청을 보냄

▶ 우리가 웹을 쓰는 동안 주소 창에 주소를 입력하고 엔터를 입력하면 서버로 요청을 보내게 됨

▶ ex) http://naver.com
           - 이것은 "naver.com"이라는 이름의 서버에 있는 "/"라는 주소 창구에 요청을 보낸 것
           - 네이버에서 그 대답으로 네이버 홈에 해당하는 HTML 파일을 줌

사용자가 보는 브라우저는 주소를 통해 API로 요청을 보내고, API는 요청에 맞는 HTML파일을 돌려주고 브라우저는 받은 받은 파일을 화면에 그려줌

## 2. HTML, CSS 기본 내용

ⅰ.  HTML과 CSS개념

HTML은 웹의 뼈대를 잡아주는 구역을 나태는 코드이고, 웹의 전반을 HTML을 통해서 작성할 수 있음

CSS는 HTML을 통해 작성된 뼈대의 속성을 선택해 예쁘게 꾸며주는 코드

HTML 내 style 속성으로 꾸미기를 할 수 있지만, HTML 코드 내에 CSS 파일을 불러와서 적용할 수 있음

HTML은 뼈대, CSS는 꾸미기!!

ⅱ.  HTML 기초

HTML은 크게 head와 body로 구성됨

▶ head태그 안에는 페이지의 속성정보를 body태그 안에는 페이지의 내용을 담음

head 안에 들어가는 대표적인 요소

▶ meta 태그
- 웹 서버와 웹 브라우저간에 상호 교환되는 정보를 정의하는 데 사용
- HTML 문서의 head 안에 입력하는 특수 태그로 사이트의 디자인에는 전혀 영향을 미치지 않고 문서가 어떤 내용을 담고 있고, 문서의 키워드는 무엇이며, 누가 만들었는지 등의 문서 자체의 특성을 담음

▶ script 태그
- 자바스크립트와 같은 클라이언트 사이드 스크립트(client-side scripts)를 정의할 때 사용
- script태그는 스크립트 코드를 요소 내부에 직접 명시하거나, src 속성을 사용하여 외부 스크립트 파일을 참조할 수 있지만 src 속성이 명시된 script 태그 안에는 스크립트 코드를 직접 명시하면 안 됨

▶ link 태그
- 해당 문서와 외부 소스(external resource) 사이의 관계를 정의할 때 사용
- link태그는 빈 태그이며, 속성만을 포함하고, head태그 요소 내부에만 위치할 수 있으며, 그 개수는 제한이 없음
- 주로 외부 스타일 시트(external style sheet)를 연결할 때 사용됨

▶ title 태그
- 브라우저의 탭에 표시될 제목을 적는 태그
- 웹페이지 본문에는 보이지 않고, 브라우저의 탭 등에서 확인할 수 있음
- 사용자에게 문서의 제목을 알리는 용도뿐만 아니라, 검색 엔진 등에서 가장 크게 보이는 텍스트이므로 페이지의 특성을 드러내는 제목을 작성하는 게 중요함

#### Html을 시작할 때 파일을 생성한 후 html을 입력하면 자동완성 부분에  html:5 클릭하면 기본 뼈대가 완성

ⅲ.  CSS기초

HTML 부모 자식 구조

▶  html 태그는 누가 누구 안에 있느냐를 이해하는 것이 가장 중요

▶  해당 태그를 감싸고 있는 태그가 바뀌면 그 안의 내용물도 모두 영향을 받음

▶  아래 그림처럼 상위 태그에 스타일을 적용하면 하위 태그도 같이 적용되고 하위 태그에 적용한 내용은 위에 태그에 적용되지 않음 

           => 스타일 시트를 어디에 적용하냐에 따라서 CSS가 하위 태그에 적용됨(계층식 구조)

CSS계층식 구조 설명

CSS(Cascading Style Sheets, 계층식 스타일 시트)란?

▶  HTML 문서의 스타일을 적용하기 위해 사용하는 양식

▶  웹문서에서 스타일이란, 문서에서 사용하는 글꼴이나 색상, 정렬 방식, 요소의 배치 방법 등을 결정하는 데 사용됨

▶   웹문서의 내용과 스타일은 함께 웹문서를 구성하는 요소이자 양식으로 사용되지만, 역할은 완벽히 구분되어 있음. 따라서, CSS의 내용이 바뀌어도 웹문서의 내용 자체에는 영향을 끼치지 않음

CSS 사용 방법은 <head> 태그 안에 <style> </style>로 공간을 만들어서 작성함

link 태그를 사용하여 따로 작성한 CSS파일과 html 문서를 합칠 수 있음

link 태그로 연결할 땐 속성으로 href, rel을 작성하는데 href에는 연결하고 싶은 파일명을, rel에는 연결한 파일이 무엇인지 작성하는데 보통은 stylesheet라고 작성함

각 태그에 style 속성을 지정할 수도 있음

CSS 속성을 적용하는 기본 양식

▶  선택자 {
            속성명: 속성값;
        }
           
▶ 선택자 : 스타일을 적용하고 싶은 대상, 태그, 아이디, 클래스 등으로 선택할 수 있음
           
▶ {} 중괄호 : 이 안에 선택된 요소에 대한 스타일을 적음
           
▶ 속성명 : 크기, 색상, 위치 등 바꾸고 싶은 스타일 관련 속성을 적음
           
▶ 속성값 : 해당 속성에 어떤 값을 지정할지 적음
           
많이 쓰는 CSS
 
★ 배경 관련  
background-color  
background-image  
background-size  
★ 사이즈     
width         
height        
★ 폰트  
font-size : 글씨 크기        
font-weight : 글씨 두께  
font-family : 글씨체  
color : 글씨색상  
★ 간격  
margin : 바깥쪽 여백  
padding : 안쪽여백  
★ 가운데 정렬  
display : flex;  
flex-direction: column;  
align-items: center;  
           
ⅴ. 꿀팁  
주석 달기  
주석이란?  
필요 없어진 코드를 삭제하는 대신 임시로 작동하지 못하게 하고 싶을 때나 코드에 대한 간단한 설명을 붙여두고 싶을 때 사용  
주석을 붙여놓으면 컴퓨터나 브라우저가 읽지는 않고 개발자를 위해서 붙여두는 것  
주석 단축키 : 주석처리하고 싶은 라인을 선택한 후 window => ctrl + /   |   mac => command + /  
window에서 ctrl + / 로 주석처리가 안 되는 경우에는 언어기본설정을 한컴입력기가 아니라 Microsoft 입력기로 설정을 변경하면 가능해짐  
코드 정렬하기  
window => shift + alt + f    |    mac => shift + option + f  

ⅵ. bootstrap

bootstrap이란?  
▶ 예쁜 CSS를 미리 모아둔 것  
▶ CSS를 다룰 줄 아는 것과, 미적 감각을 발휘하여 예쁘게 만드는 것은 다르기 때문에 미리 완성된 부트스트랩을 가져다 쓰는 경우가 많음  
bootstrap 시작 템플릿   
<!doctype html>  
<html lang="en">  
<head>  
    <meta charset="utf-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">  
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"  
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">  
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"  
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"  
        crossorigin="anonymous"></script>  
    <title></title>  
</head>  
<body>  
부트스트랩 사용하기  
▶  부트스트랩을 사용할 파일에 <head> 태그 안에 부트스트랩 링크와 스크립트를 붙여 놓음  
▶  부트스트랩에 들어가 원하는 것을 찾음  
▶  복사한 내용을 자신이 넣길 원하는 부분에 붙여 넣기 함  
ⅶ. 웹 페이지 Github를 통해서 배포해 보기  
Github란?  
▶  인터넷에서 코드를 업로드할 수 있는 사이트이며 동시에 이 코드를 배포해서 홈페이지처럼 접속할 수 있음  
▶  협업을 할 때 코드를 올려놓을 장소가 필요한데 Github를 이용해서 코드 관리를 많이 함  
배포하기  
저장소 생성하기  
▶  Create Repository를 선택  
▶   public을 선택하고 생성  
파일 업로드하기
▶  Upload Exsiting Files를 선택   
▶  finder 혹은 윈도 탐색기에서 index.html, index.js 파일을 드래그 앤 드롭으로 업로드  
배포하기  
▶  저장소에서 settings로 들어감   
▶  settings 화면 왼쪽 부분에 page를 찾아서 클릭  
▶  Deploy from a branch를 선택  
▶  Branch Name을 main으로 설정하고 save 버튼을 누름  
▶ 기다렸다가 새로고침 하면 주소가 노출됨  
※ Github를 통해서 배포할 땐 반드시 파일은 1개여야 하고 파일명은 index.html로 작성  
수정하기  
▶  code로 들어가서 연필모양을 누름  
▶  ctrl + a를 해서 전체를 삭제  
▶  새로운 코드를 다시 붙여 넣고 Commit changes 누르기  
