<template>
  <div class="about-container">
    <!-- 시험지 이미지 -->
    <div class="about-content">
      <img src="@/assets/시험지.png" alt="시험지 이미지" class="exam-image">
    </div>
    <!-- 뒤로가기 버튼 -->
    <img src="@/assets/뒤로가기_1.png" alt="뒤로가기" class="back-button" @click="goBack">
    <!-- 파란색 박스 -->
    <div class="blue-box">
      <!-- 알림 아이콘 -->
      <img src="@/assets/알림.png" alt="알림 아이콘" class="notification-icon">
      <!-- 타이머 -->
      <div class="timer">{{ formattedTime }}</div>
      <!-- 타이머 버튼 -->
      <img src="@/assets/타이머.png" alt="타이머 버튼" class="timer-button">
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const goBack = () => {
  router.go(-1);
}

let timeLeft = 3600; // 1시간(60분 * 60초)

const formatTime = (time) => {
  const minutes = Math.floor(time / 60);
  const seconds = time % 60;
  return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

setInterval(() => {
  if (timeLeft > 0) {
    timeLeft--;
  }
}, 1000);

const formattedTime = formatTime(timeLeft);
</script>

<style scoped>
.about-container {
  position: relative; 
}

.back-button {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 1; /* 다른 내용 위에 배치 */
}

.about-content {
  width: 100%;
  max-width: 1194px; 
  margin: 0 auto;
}

.exam-image {
  width: 100%;
  height: auto;
}

.blue-box {
  position: absolute;
  top: 20px;
  right: 20px;
  display: flex;
  align-items: center;
  gap: 20px;
  z-index: 1; 
}

.notification-icon {
  width: 40px;
  height: 40px;
}

.timer {
  font-size: 24px;
  color: white;
}

.timer-button {
  width: 40px;
  height: 40px;
}
</style>
