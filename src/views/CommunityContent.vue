<template>
  <div v-if="article">

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
          <div class="modal-header display">
            <img class="profile" img src="/src/assets/profile_content.jpg"></img>
            <!-- <div class="modal-margin"> -->
              <div style="margin-right: 10px;">
              <div style="font-size:40px; color: white;" class="font-bold"><b>{{ article.user_id.username }}</b></div>
              <div style="font-size:20px; color: white;" class="font-middle">{{ article.user_id.username }}님 9일 출석 완료!</div>
              </div>
              <section class="univ-logos">
                <img src="/src/assets/snu_logo.png" class="univ-img">
                <img src="/src/assets/ysu_logo.png" class="univ-img">
                <img src="/src/assets/kaist_logo.png" class="univ-img">
              </section>
            <!-- </div> -->

          </div>
          <div class="modal-body">
            <img src="/src/assets/study_check.png" width="700px" class="shadow" style="margin: 10px 0 20px 30px"></img>
          </div>
        </div>
      </div>
    </div>

    <div class="community-container">
    <div class="display">
<!-- 작성자 프로필 -->
      <div>
        <img class="profile" img src="/src/assets/profile_content.jpg" data-bs-toggle="modal" data-bs-target="#exampleModal">
      </div>
<!-- 작성자명, 작성 날짜 -->
      <div class="margin">
          <div style="font-size:40px;" class="font-bold"><b>{{ article.user_id.username }}</b></div>
          <div style="font-size:20px;" class="font-middle">{{ formatCreatedAt(article.created_at) }}</div>
        </div>
    </div>

<!-- 게시글 본문 -->
      <div style="margin: 8px 0 8px 30px; font-size: 18px;" class="font-middle">
          {{ article.content }}
      </div>

<!-- 이미지, 과목명 태그 -->
  <div>
      <div style="margin: 20px 0 8px 30px;" class="display justify-content-between">
        <div style="position: relative;">
          <img src="/src/assets/test2.jpg" width="70px" class="shadow"></img>

          <div style="position: absolute; top: 0px; left: 50px;">
            <img src="/src/assets/test1.jpg" width="70px" class="shadow"></img>
          </div>
        </div>
        <div class="tag font-middle" style="color: coral;"> 수학 </div>
      </div>
    </div>


<!-- 댓글/공유 아이콘, 답글 개수 -->
      <div style="margin: 30px 0 0 30px; font-size: 25px; color: grey;">
        <div class="display">
          <i class="fa-regular fa-message"></i>
          <div style="margin-right: 20px;"></div>
          <i class="fa-solid fa-share-from-square"></i>
          <div class="comment font-middle">답글 {{replyCount}}개</div>
        </div>
      </div>

      <hr>

<!-- 댓글 입력창 -->
<div style="width: 775px; margin-left: 25px; font-size: 18px; position: relative;" class="font-middle">
  <form action="" class="display" @submit.prevent="handleSubmit">
    <button class="send-button" style="position: absolute; top: 8px; right: 0;z-index: 100;">
      <img src="/src/assets/send.png">
    </button>
    <input type="text" placeholder="내용을 입력해주세요" class="comment-input" style="position: relative;" v-model="commentText">
  </form>
</div>

<!-- 댓글창 -->
    <div>
      <div class="comment-container" style="margin-left: 25px;">
        <div class="display">
          <img class="comment-profile" src="/src/assets/profile_comment.jpg" style="border: 1px solid lightgrey;">
          <div style="font-size:20px; margin-top: 17px;" class="font-middle"><b>{{ article.studycomment_set[0].user_id.username }}</b></div> <!-- 변경된 부분 -->
          <div class="comment-comment font-middle" style="font-size: 15px;">{{ formatCreatedAt(article.studycomment_set[0].created_at) }}</div> <!-- 변경된 부분 -->
        </div>

          <div style="margin: 0 18px 3px 18px; font-size: 18px;" class="font-middle">{{ article.studycomment_set[0].content }}</div>
        <div class="display">
          <div style="font-size: 20px; margin: 0 0 0 18px; color: grey;"><i class="fa-regular fa-message"></i></div>
          <div style="margin: 0 0 0 660px; color: grey;" class="font-middle">답글 0개</div>
        </div>
        </div>
    </div>

    <br>

    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';

