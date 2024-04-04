<template>
  <div style="background-image: url(/src/assets/배경.png); height: 100%;">

    <!-- <img class="background-image" src="/src/assets/배경.png" style="z-index: -100;"></img> -->


    <!-- 뒤로가기 버튼 -->
    <div class="nav">
      <img src="@/assets/뒤로가기_1.png" class="back-button" @click="goBack" alt="뒤로가기">
      <img src="@/assets/plus_icon.png" style="margin-left: 960px;">  
    </div>

    <!-- 사이드 메뉴 -->
    <div class="sidebar">
        <img class="profile" img src="/src/assets/profile.jpg">
        <!-- <button type="button" onclick="location.href='#'">공부방</button> -->
      <div class="box1 nav-font box-shadow" @click=""> 
        <div class="icon"><i class="fa-regular fa-pen-to-square"></i></div>
        <div class="margin"></div>
        <RouterLink to="/community" style="color: white;" class="font">공부방</RouterLink>
      </div>
      <div class="box2 nav-font box-shadow"> 
        <div class="icon"><i class="fa-regular fa-comments"></i></div>
        <div class="margin"></div>
        <RouterLink to="/community" style="color: white;" class="font">이야기방</RouterLink>
      </div>
    </div>
    <RouterView/>

  </div>


</template>

<script>
export default {
  name: 'Navbar',
  methods: {
    goBack() {
      this.$router.push('/');
    },
  },
}
</script>

<style lang="scss" scoped>

.back-button{
  cursor: pointer;
}

.background-image{
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 100vh; /* 화면 전체 높이로 설정 */
}


.nav{
  padding: 40px;
}

.font{
  font-family: "Pretendard Variable";
  font-weight: bold;
}

.profile{
  border-radius: 100px;
  width: 180px;
  padding: 20px;
  margin-left: 10px;
}

.icon{
  font-size: 50px;
  color: white;
}

.margin{
  margin: 15px;
}

.nav-font{
  font-size: 30px;
}


.sidebar {
  background-color: #00068E;
  width: 200px;
  height: 645px;
  border: 1px solid;
  border-radius : 20px;
  float: left;
  // margin-top: 12%;
  margin-left: 3.5%;
}

.box1 {
  background-color: #004BE1;
  width: 180px;
  height: 190px;
  padding: 20px;
  border-top-left-radius : 20px;
  border-bottom-left-radius: 20px;
  margin: 17px;
  text-align: center;
}

.box2 {
  background-color: #00068E;
  width: 180px;
  height: 190px;
  padding: 20px;
  border-top-left-radius : 20px;
  border-bottom-left-radius: 20px;
  margin: 17px;
  text-align: center;
}

.box-shadow{
  box-shadow: 1px 1px 1px 1px black;
}

</style>