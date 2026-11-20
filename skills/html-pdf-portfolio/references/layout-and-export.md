# 레이아웃과 PDF 출력

본문은 HTML 정본 하나에서 편집한다. 템플릿의 `section.slide`가 PDF 한 페이지다. 각 페이지 안에 제목·본문·근거·출처를 두고 바닥 여백을 확보한다.

[디자인 첨삭 지침](design-review.md)의 타이포그래피·배경·벤토·검수 기준을 함께 적용한다. 템플릿에는 Pretendard Variable, 제목 60px(표지 72px), 본문 28px, 보조 22px, 캡션 18px이 실제 CSS로 적용돼 있다. 검증된 수치가 있을 때만 64~88px로 강조하고 지표·단위·조건을 함께 표시한다.

`python3 tools/prepare_documents.py output/application/v1 --kind portfolio`로 HTML과 폰트·라이선스를 준비한다. `assets/fonts/`를 함께 유지하고 실제 폰트 로드가 끝난 뒤 출력한다. 템플릿을 직접 열 때는 저장소의 공용 폰트를, 개인 출력본은 복사된 상대 경로의 폰트를 읽는다.

```css
.slide { width:1600px; height:900px; min-width:1600px; min-height:900px; container-type:size; }
@page { size:16.666667in 9.375in; margin:0; }
@media print {
  html,body,.deck { width:1600px; margin:0; padding:0; }
  .slide { zoom:1; break-after:page; break-inside:avoid; margin:0; box-shadow:none; }
  .slide:last-child { break-after:auto; }
  .controls { display:none; }
}
```

인쇄 시 화면 확대·축소를 1로 초기화한다. 페이지 내부의 글자나 이미지 크기에 `vw`·`vh`를 쓰지 않는다. 화면상 문서 전체에만 배율을 적용한다. 1600×900 CSS px은 PDF에서 약 1200×675pt이다.

템플릿은 외부 라이브러리 없이 열린다. 브라우저 인쇄에서 PDF 저장, CSS가 정한 용지 크기, 배경 그래픽 켜기, 머리글·바닥글 끄기를 확인한다. 자동 출력은 저장소의 `tools/export_pdf.py`를 사용할 수 있으나 스킬이 설치된 환경에 없으면 브라우저 인쇄로 진행한다.

PDF를 다시 열어 페이지 수·텍스트 선택·링크·폰트를 확인하고 모든 페이지를 이미지로 렌더링해 검사한다. 자동 검사는 기본 1~30페이지, 16:9, 링크 주석을 확인한다. 30페이지는 검사 한도일 뿐 목표 분량이 아니다. 제출 조건이 있으면 `--max-pages N`으로 실제 한도를 적용한다. 자동 검사 없이 눈으로만 확인했다면 그 범위를 보고한다.
