<template>
  <div class="about-container">
    <!-- 시험지 이미지 -->
    <div class="about-content">
      <div class="canvas-container">
        <img src="@/assets/시험지.png" alt="시험지 이미지" class="exam-image">
        <!-- Canvas 요소 -->
        <canvas ref="canvas" class="drawing-canvas"></canvas>
      </div>
    </div>
    <!-- 뒤로가기 버튼 -->
    <img src="@/assets/뒤로가기_1.png" alt="뒤로가기" class="back-button" @click="goBack">
    <!-- OMR 버튼 -->
    <img v-if="!showOverlay" src="@/assets/OMR.png" alt="OMR" class="omr-button" @click="toggleOverlay">
    <!-- 파란색 박스 -->
    <div class="b-box">
      <!-- 알림 아이콘 -->
      <img src="@/assets/알림.png" alt="알림 아이콘" class="notification-icon">
      <!-- 타이머 -->
      <div class="timer">{{ formattedTime }}</div>
      <!-- 타이머 버튼 -->
      <img v-if="!timerRunning" src="@/assets/재생버튼.png" alt="재생 버튼" class="timer-button" @click="startTimer">
      <img v-else src="@/assets/타이머.png" alt="일시정지 버튼" class="timer-button" @click="pauseTimer">
    </div>
    <!-- 페이지 넘김 버튼 -->
    <img src="@/assets/페이지넘김.png" alt="페이지 넘김" class="page-turn">
    <!-- 제출하기 버튼 -->
    <button class="submit-button" @click="goToFeedbackPage">제출하기</button>
    <!-- 검정색 투명 화면 -->
    <div v-if="showOverlay" class="overlay">
      <img src="@/assets/OMR실물.png" alt="OMR실물" class="omr-real">
      <!-- 닫기 버튼 -->
      <img src="@/assets/닫기.png" alt="닫기" class="close-button" @click="toggleOverlay">
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const timeLeft = ref(3600); // 1시간(60분 * 60초)
let timerInterval = null;
const timerRunning = ref(false);
const showOverlay = ref(false);

const canvas = ref(null);
let context = null;
let isDrawing = false;
let lastX = 0;
let lastY = 0;

const goBack = () => {
  router.push('/home');
}

const formatTime = (time) => {
  const hours = Math.floor(time / 3600);
  const minutes = Math.floor((time % 3600) / 60);
  const seconds = time % 60;
  return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

const startTimer = () => {
  timerRunning.value = true;
  timerInterval = setInterval(() => {
    if (timeLeft.value > 0) {
      timeLeft.value--;
    }
    if (timeLeft.value === 0) {
      clearInterval(timerInterval);
      timerRunning.value = false;
    }
  }, 1000);
}

const pauseTimer = () => {
  clearInterval(timerInterval);
  timerRunning.value = false;
}

const toggleOverlay = () => {
  showOverlay.value = !showOverlay.value;
}

const formattedTime = computed(() => formatTime(timeLeft.value));

const goToFeedbackPage = () => {
  router.push('/feedback');
}

onMounted(() => {
  if (canvas.value) {
    context = canvas.value.getContext('2d');
    canvas.value.width = canvas.value.offsetWidth;
    canvas.value.height = canvas.value.offsetHeight;

    canvas.value.addEventListener('mousedown', startDrawing);
    canvas.value.addEventListener('mousemove', draw);
    canvas.value.addEventListener('mouseup', stopDrawing);
    canvas.value.addEventListener('mouseout', stopDrawing);
  }
});

const startDrawing = (e) => {
  isDrawing = true;
  const rect = canvas.value.getBoundingClientRect();
  lastX = e.clientX - rect.left;
  lastY = e.clientY - rect.top;
};

const draw = (e) => {
  if (!isDrawing) return;
  context.strokeStyle = '#000'; // 그리기 색상 설정
  context.lineWidth = 2; // 그리기 선 두께 설정
  context.lineCap = 'round'; // 선 끝 모양 설정

  const rect = canvas.value.getBoundingClientRect();
  const currentX = e.clientX - rect.left;
  const currentY = e.clientY - rect.top;

  context.beginPath();
  context.moveTo(lastX, lastY);
  context.lineTo(currentX, currentY);
  context.stroke();

  lastX = currentX;
  lastY = currentY;
};

const stopDrawing = () => {
  isDrawing = false;
};
</script>

<style scoped>
.about-container {
  position: relative; 
  height: 100%;
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
  overflow-y: auto; /* 수직 스크롤 추가 */
  height: 100%;
  position: relative; /* 추가 */
}

.exam-image {
  width: 100%;
  height: auto;
}

.omr-button {
  position: absolute;
  top: 100px;
  left: 20px;
}

.close-button {
  position: absolute;
  top: 100px;
  left: 20px;
  z-index: 2;
}

.b-box {
  position: absolute;
  justify-content: center;
  top: 20px;
  right: 34px;
  display: flex;
  align-items: center;
  gap: 20px;
  z-index: 1; 
  background-color: #00068E;
  border-radius: 20px;
  width: 300px;
  height: 58px;
}

.notification-icon {
  width: 40px;
  height: 40px;
}

.timer {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 28px;
  color: white;
}

.timer-button {
  width: 42px;
  height: 42px;
}

.page-turn {
  position: absolute;
  bottom: 20px;
  left: 20px;
}

.submit-button {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 24px;
  position: absolute;
  bottom: 20px;
  right: 34px;
  width: 284px;
  height: 58px;
  background-color: #00068E;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); 
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1; 
}

.omr-real {
  max-width: 80%;
  max-height: 80%;
}

.canvas-container {
  position: relative;
  width: 100%;
  height: 100%;
}
.drawing-canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