const article = ref(null);
const replyCount = ref(0);
const commentText = ref('');

onMounted(async () => {
  try {
    const articleResponse = await axios.get('http://127.0.0.1:8000/JSX/articles/5/');
    article.value = articleResponse.data;
    const commentSumResponse = await axios.get('http://127.0.0.1:8000/JSX/articles/5/commentsum/');
    replyCount.value = commentSumResponse.data.comment_len;
    console.log(commentSumResponse.data.comment_len)
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});

const formatCreatedAt = (createdAt) => {
  const date = new Date(createdAt);
  return date.toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric'
  });
}

const handleSubmit = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/JSX/articles/2/comments/', {
      content: commentText.value // 사용자가 입력한 댓글
    });
    // 요청 성공 시, 추가 작업 수행 가능
    commentText.value = ''; // 입력 필드 초기화
  } catch (error) {
    console.error('Error posting comment:', error);
  }
}
</script>

<style lang="scss" scoped>

// modal style
.modal-header{
  width: 100%;
  height: 160px;
  background-color: #00068E;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
}

.univ-logos{
  background-color: rgb(204, 204, 204);
  width: 350px;
  border-radius: 15px;
  padding: 2%;
  margin: 20px 0 20px 20px;
  justify-content: space-evenly;
}

.univ-img{
  background-color: white;
  border-radius: 50%;

  width: 80px;
  height: 80px;
  margin-left: 20px;

  position: relative;
}

.font-bold{
  font-family: "Pretendard Variable";
  font-weight: bold;
}

.font-middle{
  font-family: "Pretendard Variable";
  font-weight: middle;
}

.font-light{
  font-family: "Pretendard Variable";
  font-weight: light;
}

.profile{
  border-radius: 100px;
  width: 150px;
  padding: 20px;
}

.comment-profile{
  border-radius: 100px;
  width: 50px;
  padding: 3px;
  margin: 10px;
}

.tag{
  margin: 68px 30px 0 0;
  border-radius: 15px;
  height: 35px;
  width: 70px;
  background-color: rgb(255, 239, 241);
  text-align: center;
  font-size: 20px;
  border: 10px;
}

.shadow{
  box-shadow: 5px 5px 5px 5px black;
  border-radius: 10px;
}

.margin{
  margin-top: 23px;
}

.modal-margin{
  margin-top: 10px;
}

.community-container{
  background-color: rgba(255, 255, 255, 0.5);
  box-shadow: 4px 4px 4px 4px lightgrey;
  border-radius : 10px;
  width: 850px;
  height: 665px;
  margin-top: -2%;
  margin-right: 5%;
  float: right;
  overflow-y: auto;
}

.comment-container{
  background-color: white;
  box-shadow: 1px 1px 1px 1px lightgrey;
  border-radius : 10px;
  width: 775px;
  height: 175px;
  margin-top: 13px;
}

.comment-comment-container{
  background-color: white;
  box-shadow: 1px 1px 1px 1px lightgrey;
  border-radius : 10px;
  width: 700px;
  height: 175px;
  margin: 13px 0 0 96px;
}

.comment{
  margin-left: 620px;
  font-size: 20px;
}

.comment-comment{
  margin-left: 400px;
  margin-top: 22px;
  font-size: 20px;
}

.comment-comment-comment{
  margin-left: 409px;
  margin-top: 22px;
  font-size: 20px;
}

.display{
  display: flex;
}

.comment-input{
  font-family: "Pretendard Variable";
  width:800px;
  height:50px;
  font-size:15px;
  border-radius: 15px;
  padding: 17px;
}

.send-button{
  border: none;
  outline: none;
  background-color: inherit ;
  cursor: pointer;
}
</style>