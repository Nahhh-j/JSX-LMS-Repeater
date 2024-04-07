<template>
  <div class="box">
    <!-- 헤더 -->
    <header class="header">
      <!-- 네비게이션 바 -->
      <nav class="p-3">
        <div class="nav-icons">
          <img src="/src/assets/back_icon.png" class="nav-icon" @click="goBack" alt="뒤로가기">
          <img src="/src/assets/calender_icon.png" class="nav-icon" alt="">
        </div>
      </nav>

      <!-- 총 학습시간 -->
      <div class="total-time">
        {{ formatTime(totalStudyTime) }}
      </div>
    </header>

    <!-- 타이머 -->
    <section class="timer">
      타이머
    </section>

    <!-- 과목별 타이머 -->
    <section class="subject-timers">
      <div v-for="(subject, index) in subjects" :key="index">
        <div class="d-flex s-between">
          <div class="d-flex">
            <img :src="getButtonImage(subject.isRunning, subject.color)" class="m-10px" alt="" @click="toggleTimer(index)">
            <div class="subject-name">{{ subject.name }}</div>
          </div>
          <div class="subject-timer">{{ formatTime(subject.time) }}</div>
        </div>
        <hr> <!-- 각 과목 아래에 구분선 추가 -->
      </div>
    </section>

    <!-- (+) 버튼 -->
    <div class="plus" @click="showModal">
      <button class="add-button" @click="addSubject" v-show="isModalVisible"></button>
      <img src="/src/assets/plus_icon.png" alt="">
    </div>

    <!-- 검정 투명창 -->
    <div class="overlay" v-if="isModalVisible" @click="hideModal"></div>

    <!-- 텍스트 입력창 -->
    <div class="textinput" v-if="isModalVisible">
      <input type="text" placeholder="카테고리 이름을 입력해주세요." v-model="newSubjectName">
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isModalVisible: false,
      subjects: [],
      totalStudyTime: 0,
      newSubjectName: '',
      runningTimerIndex: null // 실행 중인 타이머의 인덱스 저장
    };
  },
  mounted() {
    this.fetchSubjectStudyTime();
  },
  methods: {
    goBack() {
      this.$router.push('/');
    },
    showModal() {
      this.isModalVisible = true;
    },
    hideModal() {
      this.isModalVisible = false;
    },
    toggleTimer(index) {
      const subject = this.subjects[index];
      if (subject.isRunning) {
        clearInterval(subject.timerId);
        // 현재 실행 중인 타이머가 해당 과목의 타이머인 경우에만 실행 중인 타이머 ID 초기화
        if (this.runningTimerId === subject.timerId) {
          this.runningTimerId = null;
        }
      } else {
        // 현재 실행 중인 타이머가 있으면 멈춤
        if (this.runningTimerId !== null) {
          clearInterval(this.runningTimerId);
          // 이전에 실행 중이던 타이머의 버튼 이미지를 stop.png로 변경
          const previousSubject = this.subjects.find(s => s.timerId === this.runningTimerId);
          if (previousSubject) {
            previousSubject.isRunning = false;
          }
        }
        subject.timerId = setInterval(() => {
          subject.time++;
          this.totalStudyTime++;
        }, 1000);
        // 현재 실행 중인 타이머의 ID 저장
        this.runningTimerId = subject.timerId;
      }
      subject.isRunning = !subject.isRunning;
    },
    formatTime(time) {
      const hours = Math.floor(time / 3600);
      const minutes = Math.floor((time % 3600) / 60);
      const seconds = time % 60;
      return `${hours.toString().padStart(2, '0')} : ${minutes.toString().padStart(2, '0')} : ${seconds.toString().padStart(2, '0')}`;
    },
    async fetchSubjectStudyTime() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/JSX/manage/subject-study-time/');
        this.subjects = response.data.map((subject, index) => ({
          name: subject.subject_name,
          color: ['red', 'orange', 'yellow', 'green'][index % 4], // % 연산자를 사용하여 색상을 순환하도록 수정
          time: 0,
          timerId: null,
          isRunning: false
        }));
      } catch (error) {
        console.error('Error fetching subject study time:', error);
      }
    },
    async addSubject() {
      try {
        await axios.post('http://127.0.0.1:8000/JSX/manage/subject/', { subject_name: this.newSubjectName });
        this.fetchSubjectStudyTime();
        this.hideModal();
      } catch (error) {
        console.error('Error adding subject:', error);
      }
    },
    getButtonImage(isRunning, color) {
      return `/src/assets/${isRunning ? 'stop_' : 'play_'}${color}.png`;
    }
  }
};
</script>

