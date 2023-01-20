- `pip install jupyterthemes`
- jt -t monokai -f roboto -fs 11 -tfs 11 -ofs 10 -cursc o -cursw 4 -cellw 90% -lineh 170 -T
- `pip install jupyter_contrib_nbextensions`
- `jupyter contrib nbextension install --user`
- user 폴더내에 .jupyter 확인
- .jupyter - custom - custom.css 파일에서 상세 설정
- 툴바와 목차 겹치지 않게
``` css
#toc-wrapper {
  top:100px !important;
}
div#maintoolbar {
  margin-left: -20px !important;
  background: transparent !important;
  width: 100% !important;
  padding-left: 25px !important;
}
```
- 주석 글씨색 변경
``` css
.cm-s-ipython span.cm-comment {
 color: #B2B2B2;
 font-style: italic;
}
```
  