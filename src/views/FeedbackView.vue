<template>
  <div class="feedback-container">
    <!-- 뒤로가기 버튼 -->
    <img src="/src/assets/뒤로가기_1.png" alt="뒤로가기" class="back-button" @click="goToAboutPage">

    <!-- 화면 왼쪽 영역 - 시험지 이미지 -->
    <div class="test-paper-wrapper">
      <img src="/src/assets/시험지.png" alt="시험지" class="test-paper">
    </div>
    
    <!-- 화면 오른쪽 영역 -->
    <div class="sidebar" :style="{ width: sidebarWidth + 'px' }">
      <!-- 파란색 박스 -->
      <img :src="sidebarWidth === 40 ? '/src/assets/펼치기.png' : '/src/assets/사이드바닫기.png'" alt="펼치기" class="expand-icon" @click="toggleSidebarWidth">
      <!-- 사이드바 내용 -->
      <div v-if="sidebarWidth === 466" class="sidebar-content">
        <div class="text-input-container">
          <!-- 텍스트 입력 박스 -->
          <input type="text" class="text-input" placeholder="내용을 입력해주세요..." v-model="commentText">
          <!-- 댓글 버튼 -->
          <img src="/src/assets/댓글.png" alt="댓글" class="comment-button" @click="postComment">
        </div>
        <!-- 임시 댓글 박스 -->
        <div class="comment-wrapper">
          <div class="comment-box" v-for="(comment, index) in comments" :key="index">
            <div class="comment-header">
              <img src="/src/assets/임시프로필.png" alt="임시이미지" class="temp-image">
              <div class="user-name">{{ comment.user }}</div>
              <img src="/src/assets/마이너스.png" alt="마이너스" class="minus-icon">
            </div>
            <div class="comment-content">{{ comment.content }}</div>
          </div>
        </div>
      </div>
      <!-- 제출하기 버튼 -->
      <button class="submit-button" v-if="sidebarWidth === 466" @click="goToMainPage">제출하기</button>
    </div>
    <!-- 왼쪽 하단 페이지 넘김 아이콘 -->
    <img src="/src/assets/페이지넘김.png" alt="페이지 넘김" class="page-turn">
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import axios from 'axios';

const router = useRouter();
const sidebarWidth = ref(40);
const comments = ref([]);
const commentText = ref('');

const toggleSidebarWidth = () => {
  sidebarWidth.value = sidebarWidth.value === 40 ? 466 : 40;
}

const goToAboutPage = () => {
  router.push('/about');
}

const goToMainPage = () => {
  router.push('/');
}

const postComment = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/JSX/feedback/7/add', {
      content: commentText.value
    });
    // 데이터 전달 후 텍스트 리셋
    commentText.value = '';
    // 성공적으로 댓글이 추가된 경우, 댓글 목록 다시 불러오기
    loadComments();
  } catch (error) {
    console.error('Error posting comment:', error);
  }
}

const loadComments = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/JSX/feedback/7/contents/');
    comments.value = response.data.map(item => ({
      user: item.feedback_id.teacher_id.user_id.username,
      content: item.content
    }));
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// 페이지가 로드될 때 댓글을 불러오도록 설정
loadComments();
</script>

<style scoped>
.feedback-container {
  display: flex;
  position: relative;
}

.back-button {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 1;
}

.test-paper-wrapper {
  flex: 1;
  height: 834px;
  overflow-y: auto;
}

.test-paper {
  width: 100%;
}

.sidebar {
  flex-shrink: 0;
  height: 834px;
  background-color: #00068E; 
  position: relative;
}

.expand-icon {
  width: 14px;
  height: 28px;
  cursor: pointer;
  position: absolute;
  top: 50%;
  left: 10px;
}

.sidebar-content {
  padding: 40px 0px 0px 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.text-input-container {
  margin-bottom: 15px;
  position: relative;
  display: flex;
  align-items: center;
}

.text-input {
  font-family: "Pretendard Variable";
  font-weight: light;
  border-right: 2px solid rgb(0, 0, 0);
  flex: 1;
  height: 47px;
  width: 360px;
  border-radius: 20px;
  padding-left: 20px;
}

.comment-button {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  width: 30px;
  height: 30px;
  cursor: pointer;
}

.comment-wrapper {
  overflow-y: auto;
  max-height: 634px;
}

.comment-box {
  margin-top: 15px;
  background-color: white;
  padding: 10px;
  border-radius: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 360px;
}

.comment-header {
  display: flex;
  align-items: center;
}

.temp-image {
  width: 60px;
  height: 60px;
  margin-right: 10px;
}

.user-name {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 20px;
}

.minus-icon {
  margin-left: auto;
  width: 20px;
  height: 20px;
}

.comment-content {
  font-family: "Pretendard Variable";
  font-weight: light;
  font-size: 20px;
  margin-top: 5px;
  padding: 10px;
}

.submit-button {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 24px;
  width: 284px;
  background-color: #004BE1;
  color: white;
  border: none;
  border-radius: 10px;
  padding: 10px 0;
  cursor: pointer;
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
}

.page-turn {
  position: absolute;
  bottom: 20px;
  left: 20px;
}
</style>
