from bs4 import BeautifulSoup

html = '''
<tr>
<th rowspan="2" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Name
</th>
<th rowspan="2" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Developer
</th>
<th rowspan="2" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Initial release
</th>
<th colspan="2">Latest release
</th>
<th rowspan="2" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><a href="/wiki/Programming_language" title="Programming language">Program­ming language</a>
</th>
<th rowspan="2" data-sort-type="currency" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Cost (<a href="/wiki/United_States_dollar" title="United States dollar">US$</a>)
</th>
<th rowspan="2" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><a href="/wiki/Software_license" title="Software license">License</a>
</th>
<th rowspan="2" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><a href="/wiki/Graphical_user_interface" title="Graphical user interface">GUI</a>
</th>
<th rowspan="2" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><a href="/wiki/Text-based_user_interface" title="Text-based user interface">TUI</a> or <a href="/wiki/Command-line_interface" title="Command-line interface">CLI</a>
</th></tr><tr>
<th data-sort-type="number" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Version
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Date
</th>
</tr>
'''

soup = BeautifulSoup(html, 'html.parser')

# 첫 번째 tr 태그 안의 th 태그들을 추출
headers = [th.get_text(strip=True) for th in soup.select('tr:first-child th')]
print(f"First_Row_Headers: {headers}")

# 두 번째 tr 태그 안의 th 태그들을 추출
second_row_headers = [th.get_text(strip=True) for th in soup.select('tr:nth-child(2) th')]
print(f"Second_Row_Headers: {second_row_headers}")

# 'Latest release' 합치기
latest_release_index = headers.index('Latest release')
headers[latest_release_index:latest_release_index+1] = [f'Latest release: {hdr}' for hdr in second_row_headers]

print(headers)
