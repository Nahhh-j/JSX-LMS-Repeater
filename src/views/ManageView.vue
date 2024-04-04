<template>
<div class="box">
  <!-- container로 하면 오류나서 box만듦(bootstrap때문에) -->
 <!-- 이 위는 가장 큰 div (template의 div) -->

 <header class="header">
      <!-- 위에 nav 바 -->
      <nav class="p-3">
        <div class="nav-icons">
         <img src="/src/assets/back_icon.png" class="nav-icon" alt="">
         <img src="/src/assets/calender_icon.png" class="nav-icon" alt="">
        </div>  
      </nav>

      <!-- 총 학습시간 -->  
      <div class="total-time">
        07 : 43 : 32
      </div>
    </header>

    <!-- '타이머' 부분 -->  
    <section class="timer">
      타이머
    </section>

    <!-- 과목별 타이머 부분 -->
    <section class="subject-timers">
      <div class="d-flex s-between">
        <div class="d-flex">
          <img src="/src/assets/play_red.png" class="m-10px" alt="">
          <div class="subject-name">국어</div>
        </div>
        <div class="subject-timer">01 : 02 : 42</div>
      </div>
      <hr>
      <div class="d-flex s-between">
        <div class="d-flex">
          <img src="/src/assets/play_orange.png" class="m-10px" alt="">
          <div class="subject-name">영어</div>
        </div>
        <div class="subject-timer">01 : 02 : 42</div>
      </div>
      <hr>
      <div class="d-flex s-between">
        <div class="d-flex">
          <img src="/src/assets/play_yellow.png" class="m-10px" alt="">
          <div class="subject-name">수학</div>
        </div>
        <div class="subject-timer">01 : 02 : 42</div>
      </div>
      <hr>
      <div class="d-flex s-between">
        <div class="d-flex">
          <img src="/src/assets/play_green.png" class="m-10px" alt="">
          <div class="subject-name">한국사</div>
        </div>
        <div class="subject-timer">01 : 02 : 42</div>
      </div>
      <hr>
      <div class="d-flex s-between">
        <div class="d-flex">
          <img src="/src/assets/play_green.png" style="filter: saturate(200%)" class="m-10px" alt="">
          <div class="subject-name">운동</div>
        </div>
        <div class="subject-timer">01 : 02 : 42</div>
      </div>
      <hr>
      <div class="d-flex s-between">
        <div class="d-flex">
          <img src="/src/assets/play_orange.png" style="filter: saturate(200%)" class="m-10px" alt="">
          <div class="subject-name">코딩</div>
        </div>
        <div class="subject-timer">01 : 02 : 42</div>
      </div>
    </section>

    <!-- (+) 버튼 -->
    <div class="plus">
      <img src="/src/assets/plus_icon.png" alt="">
    </div>







 <!-- 이 아래는 가장 큰 div (template의 div) -->
</div>
</template>

<script setup>

</script>

<style lang="scss" scoped>

.header{
  background-color: #00068E;
  border-bottom-left-radius: 20px; /* 왼쪽 밑부분의 둥글기 정도 */
  border-bottom-right-radius: 20px; /* 오른쪽 밑부분의 둥글기 정도 */
}

.box{
  // background-color: #00068E;
  position: relative;
}

.nav-icons{
  display: flex;
  justify-content: space-between;
}

.nav-icon{
  width: 5%;
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
  // position: relative;
  overflow: auto; /* 내용이 넘칠 때 스크롤 바 표시 */
  background-color: white;
}

.timer{
  border-bottom: 1px solid rgb(196, 196, 196);
  border-bottom-left-radius: 20px; /* 왼쪽 밑부분의 둥글기 정도 */
  border-bottom-right-radius: 20px; /* 오른쪽 밑부분의 둥글기 정도 */
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1%;
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 30px;
  color: gray;
}

.subject-name{
  padding: 20px;
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 30px;
}

.subject-timer{
  padding: 20px;
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 30px;
  color: gray;
}


.plus{
  position: absolute; /* 절대 위치로 설정 */
        top: 730px; /* 컨테이너 상단에서 중앙으로 이동 */
        left: 90%; /* 컨테이너 좌측에서 중앙으로 이동 */
        // transform: translate(-50%, -50%); /* 이미지의 중앙 정렬 */
}

// -----------------------------------------


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
  margin: 10px 10px 10px 10px;
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
 

</style>