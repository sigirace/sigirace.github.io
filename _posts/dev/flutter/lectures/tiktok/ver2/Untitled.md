Home

- 글이 파이어 스토어에서 로드됨
- 이미지가 파이어베이스에서 로드됨



Write



글

- 이미지 주소
- 텍스트
- 사용자 - 프로필





1. User
   1. user_id (uid)
      1. email
      2. hasAvatar -> update
      3. name
      4. followcount -> cloud function (미구현)
      5. followers -> cloud function (미구현)
         1. user_id (uid)
      6. posts -> cloud function
         1. post_id
2. Post 
   1. post_id (uid)
      1. content
      2. images -> cloud function
         1. image_url (publicUrl)
      3. createUser: user_id(uid)
      4. replyCount
      5. replies
         1. reply_id (uid)
      6. likeCount  -> cloud function (미구현)
      7. likes  -> cloud function (미구현)
         1. user_id (uid)
      8. InnerPost
         1. post_id (uid)
3. Reply
   1. reply_id (uid)
      1. content
      2. createUser: user_id(uid)
      3. likeCount   -> cloud function (미구현)
      4. likes   -> cloud function (미구현)
         1. user_id (uid)