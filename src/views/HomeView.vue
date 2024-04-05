<template>
  <div>
    <div class="navbar">
      <img src="@/assets/뒤로가기.png" class="back-button" @click="goBack" alt="뒤로가기">
      <img src="@/assets/로고.png" class="logo" alt="로고">
    </div>
    <div class="white-box">
      <div class="section left-section">
        <p class="title" style="margin-bottom: 0rem;">문제 풀이 완료</p>
        <div class="count">
          <p class="big-number" style="margin-bottom: 0rem;">3</p>
          <p class="small-text">건</p>
        </div>
        <button class="blue-button" style="margin-bottom: 0rem;">문제 풀이 완료 건수</button>
      </div>
      <div class="separator"></div>
      <div class="section right-section">
        <p class="title" style="margin-bottom: 0rem;">1 : 1 피드백 완료</p>
        <div class="count">
          <p class="big-number" style="margin-bottom: 0rem;">1</p>
          <p class="small-text">건</p>
        </div>
        <button class="blue-button">피드백 완료 건수</button>
      </div>
    </div>
    <div class="gray-box">
      <button class="gray-button" :class="{ 'selected': selectedButton === '국어' }" @click="selectButton('국어')">국어</button>
      <button class="gray-button" :class="{ 'selected': selectedButton === '영어' }" @click="selectButton('영어')">영어</button>
      <button class="gray-button" :class="{ 'selected': selectedButton === '수학' }" @click="selectButton('수학')">수학</button>
    </div>
    <div class="scrollable-white-box">
      <!-- 데이터 1 -->
      <div class="divider"></div>
      <div class="data-container">
        <div class="left-data" style="text-align: center; margin-top: -70px;">
          <p>2023년 고3 3월 언어와 매체</p>
        </div>
        <div class="right-data">
          <div class="blue-box">
            <div class="content">
              <img src="@/assets/다운로드.png" alt="이미지">
              <p>문제</p>
            </div>
            <div class="content">
              <img src="@/assets/다운로드.png" alt="이미지">
              <p>정답</p>
            </div>
            <div class="content">
              <img src="@/assets/다운로드.png" alt="이미지">
              <p>해설</p>
            </div>
          </div>
          <div class="buttons">
            <router-link to="/about" class="action-button">응시하기</router-link>
            <button class="action-button">이어서풀기</button>
          </div>
        </div>
      </div>
      <div class="divider"></div>
      
      <!-- 데이터 2 -->
      <div class="data-container">
        <div class="left-data" style="text-align: center; margin-top: -70px;">
          <p>2023년 고3 3월 언어와 매체</p>
        </div>
        <div class="right-data">
          <div class="blue-box">
            <div class="content">
              <img src="@/assets/다운로드.png" alt="이미지">
              <p>문제</p>
            </div>
            <div class="content">
              <img src="@/assets/다운로드.png" alt="이미지">
              <p>정답</p>
            </div>
            <div class="content">
              <img src="@/assets/다운로드.png" alt="이미지">
              <p>해설</p>
            </div>
          </div>
          <div class="buttons">
            <router-link to="/about" class="action-button">응시하기</router-link>
            <button class="action-button">이어서풀기</button>
          </div>
        </div>
      </div>
      <div class="divider"></div>

      <!-- 데이터 3 -->
      <div class="data-container">
        <div class="left-data" style="text-align: center; margin-top: -70px;">
          <p>2023년 고3 3월 언어와 매체</p>
        </div>
        <div class="right-data">
          <div class="blue-box">
            <div class="content">
              <img src="@/assets/다운로드.png" alt="이미지">
              <p>문제</p>
            </div>
            <div class="content">
              <img src="@/assets/다운로드.png" alt="이미지">
              <p>정답</p>
            </div>
            <div class="content">
              <img src="@/assets/다운로드.png" alt="이미지">
              <p>해설</p>
            </div>
          </div>
          <div class="buttons">
            <router-link to="/about" class="action-button">응시하기</router-link>
            <button class="action-button">이어서풀기</button>
          </div>
        </div>
      </div>
      <div class="divider"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      selectedButton: '국어'
    };
  },
  methods: {
    goBack() {
      this.$router.push('/');
    },
    selectButton(button) {
      this.selectedButton = button;
    },
  },
  mounted() {
    this.selectedButton = '국어';
  }
}
</script>

<style>
.navbar {
  width: 100%;
  height: 120px;
  background-color: #00068E;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
}

.back-button {
  width: 75px;
  height: auto;
}

.logo {
  width: 120.22px;
  height: auto;
  margin: 0 auto;
}

.white-box {
  width: calc(100% - 40px);
  margin: 20px auto 0;
  background-color: #FFFFFF;
  border: 1.5px solid #B2B2B2;
  border-radius: 20px;
  display: flex;
  justify-content: space-between;
  padding: 20px;
}

.section {
  text-align: center;
}

.left-section,
.right-section {
  flex: 1;
}

.separator {
  width: 1px;
  background-color: #B2B2B2;
  margin: 0 20px;
}

.title {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 40px;
  color: #000000;
}

.count {
  display: flex;
  align-items: baseline;
  justify-content: center;
}

.big-number {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 90px;
  font-weight: bold;
  color: #00068E;
  margin-right: 5px;
}

.small-text {
  font-family: "Pretendard Variable";
  font-weight: light;
  font-size: 30px;
  color: #3E3D3D;
}

.blue-button {
  font-family: "Pretendard Variable";
  font-weight: bold;
  background-color: #00068E;
  color: #FFFFFF;
  border: none;
  padding: 10px 30px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 24px;
}

.gray-box {
  margin: 20px auto 0;
  width: 100%;
  background-color: #3E3E3E;
  display: flex;
  justify-content: space-around;
  padding: 10px 0;
}

.gray-button {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 35px;
  background-color: #4A4A4A;
  color: #FFFFFF;
  width: 306px;
  border: none;
  padding: 10px 20px;
  border-radius: 10px;
  cursor: pointer;
}

.gray-button.selected {
  background-color: #FFFFFF;
  color: #000000;
}

.scrollable-white-box {
  overflow-y: auto;
  max-height: 255px;
  background-color: #FFFFFF;
}

.data-container {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.left-data {
  font-family: "Pretendard Variable";
  font-weight: light;
  flex: 1;
  font-size: 40px;
}

.right-data {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.blue-box {
  width: 590px;
  height: 76px;
  background-color: #00068E;
  display: flex;
  border-radius: 5px;
  justify-content: center; 
  align-items: center;
}

.content {
  flex: 1;
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: center;
  border-right: 1px solid white;
  height: 80%; 
}

.content img {
  width: 33px;
}

.content p {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 24px; 
  color: #FFFFFF;
  margin-left: 5px;
  margin-bottom: 0rem;
}

.buttons {
  display: flex;
  justify-content: center;
}

.action-button {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 24px;
  background-color: #A7A7A7;
  color: #FFFFFF;
  border: none;
  padding: 12px 95px;
  border-radius: 10px;
  cursor: pointer;
  margin-left: 10px;
  margin-top: 16px;
}

.divider {
  width: 100%;
  height: 0.5px;
  background-color: #B2B2B2;
  margin-bottom: 20px;
}
</style>