<style lang="scss" scoped>
.header{
  background-color: #00068E;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px; 
  height: 30%;
}

.box{
  position: relative;
  height: 100%;
  background-color: white;
}

.nav-icons{
  display: flex;
  justify-content: space-between;
}

.nav-icon{
  width: 75px;
  cursor: pointer;
}

.total-time{
  border: none;
  padding: 2%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 50px;
  color: white;
}

.subject-timers{
  overflow: auto;
  background-color: white;
  height: 60%;
  margin-top: 10px;
}

.subject-timer{
  padding: 20px;
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 30px;
  color: gray;
}

.timer {
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2%;
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 30px;
  color: gray;
  height: 10%;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.subject-name{
  padding: 20px 20px 10px 20px;
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 30px;
  width: 800px;
}


.plus{
  position: absolute;
  top: 730px;
  left: 90%;
  z-index: 1000;
}

hr{
  margin: 10px;
}

.container {
  width: 1194px;
  max-height: 834px;
  margin: 0 auto;
  border: 1px solid black;
  background-color: #F6F8FF;
  overflow: hidden;
}

.background{
  background-color: #00068E
}

.back-white{
  background-color: white;
}


.bor-none{
  border: none;
}

.bor-gray{
  border: 1px solid gray;
}

.b-circle{
  border-radius: 100%;
}

.b-radius{
  border-radius: 10%;
}

.s-between{
    justify-content: space-between;
}

.s-evenly{
  justify-content: space-evenly;
}

.right{
  float: right;
}

.i-center{
  display: flex;
  justify-content: center;
  align-items: center;
}

.d-column{
  display: flex;
  flex-direction: column;
}

.white{
  color: white;
}

.gray{
  color: gray;
}

.bold{
  font-weight: bold;
}

.p-20px{
  padding: 20px;
}

.p-30px{
  padding: 30px;
}

.m-0auto{
  margin: 0 auto 0 auto;
}

.m--10{
  margin: 0 10px 0 10px;
}

.m-10px{
  margin: 15px 20px 10px 20px;
  height: 65px;
  width: 65px;
}

.m-20px{
  margin: 20px 20px 20px 20px;
}

.m-30px{
  margin: 30px 30px 30px 30px;
}

.w-30px{
  width: 30px;
}

.w-50px{
  width: 50px;
}

.w-5pc{
  width: 5%;
}

.w-10pc{
  width: 10%;
}

.w-20pc{
  width: 20%;
}

.w-30pc{
  width: 30%;
}

.w-40pc{
  width: 40%;
}

.w-50pc{
  width: 50%;
}

.w-80pc{
  width: 80%;
}

.w-100pc{
  width: 100%;
}

.h-30pc{
  height: 30%;
}

.h-100pc{
  height: 100%;
}

.f-20px{
  font-size: 20px;
}

.f-25px{
  font-size: 25px;
}

.f-30px{
  font-size: 30px;
}

.f-50px{
  font-size: 50px;
}

.f-50pc{
  font-size: 50%;
}
 
.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 999; 
}

.textinput {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 20px;
  position: absolute;
  top: 92%;
  right: 7%;
  transform: translateY(-50%);
  z-index: 999;
}

.textinput input {
  width: 523px;
  height: 60px;
  padding: 16px;
  border-radius: 15px;
}

.add-button {
  position: absolute;
  border: none;
  background: transparent;
  cursor: pointer;
  z-index: 9999;
  right: 2px;
  width: 76px;
  height: 76px;
}
</style>