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
        07 : 43 : 32
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
            <img :src="'/src/assets/' + (subject.isRunning ? 'stop_' : 'play_') + subject.color + '.png'" class="m-10px" alt="" @click="toggleTimer(index)">
            <div class="subject-name">{{ subject.name }}</div>
          </div>
          <div class="subject-timer">{{ formatTime(subject.time) }}</div>
        </div>
        <hr> <!-- 각 과목 아래에 구분선 추가 -->
      </div>
    </section>

    <!-- (+) 버튼 -->
    <div class="plus" @click="showModal">
      <img src="/src/assets/plus_icon.png" alt="">
    </div>

    <!-- 검정 투명창 -->
    <div class="overlay" v-if="isModalVisible" @click="hideModal"></div>

    <!-- 텍스트 입력창 -->
    <div class="textinput" v-if="isModalVisible">
      <input type="text" placeholder="카테고리 이름을 입력해주세요.">
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isModalVisible: false,
      subjects: [
        { name: '국어', color: 'red', time: 0, timerId: null, isRunning: false },
        { name: '영어', color: 'orange', time: 0, timerId: null, isRunning: false },
        { name: '수학', color: 'yellow', time: 0, timerId: null, isRunning: false },
        { name: '한국사', color: 'green', time: 0, timerId: null, isRunning: false },
        { name: '운동', color: 'green', time: 0, timerId: null, isRunning: false },
        { name: '코딩', color: 'green', time: 0, timerId: null, isRunning: false }
      ]
    };
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
      } else {
        subject.timerId = setInterval(() => {
          subject.time++;
        }, 1000);
      }
      subject.isRunning = !subject.isRunning;
    },
    formatTime(time) {
      const hours = Math.floor(time / 3600);
      const minutes = Math.floor((time % 3600) / 60);
      const seconds = time % 60;
      return `${hours.toString().padStart(2, '0')} : ${minutes.toString().padStart(2, '0')} : ${seconds.toString().padStart(2, '0')}`;
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
</style>