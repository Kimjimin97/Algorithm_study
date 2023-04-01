-- 코드를 입력하세요

# 도서 정보 book
# 저자 정보 author


SELECT b.book_id , a.author_name, DATE_FORMAT(b.published_date,'%Y-%m-%d')
FROM  BOOK AS b LEFT JOIN AUTHOR AS a
ON b.AUTHOR_ID = a.AUTHOR_ID
WHERE b.category = "경제"
ORDER BY published_date asc