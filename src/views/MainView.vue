<template>
  <div>


<!-- header : jsx 로고 + 알림 벨 -->
    <header>
      <div class="logo-bell">
        <img src="/src/assets/로고.png" class="w-15pc" alt="">
        <div class="bell">
          <img src="/src/assets/bell_icon.png"  alt="">        
          <div class="alarm-num">
            oo
          </div>
        </div>
      </div>   
    </header>


<!-- div 안에 좌측/우측으로 나누어 두 개의 div 있음  -->
    <div class="d-flex">

      <!-- 1st div : 좌측 상~하단에 있는 요소  -->
      <div class="left-menu">
        <!-- 프로필 + 안내 문구 -->
        <section class="profile">
          <div class="m-20">
            <img src="/src/assets/듬이.png" class="profile-img">
          </div>
          <div class="profile-hi">
            <span class="profile-name">조나희</span>님<br>반갑습니다! 
            <!-- 이름 있는 부분 함수 처리 -->
          </div>
        </section>

        <br>
        <!-- 대학교 로고들 -->
        <div class="univ-logos">
            <img src="/src/assets/snu_logo.png" class="univ-logo" alt="">
            <img src="/src/assets/ysu_logo.png" class="univ-logo" alt="">
            <img src="/src/assets/kaist_logo.png" class="univ-logo" alt="">
            <img src="/src/assets/플러스.png" class="univ-logo" alt="">
            <!-- <div class="w-10pc border b-circle"> -->
              <!-- <i class="fa-solid fa-plus i-center h-100pc"></i> -->
              <!-- + 중앙에 위치시키는 법 모르겠음 ㅠ !!!!!!!!!!!! -->
              <!-- 아 근데 안해도 된다 ㅎㅎ 피그마에 아이콘 있다  -->
            <!-- </div> -->
        </div>
        
        <!-- 학습확인표(잔디) -->
        <img src="/src/assets/study_check.png" class="study-check" alt="">

      </div>
      
      
      <!-- 2nd div : 우측 상~하단에 있는 요소  -->
      <div class="right-menu">
        <router-link to="/home" class="main-menu">
          <img src="/src/assets/test_icon.png" class="main-menu-icon" alt="">
          <div class="main-menu-each">모의고사</div>
        </router-link>
        
        <router-link to="/community/content" class="main-menu">
          <img src="/src/assets/community_icon.png" class="main-menu-icon" alt="">
          <div class="main-menu-each">커뮤니티</div>
        </router-link>
        
        <router-link to="/manage" class="main-menu">
          <img src="/src/assets/manage_icon.png" class="main-menu-icon" alt="">
          <div class="main-menu-each">학습관리</div>
        </router-link>
      </div>
    </div>





  </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>

.logo-bell{
  background-color: #00068E;
  align-items: center;
  display: flex;
  height: 118px;
  justify-content: space-between;
  font-size: 50px;
  border-bottom-right-radius: 20px; /* 오른쪽 밑부분의 둥글기 정도 */
}

.bell{
  position: relative;
  margin: 0px 30px 20px 20px;
}

.alarm-num{
  border: 1px solid red;
  background-color: red;
  border-radius: 90%;
  width: 20px;
  height: 20px;
  position: absolute;
  top: 68%; /* 컨테이너 상단에서 중앙으로 이동 */
  left: 75%;
// 아래는 font 관련
  font-family: "Pretendard Variable";
  font-weight: medium;
  font-size: 10px;
  text-align: center;
  color: white;
}

.left-menu{
  width: 50%;
}

.profile{
  display: flex;
  padding: 2%;
  justify-content: center;
  align-items: center;
  width: 431px;
  height: 163px;
  background-color: #00068E;
  color: white;
  font-size: 20px;
  border-bottom-right-radius: 20px;
  border-bottom-left-radius: 20px;
  margin-top: -1px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.profile-hi {
  font-family: "Pretendard Variable";
  font-weight: light;
  font-size: 30px;
  padding: 3%;
  margin-left: 19px;
}

.profile-name {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 40px; /* 조나희의 글꼴 크기 */
}

.profile-img{
  width: 136px;
  height: 136px;

}

.univ-logos{
  background-color: rgb(204, 204, 204);
  box-shadow: 2px 4px 4px rgb(212, 203, 203);
  border-radius: 10px;
  padding: 2%;
  margin: 20px 20px 20px 40px;
  display: flex;
  justify-content: space-evenly;
}

.univ-logo{
  width: 100px;
  height: 100px;
  padding: 5px;
  margin: 0 10px 0 10px;
}

.study-check{
  width: 93%;
    /* padding: 2%; */
  margin: 0px 0px 0px 31px;
}

.right-menu{
  width: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 1%;
  margin-top: 28px;
}

.main-menu {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #00068E;
  color: white;
  border-radius: 20px;
  margin: 20px;
  padding: 1%;
  width: 86%;
  height: 30%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.main-menu-icon {
  margin-right: 30px;
}

.main-menu-each {
  font-family: "Pretendard Variable";
  font-weight: bold;
  font-size: 47px;
}

// ---------------------------------------------------

.background{
  background-color: #00068E
}


.box{
  border: 1px solid black;
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

.m-10px{
  margin: 10px 10px 10px 10px;
}

.w-30px{
  width: 30px;
}

.w-50px{
  width: 50px;
}

.w-10pc{
  width: 10%;
}

.w-15pc{
  width: 120.22px;
  height: 69px;
  margin: 30px;
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