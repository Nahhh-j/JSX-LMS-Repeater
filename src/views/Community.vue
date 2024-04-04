<template>
  <div>
    <div class="container">
        <img class="profile" img src="/src/assets/profile.jpg">
        <!-- <button type="button" onclick="location.href='#'">공부방</button> -->
      <div class="box1 nav-font box-shadow" @click=""> 
        <div class="icon"><i class="fa-regular fa-pen-to-square"></i></div>
        <div class="margin"></div>
        <RouterLink to="/community" style="color: white;">공부방</RouterLink>
      </div>
      <div class="box2 nav-font box-shadow"> 
        <div class="icon"><i class="fa-regular fa-comments"></i></div>
        <div class="margin"></div>
        <RouterLink to="/community" style="color: white;">이야기방</RouterLink>
      </div>
    </div>
    <RouterView/>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style lang="scss" scoped>
.profile{
  border-radius: 100px;
  width: 180px;
  padding: 20px;
}

.icon{
  font-size: 50px;
  color: white;
}

.margin{
  margin: 10px;
}

.nav-font{
  font-size: 30px;
}


.container {
  background-color: #00068E;
  width: 200px;
  height: 680px;
  border: 1px solid;
  border-radius : 20px;
  float: left;
  margin-top: 10%;
  margin-left: 2%;
}

.box1 {
  background-color: #004BE1;
  width: 180px;
  height: 200px;
  padding: 20px;
  border-top-left-radius : 20px;
  border-bottom-left-radius: 20px;
  margin: 5px;
  text-align: center;
}

.box2 {
  background-color: #00068E;
  width: 180px;
  height: 200px;
  padding: 20px;
  border-top-left-radius : 20px;
  border-bottom-left-radius: 20px;
  margin: 5px;
  text-align: center;
}

.box-shadow{
  box-shadow: 1px 1px 1px 1px black;
}

</style>