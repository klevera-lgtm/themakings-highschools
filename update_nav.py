"""
모든 HTML 파일의 nav를 최신 버전으로 일괄 업데이트
사용법: python update_nav.py [대상폴더]
"""
import os, sys, re
from pathlib import Path

NEW_NAV = '<nav class="header-nav" style="margin-left:0;">\n<a href="/seoul/">서울</a><a href="/incheon/">인천</a><a href="/gyeonggi/">경기</a><a href="/busan/">부산</a><a href="/daegu/">대구</a><a href="/daejeon/">대전</a><a href="/gwangju/">광주</a><a href="/ulsan/">울산</a><a href="/sejong/">세종</a><a href="/gangwon/">강원</a><a href="/gyeongnam/">경남</a><a href="/gyeongbuk/">경북</a><a href="/chungnam/">충남</a><a href="/chungbuk/">충북</a><a href="/jeonnam/">전남</a><a href="/jeonbuk/">전북</a><a href="/jeju/">제주</a>\n</nav>'

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')

updated = 0
skipped = 0

for html_file in sorted(root.rglob('*.html')):
    try:
        content = html_file.read_text(encoding='utf-8')
        # <nav class="header-nav"...> ~ </nav> 패턴을 정규식으로 찾아 교체
        new_content, count = re.subn(
            r'<nav class="header-nav"[^>]*>.*?</nav>',
            NEW_NAV,
            content,
            flags=re.DOTALL
        )
        if count > 0:
            html_file.write_text(new_content, encoding='utf-8')
            updated += 1
        else:
            skipped += 1
    except Exception as e:
        print(f"  오류: {html_file} — {e}")

print(f"✅ 업데이트: {updated}개")
print(f"⚠️  nav 없음 (건너뜀): {skipped}개")
